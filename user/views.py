from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django import forms
import pandas as pd
# Create your views here.
from user.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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
        aca = request.POST.get("aca")
        clas = request.POST.get("class")
        password = request.POST.get("password")
        age = request.POST.get("age")
        stu.objects.create(name = name, stuid = stuid, academy= aca, stuclass=clas, age= age,gender=1, password=password )
        return redirect("/denglu/")
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




