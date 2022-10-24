x = "Python"  # str
x = 10  # int
x = [1,2,3,4]  # list
x = {'name':'eunbi','age':25}  # dict
x = True  # bool
print(type(x))

a = "Act as though \nit is impossible"  # 줄바꿈
a = '''Act as though
it is impossible'''
print(a)

a = '"Failure is simply again."he says."'  # 따음표(") 문자 처리
a = "\"Failure is simply again.\"he says.\""  # \"는 문자로 인식
print(a)

a = "hello python!"
len(a)
a[0]  # indexing
a[6:13]  # slicing
a[6:]  # slicing(마지막 원소까지 가져올 때)

a = "TitanicJames"
title = a[:7]
director = a[7:]
print("title: "+title+", director: "+director)

x = ['a','b',['c','d','e']]  # list
x[2][1]

x = {'key1':'value1','key2':'value2'}  # dict
x['key2']

x = set([5,2,1,1])  # set
x  # 중복제외