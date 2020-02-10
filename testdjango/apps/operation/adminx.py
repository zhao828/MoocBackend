from .models import *
import xadmin


class UserAskAdmin(object):

    list_display = ['name', 'mobile','course_name', 'add_time']
    search_fields = ['name', 'mobile','course_name', ]
    list_filter = ['name', 'mobile','course_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user','course', 'comments', 'add_time']
    search_fields = ['user','course', 'comments', ]
    list_filter = ['user','course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id','fav_type', 'add_time']
    search_fields =['user', 'fav_id','fav_type']
    list_filter = ['user', 'fav_id','fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user','message',  'add_time','has_read']
    search_fields = ['user','message', 'has_read']
    list_filter = ['user','message',  'add_time','has_read']


class UserCourseAdmin(object):
    list_display = ['user','add_time','course']
    search_fields = ['user','course']
    list_filter = ['user','add_time','course__name']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)