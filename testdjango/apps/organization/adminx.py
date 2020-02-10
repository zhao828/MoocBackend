from .models import *
import xadmin



class CourseOrgAdmin(object):

    list_display = ['name', 'desc','click_nums', 'fav_nums','image', 'address','city', 'add_time']
    search_fields = ['name', 'desc','click_nums', 'fav_nums','image', 'address','city']
    list_filter = ['name', 'desc','click_nums', 'fav_nums','image', 'address','city__name', 'add_time']


class CityDictAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', 'add_time']


class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company', 'work_position','points','click_nums', 'fav_nums','add_time']
    search_fields = ['org','name','work_years','work_company', 'work_position','points','click_nums', 'fav_nums']
    list_filter = ['org','name','work_years','work_company', 'work_position','points','click_nums', 'fav_nums','add_time']




xadmin.site.register( CityDict, CityDictAdmin)

xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)