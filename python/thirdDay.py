#coding=utf-8
#class中的方法的第一个函数的参数时自己的指针
#构造函数__init__(self):
#封装 继承 多态
#isinstance(typeA,typeB)/type判断是否是相同的类型
#setattr设置属性
#hasattr判断属性是否存在
#getattr获取属性
#实例属性和类属性
'''
模块和包
'''
import sys
paths= sys.path
print(type(paths))
for path in paths:
    print(path)