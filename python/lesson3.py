#!/usr/bin/env python
# coding=utf-8
#第三节课

#对象的比较
#a = 20
#b = 200

#值比较
##print a < b

#身份比较
#print id(a) == id(b)
#print a is b

#类型比较
#print type(a) == type(b)
#print isinstance(a,type(b))

#求商和余数
#a = 10
#b = 3
#r1,r2 = divmod(a,b)
#print r1,r2

#pi = 3.1415926
#print round(pi,2)

#import math
#print round(math.pi,4)

#条件和循环
#def Hello():
#    print 'hehe'
#Hello()

#def Func1():
#    def Func2():
#        print 'hehe'
#    Func2()
#Func1()

#def Func1():
#    def Func2():
#        print 'hehe'
#    return Func2
#a = Func1()
#a()

#def Hello(x):
#    print x
#Hello(10)

#def Add(x,y):
#    return x + y
#print(Add('hehe','haha'))

#def Hello(x=10):
#    print x
#Hello()

#def PrintPoint(x = 0,y = 0,z = 0):
#    print x,y,z
#PrintPoint()
#关键字参数
#PrintPoint(x = 100,z = 100)

#a = [9,5,2,7]
#print sorted(a)
#print sorted(a,reverse = True)

#def Cmp(x,y):
#    if abs(x) < abs(y):
#        return -1
#    elif abs(x) > abs(y):
#        return 1
#    else:
#        return 0
#a = [9,5,2,7]
#print sorted(a,cmp = Cmp)

#def Log(prefix,*data):#data  元组，表示参数组
#    #Log 打印一行日志，支持多个字段，字段和字段之间用\t来分割
#    print prefix +'\t'.join(data)
##按级别打印
##CRITICAL 致命
##ERROR 严重
##WARNING 一般
##INFO
##NOTICE
#Log("[Notice]\t",'id = 10','name = tian','score = 150')

#def Log(prefix,**data):#字典
#    print prefix + '\t'.join(data.values())
#
#Log("Notice\t",id = '10',name = 'tian',score = '150')

self = [1,2,3,4]
print self[-2]





