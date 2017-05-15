#Given a string, find the length of the longest substring without repeating characters.
#需要注意的是，需要输出的是子字符串的长度，而不是子字符集
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        SubList1 = []
        SubList2 = []
        for i in range(len(s)):
            if not (s[i] in SubList1): 
                SubList1.append(s[i])
            else:
                while(s[i] in SubList1): 
                    SubList1.pop(0)
                SubList1.append(s[i])
            continue
            if len(SubList1)>len(SubList2):
                SubList2 = SubList1[:]
        if SubList2 == [] : SubList2 = SubList1
        return len(SubList2)


# import copy
# s = 'abcabcab'
# s = 'qwer'
# s = 'pwwkew'

# s = 'abcabcbbb'
#期望输出3

# s = 'aab'
# s = 'cbb'
# s = 'dvdf'
# SubList1 = []
# SubList2 = []
# for i in range(len(s)):
#     if not(s[i] in SubList1):
#         SubList1.append(s[i])
#     else:
#         while(s[i] in SubList1): 
#             SubList1.pop(0)
#         SubList1.append(s[i])
#         continue
#     if len(SubList1)>len(SubList2):
#         # SubList2 = SubList1
#        #等号是深复制，这里应该使用copy
#        SubList2 = SubList1.copy()
        #LeetCode网站使用的是python2，此时应使用
        #SubList2 = SubList[:]
# if SubList2 == []: SubList2 = SubList1
# print(len(SubList2))