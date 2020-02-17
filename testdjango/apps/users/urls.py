from django.conf.urls import url,include
from .views import *




urlpatterns = [

    url('^info/$',UserinfoView.as_view(),name='user_info'),


]