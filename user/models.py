from django.db import models

# Create your models here.

class job(models.Model):
    job_name = models.CharField('岗位名称', max_length=20, null=True)
    work_demand = models.CharField('能力要求', max_length=80, null=True)
    company_locale = models.CharField('地点', max_length=20, null=True)
    company_name = models.CharField('公司名', max_length=100, null=True)
    guimo = models.CharField('公司规模', max_length=20, null=True)
    job_salary = models.CharField('公司薪资', max_length=20, null=True)
    job_salary_fif = models.BooleanField('薪资是否不超过15K', choices=((True, '是'), (False, '否')), null=True)
    demand = models.CharField('demand', max_length=20, null=True)

    def __unicode__(self):
        return self.job_name

    class Meta:
        verbose_name_plural = '招聘岗位信息表'


class stu(models.Model):
    name = models.CharField(max_length=20, unique= True, verbose_name='姓名') #,help_text='不要写小名'
    gender = models.BooleanField('性别',choices=((True,'女'),(False,'男')))
    age = models.IntegerField(default=18, verbose_name='年纪')
    stuid = models.CharField(max_length=20, verbose_name='学号')
    stuclass = models.CharField(max_length=20, verbose_name= '班级')
    academy = models.CharField(max_length=20, verbose_name='学院')
    ability = models.TextField(blank= True, null = True, verbose_name='技能')    #可插入为空或设置default
    password = models.CharField(max_length=20,null= True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '学生信息表'


class comp(models.Model):
    name = models.CharField(max_length=20, verbose_name='公司名')
    type = models.CharField(max_length=20, verbose_name='类型')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = '公司信息表'



class test(models.Model):
    uname = models.CharField(max_length=32)
    upwd = models.CharField(max_length=64)