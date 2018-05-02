#coding=utf-8
from functools import reduce
'''
reduce
'''
l=[1,2,3,4,5,6,7,8,9]
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x*y,l,10))#添加初始值
'''
map集合中的元素依次执行函数然后返回
'''
print(list(map(lambda x:x*x,l)))
'''
filter(func,seq)过滤
'''
print(list(filter(lambda x:x%2==0,l)))
'''
装饰器 需要是高阶函数
'''
def hello(fn):
    def wrapper():
        print("hello, %s"%fn.__name__)
        fn()
        print("goodbye,%s"%fn.__name__)
    return wrapper
@hello
def foo():
    print("I am foo")
foo()

