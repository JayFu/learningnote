
#源自LeetCode https://leetcode.com/problems/zigzag-conversion/#/description
#将一个字符串按照排数numRows通过zigzag的方法纵向排列，
#  n=4时的走法是：

#  0      6        12

#  1   5 7    11 13

#  2 4   8 10    14

#  3      9         15 
#个人理解中间的列长度较第一列长度少2
#再从左到右依次输出

# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """

# s = 'PAYPALISHIRING'
# #OutStr = PAHNAPLSIIGYIR
# numRows = 3

s = '123456789'
OutStr = 159246837
numRows = 3

# ss = [0] * len(s)
#作为储存位置的数组，使用字典代替
OutStr = ''

import sys

# for i in numRows:
#     while(count <= len(s)):
#         OutStr.append(s[count])
#         if i == 0 or i == (numRows - 1):
#             count = count + (numRows*2-2)
#         else if pass:
#             pass 

# #发现这样处理中间行数无法准确定位
# #提出根据i值与numRows的关系处理

#         else if:
#             pass

#提出另一种方法：
#在获取数据的时候就对每个字符的位置进行计算，放入字典中。
#然后按照字典序提取

StrDict = {}

# StrDict = { ‘s[0]’ : '0' , 's[1]' : '4' }

for i in range(len(s)):

#由于并不是每列的字符数量都是numRows，采取了http://www.cnblogs.com/jiajiaxingxing/p/4537505.html 上的方法

#即将一个长列和一个短列视为一个单元，字符数量为 2 * numRows - 2
    Units = 2 * numRows - 2

    numUnits = len(s) // Units + 1
    #总单元数
    LastUnitNum = len(s) % numRows
    #最后一个单元的字符数

    m = i // Units
    n = i % Units
    #此处 i = Units * m + n
    #n代表了字符在每个小单元中的位置，对n的数值进行处理即可
    count = 0
    #作为字典key的值

    if n == 0 :
        StrDict[m] = s[i]
        print('零', StrDict)
    elif n == numRows:
        if LastUnitNum >= numRows:
            StrDict[len(s) - (numUnits - m)] = s[i - 1]
            print('i=', i, StrDict)
        else:
            StrDict[len(s) - (numUnits - m) + 1] = s[i - 1]
            print('i=', i, StrDict)
    elif n < numRows:
        for j in range(0, n - 1):
            if j <= LastUnitNum and numRows - j <= LastUnitNum - numRows :
                count += numUnits + j * 2 * numUnits
                # StrDict[numUnits + j * 2 * numUnits] = s[i]
            elif j <= LastUnitNum and numRows - j > LastUnitNum - numRows:
                count += numUnits + j * 2 * (numUnits - 1) + 1
                # StrDict[numUnits + j * 2 * (numUnits - 1) + 1] = s[i]
            else:
                count += numUnits + j * 2 * (numUnits - 1)
                # StrDict[numUnits + j * 2 * (numUnits - 1)] = s[i]
            StrDict[count] = s[i - 1]
            print('i=', i, StrDict)
    else :
        for j in range(0, numRows):
            if j <= LastUnitNum and numRows - j <= LastUnitNum - numRows :
                count += numUnits + (numRows - j) * 2 * numUnits + 1
                # StrDict[numUnits + (numRows - j) * 2 * numUnits + 1] = s[i]
            elif j <= LastUnitNum and numRows - j > LastUnitNum - numRows:
                count += numUnits + (numRows - j) * 2 * (numUnits - 1) + 2
                # StrDict[numUnits + (numRows - j) * 2 * (numUnits - 1) + 2] = s[i]
            else:
                count += numUnits + (numRows - j) * 2 * (numUnits - 1) + 1
                # StrDict[numUnits + (numRows - j) * 2 * (numUnits - 1) + 1] = s[i]
            StrDict[count] = s[i - 1]
            print('i=', i, StrDict)

    # if i == 2: sys.exit(0)
# for key in StrDict:
# 对于字典的遍历一定是按照字典下标遍历的，所以只能对一个值进行迭代

for key in range(len(s)):
    if StrDict.get(key) == None : continue
    OutStr += StrDict.get(key)

print(OutStr)
# return OutStr