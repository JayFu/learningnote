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

inputlist = input().split(" ")

from math import log
def EraSieve(nnn):
    # x/ln x > 10000
    # x > 10000 ln x
    # lnx < 10
    # x > 100000
    listrange = nnn * 10 * 1.15
    # 求第nnn个质数的位置
    # 通过质数分布公式所得
    numberlist = [True for i in range(listrange+2)]
    templist = [2]
    temp = 2
    for i in range(2, listrange//2):
        for j in range(listrange):
            if j % temp == 0: numberlist[j] = False
        for k in range(listrange):
            if numberlist[k] == True:
                temp = k
                templist.append(temp)
    
    return templist


        


    