#输入一个只包含AGCT的长度为n（n<=100）的DNA串，输出字典序最小的表示
#样例输入： CTCC CGAGTCAGCT
#样例输出： CCCT AGCTCGAGTC

#输入，保存在列表中
OriginDNAList = list(input())
#防止越界
if (len(OriginDNAList) > 100 ):
    print('error')
##将ACGT分别定义为1、2、3、4，每向后一位
#python的特性可以比较字符串大小，不需要转换成数字，因此只需遍历一次即可
#如
#>>> m = 'ACTTTTTTTT'
#>>> n = 'GCTGTAAAAA'
#>>> n > m
#>>> True
OutputDNAList = OriginDNAList
#开始遍历