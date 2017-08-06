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