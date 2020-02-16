from django.db import models

# Create your models here.
from datetime import datetime

from organization.models import *

class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构',on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('cj','初级'),("zj",'中级'),('gj','高级')),max_length=2)
    learn_times = models.IntegerField(default=0,verbose_name='学习时差（分钟）')
    students = models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="coruses/%Y/%m",verbose_name="封面图",max_length=100,blank=True)
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    category = models.CharField(max_length=20,verbose_name="课程类别",default='')
    tag = models.CharField(max_length=10,verbose_name="课程标签",default='')
    teacher = models.ForeignKey(Teacher, verbose_name='课程讲师',on_delete=models.CASCADE,null=True,blank=True)
    youneed_know = models.CharField(max_length=300,verbose_name="课程须知",default='')
    teacher_tell = models.CharField(max_length=300,verbose_name="老师告知",default='')
    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_video(self):
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    url = models.CharField(max_length=200,verbose_name='访问地址',default='')
    learn_times = models.IntegerField(default=0, verbose_name='学习时差（分钟）')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    download = models.FileField(upload_to='course/course/%Y/%m',verbose_name='资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
