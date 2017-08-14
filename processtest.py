#__main__
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)... ' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')



#探究4中生成方式的用时
# N = 10000

# import time

# def list1(n):
#     start = time.time()
#     lst = []
#     for i in range(n * N):
#         lst = lst + [i]
#     end = time.time()
#     print('runs %0.6f seconds.' % (end - start))

# def list2(n):
#     start = time.time()
#     lst = []
#     for i in range(n * N):
#         lst.append(i)
#     end = time.time()
#     print('runs %0.6f seconds.' % (end - start))

# def list3(n):
#     start = time.time()
#     lst = [i for i in range(n * N)]
#     end = time.time()
#     print('runs %0.6f seconds.' % (end - start))

# def list4(n):
#     start = time.time()
#     lst = list(range(n * N))
#     end = time.time()
#     print('runs %0.6f seconds.' % (end - start))

# if __name__ == '__main__':
#     m = 30
#     # print(list1(m),list2(m),list3(m),list4(m))
#     # list2
#     # list3
#     # list4
#     # list1(m)
#     list2(m)
#     list3(m)
#     list4(m)



#最大公约数函数
# def gcd(m , n ):
#     if n == 0: m, n = n, m
#     i = 0
#     while m != 0:
#         m, n = n % m, m
#         print(m , n)
#         # i += 1
#     print(n)
#     return n

# g = gcd(650, 475)
# print(650 // g, 475 // g)



#datetime.date()的用法，传入参数
# import datetime
# # birthday = input()
# # 这个函数要求实参为一个数组，实际操作中，需要对输入进行处理
# # birthday = [2014,2,23] #可行
# # birth = datetime.date(*birthday)
# # birthday = (2013, 2, 23) #可行
# # birthday = 2014.2.2 #不可行
# # birthday = '2014, 2, 22' # 不可行
# # birthday = (2012,2,11,2)    #不可行
# # birthday = {'1' : 2012, '2': 4, '3': 12}    #不可行
# # birthday = set([1994, 2, 23])   #可行
# birth = datetime.date(*birthday)
# print(birth)



#format格式化用法
# >>> "1{:04}{:05}".format(year,8)
# '12014120200008'
# >>> "1{:04}{:04}".format(year,8)
# '1201412020008'
# >>> "1{:03}{:04}".format(year,8)
# '1201412020008'
# >>> "1{:01}{:04}".format(year,8)
# '1201412020008'
# >>> "1{:09}{:04}".format(year,8)
# '10201412020008'
# >>> m = 2011
# >>> "1{:09}{:02}".format(year,m)
# '10201412022011'



#单链表的实现
# class LNode:
#     def __init__(self, elem, next_=None):
#         self.elem = elem
#         self.next = next_
#简单的表结点类

# llist1 = LNode(1)
# p = llist1
# for i in range(2,11):
#     p.next = LNode(i)
#     p = p.next
# #p = p.next 是遍历的基础方法

# p = llist1
# while p is not None:
#     # print(p.elem) 遍历内容中的基础操作，以输出作为例子
#     pass
#     p = p.next
# p = llist1
# if p.next = None: return print("List is void")
# #判空

# p = llist1
# q = LNode(13)
# q.next = p
# p = q
# #首端插入

# p = llist1
# for i in range(2,11):
#     p.next = LNode(i)
#     p = p.next
# q = LNode(13)
# while p.next is not None:
#     if p.elem = 5:
#         q.next = p.next
#         p.next = q
#     else: p = p.next
# #中间插入

# head = head.next
# xxx.next = xxx.next.next
# #首端、中间删除

# def a(b):
    # pass
# b = LNode(123)
# if a(b.elem):
#     print('11')



# #单链表的类实现
# class LList:
#     def __init__(self):
#         self._head = None
#     #构造函数
    
#     def is_empty(self):
#         return self._head is None
#     #判断链表是否为空

#     def prepend(self, elem):
#         self._head = LNode(elem, self._head)
#     #在链表头上添加结点

#     def pop(self):
#         if self._head is None: raise LinkedListUnderflow("in pop")
#         e = self._head.elem
#         self._head = self._head.next
#         return e
#     #从头结点删除并（取出）结点元素

#     def append(self, elem):
#         if self._head is None: 
#             self._head = LNode(elem)
#             return
#         p = self._head
#         while p.next is not None: p = p.next
#         p.next = LNode(elem)
#     #在链表末端添加结点

#     def pop_last(self):
#         if self._head is None: raise LinkedListUnderflow("in pop_last")
#         p = self._head
#         if p.next is None:
#             e = p.elem
#             self._head = None
#             return e
#         while p.next.next is not None: p = p.next
#         e = p.next.elem
#         p.next = None
#         return e
#     #在链表末端删除（取出）结点

#     def find(self, a_filter_function):
#         p = self._head
#         while p is not None: if a_filter_function(p.elem): return p.elem
#         p = p.next
#     # 查找符合a_filter_function的结点，并返回该结点元素
#     #实际上，该函数仅能返回一个符合条件的结点元素，利用一个迭代器得到一个筛选生成器，如下
#     def find_filer(self, a_filter_function):
#         p = self._head
#         while p is not None:
#             if a_filter_function(p.elem): yield p.elem
#             p = p.next

#     #同样的，利用定义一个生成器，为该对象定义一个迭代器
#     def elements(self):
#         p = self._head
#         while p is not None:
#             yield p.elem
#             p = p.next
#     #使用案例：
#     # for x in list1.elements(): print(x)



#http://blog.csdn.net/gzxcyy/article/details/8694212
#在该网站中看见字符串连接使用加号“+”则会进行多次申请内存和拷贝，而join只会进行一次
#由于目前掌握无法验证，暂时存疑
