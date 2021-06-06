from django.contrib import admin

# Register your models here.
from .models import comp
from .models import stu,job
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .resource import StuResource,JobResource



class PersonAdmin(ImportExportModelAdmin):
    resource_class = StuResource
    list_display = ('name', 'stuid', 'stuclass', 'academy')  # 列表显示字段
    list_per_page = 10  # 每页显示数据数
    # list_display_links = ('')  #控制list_display中的字段哪些可以链接到修改页
    # date_hierarchy = 'pub_date' #按日期月份筛选

    list_filter = ['stuclass']  # 以字段过滤，也就是过滤器
    search_fields = ['name']  # 添加搜索框进行模糊查询
    list_editable = ['stuclass','stuid','academy']  # 添加可在列表页编辑的字段
    ordering = ('-stuclass',)  # 排序
admin.site.register(stu,PersonAdmin)


class jobAdmin(ImportExportModelAdmin):
    resource_class = JobResource
    list_display = ('job_name', 'company_locale','guimo','job_salary')  # 列表显示字段
    list_per_page = 10  # 每页显示数据数
    # list_display_links = ('')  #控制list_display中的字段哪些可以链接到修改页
    # date_hierarchy = 'pub_date' #按日期月份筛选
    search_fields = ['job_name']  # 添加搜索框进行模糊查询
    ordering = ('-job_salary',)  # 排序
admin.site.register(job,jobAdmin)

class compAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')  # 列表显示字段
    list_per_page = 10  # 每页显示数据数
    # list_display_links = ('')  #控制list_display中的字段哪些可以链接到修改页
    # date_hierarchy = 'pub_date' #按日期月份筛选
    search_fields = ['name']  # 添加搜索框进行模糊查询
    ordering = ('-type',)  # 排序


admin.site.register(comp,compAdmin)

#登录时/后台主界面显示的名称
admin.site.site_header = '大学生就业信息系统后台'
admin.site.site_header = '大学生就业信息系统后台'
#title显示的名称
admin.site.site_title = '就业平台管理后台'



# class stuAdmin(admin.ModelAdmin):
#     list_display = ('name','stuid','stuclass','academy')   #列表显示字段
#     list_per_page = 10    #每页显示数据数
#     # list_display_links = ('')  #控制list_display中的字段哪些可以链接到修改页
#     # date_hierarchy = 'pub_date' #按日期月份筛选
#
#     list_filter = ['stuclass']     #以字段过滤，也就是过滤器
#     search_fields = ['name']     #添加搜索框进行模糊查询
#     list_editable = ['stuclass']  #添加可在列表页编辑的字段
#     ordering = ('-stuclass',)  #排序
# admin.site.unregister(stu)   #先删除再创建一个新的
# admin.site.register(stu,stuAdmin)   #绑定模型类和注册模型管理器




# name = models.CharField('岗位名称', max_length=20, null=True)
    # work_demand = models.CharField('标题', max_length=40, null=True)
    # company_locale = models.CharField('地点', max_length=20, null=True)
    # company_name = models.CharField('公司名', max_length=40, null=True)
    # guimo = models.CharField('公司规模', max_length=20, null=True)
    # job_salary = models.CharField('公司薪资', max_length=20, null=True)
    # job_salary_fif = models.BooleanField('薪资是否超过15K', choices=((True, '是'), (False, '否')), null=True)
    # demand = models.CharField('demand', max_length=20, null=True)