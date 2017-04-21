#n（n<=20）个人逆时针站成一圈，两个官员，A从1号逆时针数k个停下，B从n号顺时针数m个停下
#他们数的下一个人选出来
#输入n, m, k，输出选出来的人
#输入示例：10 4 3
#输出示例：4 8,9 5,3 1,2 6,10,7

#

CircleList = list(range(1,n+1))
#查找到zip函数，可以把两个list合并为一个dict。
#本题中意义不大且造成计算步长繁琐，熟悉dict用法
#CircleList = dict(zip(list(range(n)),list(range(1,n+1))))
#第n个人下标为n-1
#每次官员A选出下标为m+1的人，官员B选出下标为-k+1的人，之后各自自加m、k，进入下次循环

while(len(CircleList)>0):
    
#保证数据不越界
    while(m+1 > len(CircleList)):m - len(CircleList)
    while(k+1 > len(CircleList)):k - len(CircleList)
#判断是否选中同一人
    if(CircleList[m + 1]==CircleList[-(k + 1)]):
        print(CircleList[m + 1], ',')
        CircleList.pop(m + 1)

    else: 
        print(CircleList[m + 1], ' ', CircleList[-(k + 1)], ',')
        CircleList.pop(m + 1)
        CircleList.pop(-(k + 1))

