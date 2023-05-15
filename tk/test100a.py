#coding=utf-8
# # lesson 1
# s="a_b_c"
# print(s.split("_"))

# # lesson 2
# ls=["a","b","c"]
# print(str.join("_",ls))
# s1=""
# for i in ls:
#     s1+="_"+i
# print(s1.lstrip("_"))

# # lesson 3
# s='a b c'
# print(s.replace(' ','%20'))

# s="a b c"
# print(s.replace(" ","%20"))

# # lesson 4
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end=" ")
#     print()

# # lesson 10
# B="Hello"
# A=" sssss kHello slsls Hello"
# def test(Str,subStr):
#     pos=-1
#     while True:
#         # pos1=Str.find(subStr,pos+1)
#         pos1=str.find(Str,subStr,pos+1)
#         if(pos1==-1):
#             return pos
#         pos=pos1
# print(test(A,B))
# print(str.find(A,B,0))
# print(A.upper())
# print(A.strip())
# print(B.rstrip())
# print(B.rstrip("o"))




# -*- coding: UTF-8 -*-
import csv
import datetime
import json
import time


json_Example={
    "id":1,
    "name":"Kitty",
    "info":[
        {
            "gender":"女"
        },
        {
            "birth":"2000-01-01"
        }
    ]
}
print(json_Example["info"][0]["gender"])
# print(json_Example.keys)
fileName ="a.csv"
s="ssss\nbbbb\ncccc\n"
# with open(fileName,'a',newline="") as file: # newline=""：保存数据时去除空行
#     # writer=csv.writer(file)
# # # writer.writerow(需要保存的数据变量)
# #     writer.writerows(json_Example) # 数据取键名，一个字母一列
# #     writer.writerow("")
# #     # 数据取键名，一个字段一列      下面两行代码运行相同
# #     writer.writerow(json_Example)
# #     writer.writerow(json_Example.keys())
#     file.write(s)

str1 = json.dumps(json_Example, indent=2) #indent=2按照缩进格式
str2=json.dumps(json_Example,indent=0)
# with open(fileName,"a",newline="") as file:
#     #file.write(str1)
#     json.dump(json_Example,file,indent=2) #json对象写入文件
#     pass
with open(fileName) as file:
    json_Example1=json.load(file)
    json_Example1["info"][0]["gender"]="品男林"
with open(fileName,"w",encoding='utf-8') as file:
    json.dump(json_Example1,file,indent=4)


order_info={
    '订单需求信息': {'订单任务编号':'','观测目标名称':'','观测目标经度':''},
    '任务规划结果': {'子订单任务编号':'','观测目标名称':''},   
}

json_str=json.dumps(order_info,indent=4,ensure_ascii=False)
with open(r"test.json",'w',encoding='utf-8') as json_file:
    json_file.write(json_str)
print(json_Example1)

date1=datetime.datetime.now()
print(date1)
date1=date1+datetime.timedelta(days=1)
print(date1.strftime("%Y-%m-%d %H%M:%S %f"))

time1=time.localtime(time.time())
# time1=time.asctime(time1)
print(time1)
print(time.strftime("%Y-%m-%d %H%M:%S %f",time1))