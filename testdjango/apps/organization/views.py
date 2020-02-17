from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import UserAskForm
from django.http import HttpResponse
from courses.models import Course
from operation.models import *
from django.db.models import Q
class AddUserAskView(View):
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')



class OrgView(View):
    #课程机构列表功能
    def get(self,request):
        all_orgs = CourseOrg.objects.all()

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_orgs = all_orgs.filter(
                Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) )

        all_cities = CityDict.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get('sort','')
        if sort:
            if sort=='students':
                all_orgs = all_orgs.order_by('-students')
            elif sort=='courses':
                all_orgs = all_orgs.order_by('-course_nums')
        org_nums = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_cities':all_cities,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort
        })


class OrgHomeView(View):
    def get(self,request,org_id):
        current_page = 'home'


        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        has_fav = False;
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id,fav_type=2):
                has_fav = True
        return render(request,'org-detail-homepage.html',
                      {'all_courses':all_courses,
                        'all_teachers':all_teachers,
                       'course_org':course_org,
                       'current_page':current_page ,
                       'has_fav':has_fav,
                       })

class OrgCourseView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        current_page = 'course'
        has_fav = False;
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-course.html',
                      {'all_courses':all_courses,
                       'course_org':course_org,
                       'current_page': current_page,
                       'has_fav': has_fav,
                       })

class OrgDescView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        current_page = 'desc'
        has_fav = False;
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-desc.html',
                      {
                       'course_org':course_org,
                       'current_page': current_page,
                        'has_fav': has_fav,
                       })

class OrgTeacherView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        current_page = 'teacher'
        has_fav = False;
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-teachers.html',
                      {'all_teachers':all_teachers,
                       'course_org':course_org,
                       'current_page': current_page,
                       'has_fav': has_fav,
                       })


class AddFavView(View):
    def post(self,request):

        id = request.POST.get('fav_id',0)
        type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated:
            #判断登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_record = UserFavorite.objects.filter(user=request.user, fav_id=int(id), fav_type=int(type))

        if exist_record:
            exist_record.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(id)>0 and int(type)>0:
                user_fav.fav_id = int(id)
                user_fav.fav_type = int(type)
                user_fav.user = request.user
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')

class TeacherListView(View):
    def get(self,request):
        all_teachers = Teacher.objects.all()
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_teachers = all_teachers.filter(
                Q(name__icontains=search_keywords) | Q(work_company__icontains=search_keywords))
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_teachers = all_teachers.order_by('-click_nums')
        sorted_teacher = Teacher.objects.all().order_by('-click_nums')[:3]
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_teachers, 5, request=request)
        teachers = p.page(page)
        return render(request,'teachers-list.html',{
            'all_teachers':teachers,
            'sorted_teacher':sorted_teacher,
            'sort': sort,
            'teacher_nums':len(all_teachers)
        })

class TeacherDetailView(View):
    def get(self,request,teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        all_courses = Course.objects.filter(teacher=teacher)
        sorted_teacher = Teacher.objects.all().order_by('-click_nums')[:3]
        has_teacher_faved = False
        if UserFavorite.objects.filter(user=request.user,fav_type = 3,fav_id = teacher.id):
            has_teacher_faved = True
        has_org_saved = False
        if UserFavorite.objects.filter(user=request.user,fav_type = 2,fav_id = teacher.org.id):
            has_org_saved = True
        return render(request, 'teacher-detail.html', {
            'teacher':teacher,
            'all_courses':all_courses,
            'sorted_teacher': sorted_teacher,
            "has_teacher_faved":has_teacher_faved,
            "has_org_saved":has_org_saved
        })