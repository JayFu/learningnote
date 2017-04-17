#输入一个只包含AGCT的长度为n（n<=100）的DNA串，输出字典序最小的表示
#样例输入： CTCC CGAGTCAGCT
#样例输出： CCCT AGCTCGAGTC
import sys
#输入，保存在列表中
OriginDNAList = input()
#防止越界
if len(OriginDNAList) > 100:
    print('error')
    sys.exit()
#判定是否在AGCT之外
for i in OriginDNAList:
    if i != 'A' and i != 'G' and i != 'C' and i != 'T':
        print('error')
        sys.exit()
##将ACGT分别定义为1、2、3、4，每向后一位
#python的特性可以比较字符串大小，不需要转换成数字，因此只需遍历一次即可
#如
#>>> m = 'ACTTTTTTTT'
#>>> n = 'GCTGTAAAAA'
#>>> n > m
#>>> True
OutputDNAList = OriginDNAList
#开始遍历
for i in range(len(OriginDNAList)):
    ListPointer = OriginDNAList[i:len(OriginDNAList)] + OriginDNAList[:i]
    if (ListPointer < OutputDNAList):
        OutputDNAList = ListPointer

print(OutputDNAList)
