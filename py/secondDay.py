#coding=utf-8
"""
列表list
元组tuple
字典dictionalry
集合set
"""
lists=[1,1,2,3]
for i in lists:
    print(i)
print(lists.index(1))
lists.append(7)
lists_c=lists
lists.extend(lists_c)#将list添加到另一个list
print(lists)
print(type(lists))
#set 自动去除重复的元素
s_a=set([1,3,4,5,7,9])
s_b=set([1,3,4,5,4,2,4,6,8,10])
print(s_a)
print(s_b)
#并集
print(s_a|s_b)
print(s_a.union(s_b))

#交集
print(s_a&s_b)
print(s_a.intersection(s_b))
#差集a-(a&b)
print(s_a-s_b)
print(s_a.difference(s_b))
#对称差(a|b)-(a&b)
print(s_a^s_b)
print(s_a.symmetric_difference(s_b))
#set无法根据下标访问
print(len(s_a))
for x in s_a:
    print(x)
#切片
si_li=list(range(10))
print(si_li[::-1])
repeat_li=[2]*10
print(repeat_li)
repeat_li=[i*9 for i in range(20)]
print(repeat_li)
#生成器 不会马上生成到内存中 等到使用时才去做真正的计算
square_generator=(x*x for x in range(50000))
print(type(square_generator))
for i in range(10):
    print(next(square_generator))
#迭代器
