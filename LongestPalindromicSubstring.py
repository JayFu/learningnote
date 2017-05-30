# -*- coding: utf-8 -*-

#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#palindromic: 回文，从中间对称的字符串

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: "cbbd"
# Output: "bb"

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
        
# s = 'babad'
# s = 'cbbd'

# s = 'a'
# 对于单个字符处理有问题

# s = 'bbbbbb'
# 对于相同字符组成的字符串处理有问题

# s = 'abb'
#此例及以上两例都可以总结为，最后一个字符没有进入循环。解决：修改了循环参数

# s = 'bba'

s = 'abcdasdfghjkldcba'
#在判断是否是回文串时，采用了判断子字符串是否存在于逆序字符串中的方法。但是在这个例子中很明显得出了错误的结果
#

OutPalStr = ''
TrapStr = ''

# for i in range(len(s)):
#     for j in range(i, len(s)+1):
#         # print(s[i:j], i, j)
#         TrapStr = s[i:j]
#         if TrapStr == (TrapStr[::-1]):
#             if len(s[i:j]) > len(OutPalStr):
#                 OutPalStr = s [i:j]
# 整个代码时间复杂度为O(n^3)，测试时出现超时问题，改用其他的方法



print(OutPalStr)
        
