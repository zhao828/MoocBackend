# Generated by Django 2.0 on 2020-02-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20200208_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=models.TextField(max_length=300, verbose_name='机构描述'),
        ),
    ]
