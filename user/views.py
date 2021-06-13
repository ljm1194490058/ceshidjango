from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django import forms
import pandas as pd
# Create your views here.
from user.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#核心算法函数
def forest(list,df):
    df['job_salary_range'] = df['job_salary_range'].astype(str).map({'0-10K': 0, '10-20K': 1, '20-30K': 2, '>30K': 3})
    y = df['job_salary_range']
    x = df.drop(labels=['job_salary_range', 'job_name', 'company_name'], axis=1)  # 删除掉无关列
    x = pd.get_dummies(x)    #独热编码
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=5)  # test_size是x，y测试集占总的20%
    rfc = RandomForestClassifier(max_depth=None, min_samples_split=2,
                                 random_state=0)  # 实例化rfc = rfc.fit(xtrain, ytrain)    #用训练集数据训练
    rfc = rfc.fit(xtrain, ytrain)
    # result = rfc.score(xtest, ytest)  # 导入测试集，rfc的接口score计算的是模型准确率accuracy
    res = rfc.predict(list)
    return res


def xinzi_predict(request):
    if request.method == 'GET':
        return render(request,'predict_xinzi.html')
    else:
        list1 = []
        list_sum = []
        java1 = request.POST.get('java1')              #JAVA要求
        spring1 = request.POST.get('spring1')
        sql1 = request.POST.get('sql1')
        python1 = request.POST.get('python1')           #Python要求
        linux1 = request.POST.get('linux1')
        spider1 = request.POST.get('spider1')
        html1 = request.POST.get('html1')              # web要求
        cssjs1 = request.POST.get('cssjs1')
        vue1 = request.POST.get('vue1')
        jiqi1 = request.POST.get('jiqi1')               # 算法工程师要求
        tuxiang1 = request.POST.get('tuxiang1')
        C1 = request.POST.get('C1')
        city = request.POST.get('city')
        demand = request.POST.get('demand')
        guimo = request.POST.get('guimo')
        a = request.POST.get('job_name')
        global df  #声明全局变量
        if a == 'Java开发工程师':
            list1.append(java1)
            list1.append(spring1)
            list1.append(sql1)
            df = pd.read_csv('C:\\Users\\独为我唱\\Desktop\\data_sum\\updata_java_ceshi222.csv', encoding='gbk')
        elif a == 'Python开发工程师':
            list1.append(python1)
            list1.append(linux1)
            list1.append(spider1)
            df = pd.read_csv('C:\\Users\\独为我唱\\Desktop\\data_sum\\updata_python_ceshi.csv', encoding='gbk')
        elif a == 'web前端开发师':
            list1.append(html1)
            list1.append(cssjs1)
            list1.append(vue1)
            df = pd.read_csv('C:\\Users\\独为我唱\\Desktop\\data_sum\\updata_web_ceshi.csv', encoding='gbk')
        elif a == '算法工程师':
            list1.append(jiqi1)
            list1.append(tuxiang1)
            list1.append(C1)
            df = pd.read_csv('C:\\Users\\独为我唱\\Desktop\\data_sum\\updata_suanfa_ceshi.csv', encoding='gbk')
        city = city.split(',')
        list1.extend(city)
        demand = demand.split(',')
        list1.extend(demand)
        guimo = guimo.split(',')
        list1.extend(guimo)
        list_sum.append(list1)  # 得到双中括号包起来的列表，并且里面的元素都变成了算法可以直接调用的元素

        res = forest(list_sum,df)
        if res[0] == 0:
            message = '预测薪资范围是每月5-10K'
        elif res[0] == 1:
            message = '预测薪资范围是每月10-20K'
        elif res[0] == 2:
            message = '预测薪资范围是每月20-30K'
        else:
            message = '预测薪资范围是每月在30k以上'
    return render(request, 'predict_xinzi.html', {'message': message})

def ceshi2(request):
        return render(request
                  ,'ceshi2.html',
                  {
                      'name':'all',
                      'users':['ab','qwe'],
                      'user_dict':{'k1':'v1', 'k2':'v2'},
                      'us':[
                          {'id':1,'name':'xiaomm','email':'1111@qq.com'},
                          {'id':2, 'name':'xoapxaopx', 'email':'ssss@163.com'},
                      ]
                  }
            )



def job_demand(request):
    return render(request, 'job_demand_pie_sum.html',)
def xinzi_bar(request):
    return render(request,'xinzi_bar_sum.html')


def denglu(request):
    if request.method == "GET":
        return render(request, 'zhuce.html')
    else:
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        test = stu.objects.filter(stuid = name, password = pwd)
        name = test.values('name')[0]['name']      #通过学号和登录密码查询到学生的姓名
        if test:
            return render(request, 'zhuye.html', {'username': name})
        else:
            error_msg = '用户名或密码错误'
            return render(request,'zhuce.html',{"error_msg":error_msg})


def zhuce(request):
    if request.method == "POST":
        name = request.POST.get("uname")
        stuid = request.POST.get("stuid")
        if stu.objects.filter(stuid = stuid):
            return render(request, 'zhuce.html',{"message": '该账号已存在，请重新注册！'})
        aca = request.POST.get("aca")
        clas = request.POST.get("class")
        password = request.POST.get("password")
        age = request.POST.get("age")
        stu.objects.create(name = name, stuid = stuid, academy= aca, stuclass=clas, age= age,gender=1, password=password )
        return render(request, 'zhuce.html',{"msg":'注册成功'})
    else:
        return render(request, "zhuce.html")



