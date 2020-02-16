from django.conf.urls import url,include
from .views import *




urlpatterns = [

    url('^list/$',CourseListView.as_view(),name='course_list'),
    url('^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(),name='course_detail'),
    url('^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(),name='course_info'),
    url('^comment/(?P<course_id>\d+)/$',CommentView.as_view(),name='course_comment'),
    url('^add_comment/$',AddCommentsView.as_view(),name='add_comment'),
    url('^video/(?P<video_id>\d+)/$',VideoPlayView.as_view(),name='video_play'),

]