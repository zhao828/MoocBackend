# Generated by Django 2.0 on 2020-02-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
    ]