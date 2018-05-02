#coding=UTF-8
#import string
#字符串的处理
s='abc'
print(s[0])
s=' abc '
print(s)
#s[0]='d' string类型不支持修改 实际返回新的字符串
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.strip()+'das'+s.strip())
print(s.strip(),'das',s.strip())
s='ads'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())#首字母大写
str_A='abcdefg'
str_B='adsdsaas'
print(str_A.index('def'))
try:
    print(str_B.index('def'))
except ValueError:
    print("str_B Not Contains 'def'")
#字符串可以直接大于小于等于去比较
print('a'>'b')
str_T="""abc
def
ghj
klz"""
str_sp=str_T.split('\n')
print(str_sp)
print(str_T.splitlines())
strsp_join=','.join(str_sp)
print(strsp_join)
print(strsp_join.startswith('abc'))
print(strsp_join.endswith('klz'))
print('123'.isalnum())#字母或数字
print('abcd'.isalpha())#只有字符
print('123'.isdigit())#只有数字
print(' '.isspace())
print('addd122'.islower())

#类型转换
print(str(5))
print(str(5.26))
print(int('6'))
print(float('6.36'))
try:
    print(int('6.26'))
except ValueError:
    print("浮点字符串转int不会自动把浮点转int")
#进制转换
print(int('777',8))
#字符串转数组
l="abcdefg"
arry=list(l)
print(arry)
print(' I love china! '[::-1])

#None判断
x=None
if x is None:
    print("x is None")
else:
    print("x")
#for
for i in range(0,20,2):
    print(i)
#命名关键字参数 *后面的参数需要带上名字
def func(a,b,c,*,china,uk):
    print(china,uk)
func(1,2,3,china=5,uk=7)
def funcT(a,b,c=2,*args,**kvs):
    print(a,b,c)
    print(args)
    print(kvs)
funcT(1,2)
funcT(1,2,3)
funcT(1,2,3,'a','b')
funcT(1,2,3,'a','b',name='zhangsan',age=18)
funcT(1,2,3,*('a','b'),**{'name':'zhangsan','age':18})
#斐波那契数列fn=fn-1+fn-2
def fibona(n):
    if n>1:
        return fibona(n-1)+fibona(n-2)
    elif n==1:
        return n
    else:
        return 0
for index in range(0,20,1):
    print(fibona(index))
#汉诺塔
#函数可以作为参数
def sum(x,y,p=None):
    s=x+y
    if p:
        p(s)
    return s
sum(3,2,print)
#实现自定义比较函数 冒泡排序
print("冒泡排序")
arry_Demo=[12,3,56,8,45,48,6,56,34,89,567,894,55,658,745,312,485]
for i in range(0,len(arry_Demo),1):
    for j in range(i+1,len(arry_Demo),1):
        if arry_Demo[i]>arry_Demo[j]:
            arry_Demo[i],arry_Demo[j]=arry_Demo[j],arry_Demo[i]
for resValue in arry_Demo:
    print(resValue)























