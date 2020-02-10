"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
import xadmin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.static import  serve
from users.views import *
from organization.views import *
from testdjango.settings import MEDIA_ROOT
urlpatterns = [
    url('xadmin/', xadmin.site.urls),

    url('^$',TemplateView.as_view(template_name =  'index.html'),name = 'index'),
    url('^login/$',LoginView.as_view(),name = 'login'),
    url('^register/$',RegisterView.as_view(),name = 'register'),
    url('^captcha/',include('captcha.urls')),
    url('^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name='user_active'),
    url('^reset/(?P<active_code>.*)/$',ResetView.as_view(),name='reset_pwd'),
    url('^forget/$',ForgetPwdView.as_view(),name='forget_pwd'),
    url('^modify_pwd/$',ModifyPwdView.as_view(),name='modify_pwd'),

    #课程机构首页
    url('^org_list/$',OrgView.as_view(),name='org_list'),
    #配置上传文件访问处理
    url('^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
]
