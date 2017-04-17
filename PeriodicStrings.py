#如果一个字符串可以有某个长度为k的字符串重复多次得到，则称该串以k为周期
#输入一个不超过80的字符串，输出其最小周期
#输入案例：abcabcabc
#输出案例：abc

#输入hujikolp 输出hujikolp
#输入0 输出0
#输入hujikolphujikolphujiko 输出hujikolphujikolphujiko
#输入baozi baozi baozi baozi baozi 输出baozi (有空格)
#本题中，没有提到关于空格、标点等的处理。在之后学习中掌握了相关处理之后可以加上相关判断
#输入空格 输出空格

import sys

#设置输入并初始化参数
OriginList = input()
k = 0
OutputList = ''

#判断输入是否越界
#理论上不会越界，但是本题中要求字符串长度80以内，因此加入判断
if len(OriginList) > 80:
    print('error')
    sys.exit()

for i in OriginList:
    OutputList += i
    MutiNum = len(OriginList) // len(OutputList)

#如果长度不能被整除，必不是最小周期，跳过该次循环
    if len(OriginList) % len(OutputList) : 
        continue

#判断是否周期与每段相同
    if OriginList == OutputList * MutiNum :
#输出并终止程序
        print(OutputList)
        sys.exit()

