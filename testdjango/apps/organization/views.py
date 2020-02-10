from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CourseOrg,CityDict

class OrgView(View):
    #课程机构列表功能
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 2, request=request)
        orgs = p.page(page)
        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_cities':all_cities,
            'org_nums':org_nums,
        })