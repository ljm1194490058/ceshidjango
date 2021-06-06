from import_export import resources
from .models import *


class StuResource(resources.ModelResource):
    class Meta:
        model =  stu
        # import_id_fields = ['id','name','stuid','stuclass','academy', 'ability', 'age','gender']
        # exclude = ['id']   #排除id
        #上一行决定了update_or_create，可以避免重复导入

class JobResource(resources.ModelResource):
    class Meta:
        model = job
