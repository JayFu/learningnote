#输出100~999中满足ABC=A^3+B^3+C^3的三位数ABC
#list(range(100,1000))
#range函数不包含后一个数字

#循环模块
for CounterNum in range(100,1000):
#循环数据分位放入列表
#    NumList = list(str(CounterNum))
#    数据类型报错
#    NumList = list(CounterNum)
#    数据类型int无法迭代，仍使用原来方法
    NumList = list(str(CounterNum))
    TotleNum = 0
#计算列表内水仙和
    for j in NumList:
#        将j转变为int类型        
        j = int(j)
#        TotleNum += (j ^ 3)
#        次方^无法使用，改成j*j*j
        TotleNum += (j * j * j)
#判断并输出
    if TotleNum == CounterNum:
        print(TotleNum)
