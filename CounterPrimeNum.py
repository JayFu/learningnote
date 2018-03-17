# -*- coding: utf-8 -*-
# 题目描述
# 令Pi表示第i个素数。现任给两个正整数M <= N <= 10000，请输出PM到PN的所有素数。

# 输入描述:
# 输入在一行中给出M和N，其间以空格分隔。


# 输出描述:
# 输出从PM到PN的所有素数，每10个数字占1行，其间以空格分隔，但行末不得有多余空格。

# 输入例子:
# 5 27

# 输出例子:
# 11 13 17 19 23 29 31 37 41 43

# 47 53 59 61 67 71 73 79 83 89

# 97 101 103

# 求质数方法成为本题关键，使用筛选法求质数
# 再使用质数分布公式推算质数范围

def EraSieve(zoe):
    # x/ln x > 10000
    # x > 10000 ln x
    # ln x < 10
    # x > 100000
    # 因为以上公式并非准确值
    # 所以在此基础上增加15%以保证不逸出
    listrange = int(zoe * 10 * 1.15)
    # 求第nnn个质数的位置
    # 通过质数分布公式所得
    numberlist = [True for i in range(listrange + 2)]
    templist = [2]
    temp = 2
    for i in range(zoe - 1):
        for j in range(listrange):
            if j % temp == 0: 
                numberlist[j] = False
        for k in range(listrange):
            if k == 1: continue
            if numberlist[k] == True:
                temp = k
                if temp is not 1: templist.append(temp)
                numberlist[k] = False
                break
    return templist

def outprint(temp):
    for i in range(len(temp)):
        if i % 10 ==9 :
            print(temp[i])
        else:
            print(temp[i], end=" ")

if __name__ == '__main__':
    inputlist = input().split(" ")
    nnn = int(inputlist[1])

    outputlist = EraSieve(nnn)
    outprint(outputlist[int(inputlist[0])-1:])
        


    