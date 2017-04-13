#开灯问题：有n盏灯，k个人，第1个人把所有灯打开，之后第k个人按动一次（打开或关闭）编号为k的倍数的灯。
#输入n和k，输出开着的灯的编号，k<=n<=1000
#输入：7 3
#输出：1 5 6 7

#初始化并输入
OriginS = input()
n = int(OriginS[0])
k = int(OriginS[-1])
OutputLast = ""
#加入CounterX帮助计算以及防止越界，但是后期仍然出现越界问题，取消

#判断
#if (k<=n & n<=1000 & k>0):
if(k<=n | n<=1000 | k>0):
#初始化列表list
    OutputOri = [ True for x in range(1,n+1)]
#    OutputOri.insert(n,False)

#    print(OutputOri)

#将list中置反
#输出有问题，数据处理不当
#    for i in range(2,k+1):
#        for j in range(CounterX):
#            CounterY = j * i
#            print(OutputOri)
#            OutputOri[CounterY] = not OutputOri[CounterY]
    for i in range(2, k+1):
        CounterX = int(n // i)
        for j in range(1,CounterX+1):
            print(i,j)
#        for j in range(CounterX):
#数据会越界，起先在初始化时加入更多数据，但是容易造成处理不当，改进为加入判断
            if ((i*j-1) > n):
                continue
            OutputOri[i*j-1] = not OutputOri[i*j-1]
#            OutputOri[i*j]= not OutputOri[i*j]
            print(OutputOri)

#按顺序输出
    for i in range(n):
        if (OutputOri[i]==True):
            j = str(i+1)
#            print(OutputOri)
            OutputLast += j
            OutputLast += ' '
    print(OutputLast)
else:
    print('error')
