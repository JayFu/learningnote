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
            if not (s[i] in SubList1): SubList1.append(s[i])
            elif len(SubList1) > len(SubList2):
            SubList2 = SubList1
            SubList1 = []
            SubList1.append(s[i])
        else: SubList1 = []
        return len(SubList2)

#s = 'abcabcab'
#s = 'pwwkew'
#SubList1 = []
#SubList2 = []
#for i in range(len(s)):
#    if not (s[i] in SubList1): SubList1.append(s[i])
#    elif len(SubList1) > len(SubList2):
#        SubList2 = SubList1
 #       SubList1 = []
  #      SubList1.append(s[i])
   # else:
    #    SubList1 = []
#    print(SubList1)
#    print(SubList2)
#print(len(SubList2))