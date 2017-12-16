# -*- coding: utf-8 -*-
# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# 这是LeetCode上的一道题目
# 需要考虑到的是得出的子集中能否有重复，在已经提出的问题中只说明了不能有重复的子集
# 可以在每个得出的子集中判定
# 但是目前的思路只有多次遍历，时间复杂度会很高

# 借鉴了http://wuchong.me/blog/2014/07/28/permutation-and-combination-realize/ 给出的全组合算法
# 使用一个数再将其转化为二进制数取第二位后
# 转化后的二进制数以字符串的形式存在
# 总共可能存在的数的数量为2^n-1

# >>> a = 123
# >>> b = bin(a)
# >>> b
# '0b1111011'
# >>> c = str(b)
# >>> c[2:]
# '1111011'
# >>> b += 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: cannot concatenate 'str' and 'int' objects
# >>> d = b [2:]
# >>> d
# '1111011'
# >>> b[1]
# 'b'

# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """

def Subsets(nums):
    """
    """
    zed = len(nums)
    teemo = 2 ** zed - 1                #使二进制标记数和总长度位数相同
    cait = []                           #输出
    for i in range(teemo):
        
        zoe = []

        ryze = bin(i)[2:]
        if len(ryze) < zed:
            tresh = ''
            for m in range(zed - len(ryze)):
                tresh += '0'
            ryze = tresh + ryze
            # print(ryze)
        
        for j in range(len(ryze)):
            if ryze[j] == '1':
                print(nums[j])
                zoe.append(nums[j])
            # print(zoe)
        
        if zoe not in cait: cait.append(zoe)
        # print(i, zoe, cait)
    
    cait.append(nums)
    return cait
            
if __name__ == '__main__':
    a = [1, 2, 3]
    print(Subsets(a))

# 后记：
# 观察其他人代码发现自己的代码非常冗余，下次尝试重构改进