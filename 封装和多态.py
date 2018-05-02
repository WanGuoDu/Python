#coding=utf-8
#repr(param)接收参数返回字符串
def getLength(param):
    print("The length of %s is %s"%(repr(param),len(repr(param))))
getLength("dataOfTest")
getLength(7)
