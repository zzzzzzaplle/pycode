from zipfile import stringEndArchive64Locator

print("hello world")
#运行文件推荐第一种方式 直接空白处run
x = 10.123
y = 20
# print(x+y,x-y,x*y,x*y,sep="\n",end="|||||")
# print("hello world")
#sep 用来间隔多个值用什么符号
#变量严格区分大小写、
# print(type(x),type(y),sep="\n")
# ma=1+2j
# mb=2+3j
# print(ma+mb)
# """" 214421412"""
# # 占位符号
# name ="bingbing"
# print("我的名字:%s" % name)
# a=123
# print("%06d" %a)
# print(False+True+True)
# abc=10.211251251
# print("%.4f" % abc)
# v1=5
# v2=2
# 算数运算符
# print(v1//v2)#整除忽略小数部分
# print(v1/v2)#除法
# print(v1%v2)#取余
# 取幂，v1的v2次方
# print(v1**v2)
# 运算过程中有浮点数结果就是用浮点数表示
# name_1=input("请输入字符")
# print(name_1)
age=21

# 逻辑运算符
# value1='haha'
# value2='xix'
# # and左右两边符合
# # or一边符合即可
# # not 表示相反的结果
# print(not 3>9)
#
# if value1 == 'haha' :
#     print("a and b are laughing")
# else:
#     print("a and b are not laughing")
# # 三目运算表达式
# print("nihao")if value1 == 'haha' and value2 == 'xixi' else print("nibuhao")
# # if else 多选一
# score=120
# if 85<=score<=90:
#      print("just 1\n")
# elif  91<=score<=100:
#      print("just 2\n")
# else:
#     print("just 4\n")
# i=1
# while i<= 5:
#     print("this is the first time")
#     j=1
#     while j <= 5:
#         print(f"this is the second time j : {j}")
#         j=j+1
#     i +=1
#     print(i)
#
str = 'hello python'
# str1=123 整形就不是一个可迭代对象
# 可迭代对象就是去取遍历取值的整体，现在记住字符串是可迭代对象
# for i in str:
#     print(i)

# range用来记录循环次数相当于一个计数器
# 包前不包后 左闭右开
sum=0
for i in range(1,101):
    sum+=i
print(sum)
# range里面只写一个数就是循环次数
name='bingbing1'
# i =1
# for i in range(0,5):
#     print(name[i])
# print(name[0:5])

# print(name[-1::1])
# print(name[3:])#从3到末尾

# print(name[-1:-5:-1])
# print(name.index('bing'))

# print(name.startswith('bing'))
# print(name.startswith('ing',1,7))
# print(name.endswith('g'))
# print(name.isupper())
# print('STX'.isupper())
# print(name.islower())
# print(name.replace('g','A',5))
# split指定分隔符切割
name1=['bing,bing','bushi','nihao',1]
print(name1[0:1])
# extend一般指的是可迭代对象，比如字符串，若是整则会报错
name1.extend(['nimahb'])
name1.insert(  3,'four')#在指定下标位置插入元素
print(name1)
list1=['zzz',"apple",'banana','orange']
print('1' in list1)
#写一段代码，判断名称是否存在
# in_name=input()
# if in_name in list1:
#     print(f"您输入的名称{in_name}在list1中")
# else:
#     print("不在其中")
#     list1.append(in_name)
# in_name2 = input()
# if in_name2 in list1:
#     print(f"您输入的名称{in_name2}在list1中")
# else:
#     print("不在其中")
#     list1.append(in_name2)
# print(list1)
# list1.sort()
# print(list1)
# # 列表推导式
# for item in range(1,60):
#     print(item)
# name2='zzq'
# age2=18
# tua=(name2,age2)
# print("%s的年龄是:%d" % tua)
# print("%s的年龄是:%d" % (name2,age2))
# 格式化输出本质就是个元组
# 字典基本格式 字典名={键1，值1，键2，值2}
# 键值对形式保存，键和值之间用:隔开
dic2={'name1':'bb',"name2":"aa","name3":"xixi" }
# 查看元素 不可以根据下标访问，只能根据键名访问
# print(dic2)
print(dic2.get('name1'))
print(dic2.get('name2'))
print(dic2.get('name4',"不存在" ))
dic2["name2"]='zzqg'
print(dic2.get('name2'))
print(eval("1010"+"241"))
# eval 可以用来执行字符串表达式返回表达式的值