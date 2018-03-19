#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 大侦探福尔摩斯接到一张奇怪的字条：“我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm”。大侦探很

#  快就明白了，字条上奇怪的乱码实际上就是约会的时间“星期四 14:04”，因为前面两字符串中第1对相同的大写英文字母（大小写有区分）是

#  第4个字母'D'，代表星期四；第2对相同的字符是'E'，那是第5个英文字母，代表一天里的第14个钟头（于是一天的0点到23点由数字0到9、

#  以及大写字母A到N表示）；后面两字符串第1对相同的英文字母's'出现在第4个位置（从0开始计数）上，代表第4分钟。现给定两对字符串，

#  请帮助福尔摩斯解码得到约会的时间。

# 输入描述:
# 输入在4行中分别给出4个非空、不包含空格、且长度不超过60的字符串。


# 输出描述:
# 在一行中输出约会的时间，格式为“DAY HH:MM”，其中“DAY”是某星期的3字符缩写，即MON表示星期一，TUE表示星期二，WED表示星期三，THU表示星期

# 四，FRI表示星期五，SAT表示星期六，SUN表示星期日。题目输入保证每个测试存在唯一解。

# 输入例子:
# 3485djDkxh4hhGE

# 2984akDfkkkkggEdsb

# s&hgsfdk

# d&Hyscvnm

# 输出例子:
# THU 14:04

def outprint(temp):
    if outputlist[0] == 'A': outputlist[0] = 'MON'
    elif outputlist[0] == 'B': outputlist[0] = 'TUE'
    elif outputlist[0] == 'C': outputlist[0] = 'WED'
    elif outputlist[0] == 'D': outputlist[0] = 'THU'
    elif outputlist[0] == 'E': outputlist[0] = 'FRI'
    elif outputlist[0] == 'F': outputlist[0] = 'SAT'
    else: outputlist[0] = 'SUN'
    
    if ord(outputlist[1]) < 58:
        outputlist[1] = int(outputlist[1])
    else: outputlist[1] = ord(outputlist[1]) - 55
    
    print(outputlist[0], "{:0>2d}:{:0>2d}".format(outputlist[1], outputlist[2]))

if __name__ == '__main__':
    inputlist, outputlist = [], []
    # for i in range(4):
    #     inputlist.append(input())

    inputlist.append('3485djDkxh4hhGA')
    inputlist.append('2984akDfkkkkggAdsb')
    inputlist.append('s&hgsfdk')
    inputlist.append('d&Hyscvnm')
    
    firstlenth = min(len(inputlist[0]), len(inputlist[1]))
    secondlenth = min(len(inputlist[2]), len(inputlist[3]))

    for i in range(firstlenth):
        if inputlist[0][i] == inputlist[1][i]:
            if (ord(inputlist[0][i]) > 64) and (ord(inputlist[0][i]) < 72):
                outputlist.append(inputlist[0][i])
                tempnum = i + 1
                break
    
    for i in range(tempnum, firstlenth):
        if inputlist[0][i] == inputlist[1][i]:
            # if (ord(inputlist[0][i]) > 64) and (ord(inputlist[0][i]) < 79):
            if (ord(inputlist[0][i]) in range(65, 79)) or (int(inputlist[0][i]) in  range(10)):
                outputlist.append(inputlist[0][i])
                break

    for i in range(secondlenth):
        if inputlist[2][i] == inputlist[3][i]:
            # if ((ord(inputlist[2][i]) > 64) and (ord(inputlist[2][i]) < 91)) or ((ord(inputlist[2][i]) > 96) and (ord(inputlist[2][i]) < 123)):            
            if (ord(inputlist[2][i]) in range(65, 91)) or (ord(inputlist[2][i]) in range(97, 123)):
                outputlist.append(i)
                break
    
    outprint(outputlist)