#总的岗位数量的饼图和柱状图
def pie_bar_test(request):
    df = pd.read_csv('C:\\Users\\独为我唱\\Desktop\\data_sum\\all.csv', encoding='gbk' , low_memory=False,converters={'work_demand':str})
    dd = df.loc[df['job_name'] != '其他职业']
    pie_data_index = list(dd['job_name'].value_counts().index)
    pie_data =  list(dd['job_name'].value_counts())
    data = []
    for i in range(len(pie_data)):
        dic = {}
        dic['name'] = pie_data_index[i]
        dic['value'] = pie_data[i]
        data.append(dic)
    return render(request, 'test.html', {"pie_data_index":pie_data_index,
                                                        "data":data,
                                                        "pie_data":pie_data,
                                                        })
#辅助函数，用于主展示屏展示工作要求饼图
def abi_class(list):
    newlist = []
    for ele in list:
        newlist += ele.split(',')
    newlist = [x.strip() for x in newlist]  # 这两行是为了使原df的工作要求单个呈现以逗号分割
    res = dict()
    for a in set(newlist):
        res[a] = newlist.count(a)
    ll = sorted(res.items(), key=lambda item: item[1], reverse=True)  # 按从大到小排序每种技能的出现次数
    ll = ll[0:6]  # 取出list前6个值
    return ll
def test_pic(request):
    df = pd.read_csv('C:\\Users\\独为我唱\\Desktop\\data_sum\\all.csv', encoding='gbk' , low_memory=False,converters={'work_demand':str})
    # 取出每个城市及其岗位数
    job = list(df['company_locale'].value_counts().index)
    job1 = list(df['company_locale'].value_counts())

    #修改成元素为字典的list，以便地图绘制
    data2 = []
    for i in range(len(job)):
        dic = {}
        dic['name'] = job[i]
        dic['value'] = job1[i]
        data2.append(dic)

    # 取出java技能各占比
    a = df['work_demand'].str.split()
    list1 = []
    x = a.copy()
    for i in range(len(x)):
        if 'Java' in df['job_name'][i]:
            list1 += x[i]
    list1 = abi_class(list1)
    abi_num = []
    abi_name = []
    for i in range(len(list1)):
        if i < 6:
            abi_num.append(list1[i][1])
            abi_name.append(list1[i][0])
    abi_snum=[]
    for i in range(len(abi_name)):
        dict = {}
        dict['value'] = abi_num[i]
        dict['name'] = abi_name[i]
        abi_snum.append(dict)

    #取出java、python和web在各地区薪资图
    dff = df.loc[df['job_name'] == 'Java']
    grouped2 = dff.groupby([df['job_name'], df['company_locale']])
    a = grouped2['job_salary'].mean()
    a = a.map(lambda x: int(x))
    java_cities_price = a.values.tolist()

    ddff= df.loc[df['job_name'] == 'Python']
    grouped2 = ddff.groupby([df['job_name'], df['company_locale']])
    a = grouped2['job_salary'].mean()
    a = a.map(lambda x: int(x))
    python_cities_price = a.values.tolist()

    ddd= df.loc[df['job_name'] == 'web']
    grouped2 = ddd.groupby([df['job_name'], df['company_locale']])
    a = grouped2['job_salary'].mean()
    a = a.map(lambda x: int(x))
    web_cities_price = a.values.tolist()

    dfdf = df.loc[df['job_name'] == '大数据']
    grouped2 = dfdf.groupby([df['job_name'], df['company_locale']])
    a = grouped2['job_salary'].mean()
    a = a.map(lambda x: int(x))
    hadoop_cities_price = a.values.tolist()

    #得到招聘岗位数排名前八的公司，返回元素为字符串的列表
    a = list(df['company_name'].value_counts().index)
    b = list(df['company_name'].value_counts())
    ll = []
    for i in range(0, 10):
        c = str(i + 1) + '  ' + a[i] + '  ' + str(b[i]) + '个岗位'
        ll.append(c)

    #取出不同岗位类型平均薪资
    gp = df.groupby('demand')
    a = gp['job_salary'].mean().sort_values(ascending=False)
    job_price_index = a.index.tolist()
    job_price = a.values.tolist()
    for i in range(len(job_price)):
        job_price[i] = int(job_price[i])
    # job_price = np.trunc(job_price)              #对list每个元素进行取整

    return render(request, '../templates/index.html', {"job": job,
                                                       "job1": job1,
                                                       "data2":data2,
                                    "job_price_index":job_price_index,
                                    "job_price":job_price,
                                    "abi_name":abi_name,
                                    "abi_snum":abi_snum,
                                    "java_cities_price":java_cities_price,
                                    "python_cities_price":python_cities_price,
                                    "web_cities_price":web_cities_price,
                                    "hadoop_cities_price":hadoop_cities_price,
                                    "ll":ll,
                                                       })




