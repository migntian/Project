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


#第四节课

#Python序列和字典
#字符串用字典序比较大小
#a = [1,2,3]
#b = [2,1,3]
#print id(a),id(b)
#两个序列，里面的值和顺序都一样才等于

#判断一个元素在不在里面
#a = [1,2,3]
#print 1 in a

#连接操作符
#拼接通过+生成新的对象
#a = 'hello'
#b = 'world'
#print a+b

#重复操作符'-',生成新对象
#a = '-'
#print a *20

#a = [1,2,3]
#print a*3

#序列的切片操作
#a = [1,2,3,4]
#print a[3]
#print a[-1]

#a = [1,2,3,4]
#print a[1:3]
#print a[:3]

#a = [1,2,3,4,5]
##每隔一个元素取一个元素
#print a[::2]

#将一个字符串进行翻转
#'abcdef'->'fedcba'
#常规解法：两个指针

#Python牛逼解法
#a = 'abcde'
#print a[::-1]

#序列内建函数
#len
#max
#min
#sorted  生成新的对象,元组也是支持的
#sum 加的时候相同类型
#enumerate

#def Find(input_list,x):
#    for i in range(len(input_list)):
#        if input_list[i] == x:
#            return i
#    return None
#
#def Find(input_list,x):
#    for i,item in enumerate(input_list):
#        if item == x:
#            return i
#    return None

#x = [1,2,3]
#y = [4,5,6]
#z = [7,8,9]
##矩阵转置
#print zip(x,y,z)

#新对象
#a = '1234'
#print 'x'+a[1:]

#一些只适用于字符串的操作
#    %格式化替换
#x,y = 10,20
#print 'x = %d,y = %d' %(x,y)

#在字符串前面加r 就不会转义

#字符串合并
#a = ['aa','bb','cc']
#print '\n'.join(a)
#print ' '.join(a)

#字符串切分
#a = 'aa bb cc'
#print a.split(' ')

#去除字符串开头和结尾的空白符（空格，回车，换行，水平制表符,垂直制表符）
#a = '               hello'
#print a.strip()

#a = 'hello '
#print '[%s]' % a.ljust(30)
#print '[%s]' % a.rjust(30)
#print '[%s]' % a.center(30)

#查找子串
#a = 'hello world'
#print a.find('world')

#字符串替换
#a = 'hello world'
#print a.replace('world','python')

#判定字符串是否是纯字母/数字
#a = 'helloworld'
#print a.isalpha()

#b = '1234'
#print b.isdigit()

#字符串转换大小写
#a = 'hello world'
#print a.upper()

#加元素
#a = [1,2]
#a.append(3)
#print a

#删除元素
#a = [1,2,3]
##del a[0]
##print a
#a.remove(2)
#print a

#reverse 改变了原有的
#a = [1,2]
#print a[::-1]
#print a.reverse()

#基于列表的堆栈
#基于列表的队列

#元组
#内容都是只读的

#元组里面的ID是不能变的
#但是元组中某个元素时可变对象的时候（比如列表或字典），那么仍然是可以变得
#a = ([1,2],[3,4])
#a[0][0] =100
#print a
#
#a = (1,2)
#a[0] = 100

#字典
#key 必须是可hash 的  值没有规定


#第五节课
#垃圾回收虽然会自动关闭，但是良好的习惯，手动关闭,防止文件描述符泄漏
#f = open("test.py",'w')
#for line in f:
#    print line,
#f.close

#lines = f.readlines()
#for line in lines:
#    print line,
#f.close

#f.writelines(['hello bat\n','nihao\n','jiayou\n'])
#f.close


#with语句和上下文管理器
#避免忘记关闭文件描述符

#with open('./test.py') as f:
#    print f.readlines()


#文件系统相关操作
#import os.path
#
#mypath = '/home/tian/day01/python/test.txt'
#print os.path.basename(mypath)
#print os.path.dirname(mypath)
#print os.path.split(mypath)
#print os.path.splitext(mypath)


#dirnames 当前操作的位置
#import os
#mypath = '/home/tian/day01/python/'
#for basedir,dirnames,filenames in os.walk(mypath):
#    print'basedir:',basedir
#    print'dirnames:',dirnames
#    print'filenames:',filenames




#import os
#import os.path
#mypath = '/home/tian/day01/python/'
#for basedir,dirnames,filenames in os.walk(mypath):
#    for filename in filenames:
#        print os.path.join(basedir,filename)

#简易ls
#import os 
#import sys
#if len(sys.argv) < 2:
#    path = '.'
#else:
#    path = sys.argv[1]
#for f in os.listdir(path):
#    print f
#
#默认，忽略，自定义
#try:
#    a = [1,2,3]
#    print a[100]
##except IndexError as e:
#except Exception as e:
#    print e
#    print type(e)
#    #except 语句需要知道当前处理异常是那种类型
#    #可以把所有异常都写出来
#    #变量名e表示前面抛出的异常对象的引用
#    #pass
#finally:
#    print 'hehe'
#
##else 可以跟if，while/for，except搭配
##异常机制，C++不推荐，运行时增加开销


#def Divide(x,y):
#    if y == 0:
#        raise Exception('Divide  Zero')
#    return x/y
#Divide(1,0)
#print a


while True:
    print 'hehe'

















