# def login ():
#     print("这是登录函数")
# def say_hello():
#     print("hello")
# login();
# say_hello();
# def buy():
#     return "一桶水果茶",20 #return 返回元组形式给调用者
# print(buy());
# #返回值的三种情况总结
# def funb(b,a=2):
#     return a*b
# print(funb(2));
# def func(*args):
#     print(args)
#     print(type(args))
#     return 233
# print(func(1,2,3,4,"apple",9,10))
def study():
    global  name;
    name='python base'
    print("we are learning {name}!".format(name=name))
study()
add = lambda a,b: a+b
print(add(1,2))
funb = lambda  name:name
print(funb(name))

A = '孙浩烜'
B = '张宇'
print(A+B)