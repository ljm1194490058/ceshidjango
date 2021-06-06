# Generated by Django 2.2 on 2021-05-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='公司名')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
            ],
            options={
                'verbose_name_plural': '公司信息表',
            },
        ),

        migrations.CreateModel(
            name='stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('gender', models.BooleanField(choices=[(True, '女'), (False, '男')], verbose_name='性别')),
                ('age', models.IntegerField(default=18, verbose_name='年纪')),
                ('stuid', models.CharField(max_length=20, verbose_name='学号')),
                ('stuclass', models.CharField(max_length=20, verbose_name='班级')),
                ('academy', models.CharField(max_length=20, verbose_name='学院')),
                ('ability', models.TextField(blank=True, null=True, verbose_name='技能')),
            ],
            options={
                'verbose_name_plural': '学生信息表',
            },
        ),
    ]