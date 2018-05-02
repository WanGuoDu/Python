#coding=utf-8
import os
print(os.name)
print(os.uname_result)
#文件读写以及函数式编程
with open("demo.py",'r') as f:
    for line in f:
        print(line)
os.path.abspath('.')
ospath= os.path.join("/usr/dev",'picture')
print(ospath)
os.mkdir('../python/testDir')
os.rmdir('../python/testDir')
fileInfo= os.path.split("../python/demo.py")
print(fileInfo)
endTypeInfo=os.path.splitext("../python/demo.py")
print(endTypeInfo)
os.rename("../python/demo.py","demo1.py")
os.rename("../python/demo1.py","demo.py")
#os.remove("fileName")
#import shutil 复制文件
dirs= [y for y in os.listdir("../../") if os.path.isdir(y)]
for path in dirs:
    print(path)
'''
序列化和反序列化
'''
#import pickle 为保证兼容python2
try:
    import cPickle as pickle
except ImportError:
    import pickle
d=dict(name='joydu',age=22,score=100)
str=pickle.dumps(d)#序列化处理
print(str)
with open("../python/dumps.txt",'wb') as wr:
    pickle.dump(d,wr)
with open("../python/dumps.txt",'rb') as rb:
    d=pickle.load(rb)
    name=d['name']
print('name is %s'%d['name'])
'''
高阶函数 函数当成另一个函数的参数
'''
def count(a,b):
    return a+b
def getcount(a,b,fu):
    print(fu(a,b))
getcount(2,3,count)
'''
匿名函数 可以使用lambda创建
'''
rescount=lambda x,y:x+y,
print(rescount)
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
'''
偏函数 functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''
import functools
int2=functools.partial(int,base=2)
print(int2('10010'))

