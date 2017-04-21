#n（n<=20）个人逆时针站成一圈，两个官员，A从1号逆时针数k个停下，B从n号顺时针数m个停下
#他们数的下一个人选出来
#输入n, m, k，输出选出来的人
#输入示例：10 4 3
#输出示例：4 8,9 5,3 1,2 6,10,7

#初始化输入
OringinInput = input()
OutputList = ''
#处理输入内的空格，查找到split函数和strip
#split()用于移除字符串头尾指定的字符。参数为指定的字符串，默认空格
#str.strip([chars])
#strip()函数可以根据一个分隔符将字符串切片。参数为分割符（默认空格）和分割次数指定值（默认无限制）
#str.split(str="", num=string.count(str))
#本题中，要从输入字符串中得到三个数字，使用strip()函数更好
ListStrip = OringinInput.split()
n = int(ListStrip[0])
m = int(ListStrip[1])
k = int(ListStrip[2])


CircleList = list(range(1,n+1))
#查找到zip函数，可以把两个list合并为一个dict。
#本题中意义不大且造成计算步长繁琐，熟悉dict用法
#CircleList = dict(zip(list(range(n)),list(range(1,n+1))))
#第n个人下标为n-1
#每次官员A选出下标为m+1的人，官员B选出下标为-k+1的人，之后各自自加m、k，进入下次循环

while(len(CircleList)>0):
    
#保证数据不越界
#进入死循环    while(m+1 > len(CircleList)):m - len(CircleList)
#    while(k+1 > len(CircleList)):k - len(CircleList)
    while(m > len(CircleList)):m - len(CircleList)
    while(k > len(CircleList)):k - len(CircleList)

    if (len(CircleList)==1): OutputList += CircleList
#判断是否选中同一人
    if(CircleList[m + 1]==CircleList[-(k + 1)]):
#print函数会加入换行，使用字符串
#        print(CircleList[m + 1], ',')
        OutputList += (CircleList[m+1]+',')
        CircleList.pop(m + 1)

    else: 
#        print(CircleList[m + 1], CircleList[-(k + 1)],',')
        OutputList += (CircleList[m+1]+CircleList[-(k+1)+'+'])
        CircleList.pop(m + 1)
        CircleList.pop(-(k + 1))

