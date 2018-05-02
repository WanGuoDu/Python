#coding=utf-8
import traceback
from types import MethodType
class MyClass(object):
    __slots__=['name','set_name']#限制当前类的属性，子类无限制
def set_name(self,name):
    self.name=name
cls=MyClass()
cls.name="Tom"
cls.set_name=MethodType(set_name,cls)
cls.set_name('jerry')
print(cls.name)
try:
    cls.age=30
except AttributeError:
    traceback.print_exc()
#读写检查
