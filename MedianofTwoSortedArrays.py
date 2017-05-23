# -*- coding: utf-8 -*-

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        outputnums = []
        num2 = 0
        
        if (m + n) % 2 == 0:
            num2 = (m + n) // 2
            num1 = num2 - 1
        else:
            num1 = (m + n) // 2
        
        a = 0
        b = 0
        
        for i in range(0 , ((m + n) // 2 + 1)):
            if a >= m:
                outputnums.append(nums2[b])
                b += 1
            elif b >= n:
                outputnums.append(nums1[a])
                a += 1
            elif nums1[a] > nums2[b]:
                outputnums.append(nums2[b])
                b += 1
            else:
                outputnums.append(nums1[a])
                a += 1
        
        if num2 == 0: return outputnums[num1]
        else : return (float(outputnums[num1] + outputnums[num2])) / 2
        
# nums1 = [1, 2]
# nums2 = [3, 4]

# nums1 = [1]
# nums2 = [2,3,4,5,6]

# nums1 = [1,2,4]
# nums2 = [2,3,4,7]



# m = len(nums1)
# n = len(nums2)

# outputnums = []
# num2 = 0

# if (m + n) % 2 == 0: 
#     num2 = (m + n) // 2
#     num1 = num2 - 1
# else: 
#     num1 = (m + n) // 2

# a = 0
# b = 0

# for i in range(0, ((m + n ) // 2 + 1)):
#     if a >= m: 
#         outputnums.append(nums2[b])
#         b += 1
#         # continue        
#     elif b >= n: 
#         outputnums.append(nums1[a])
#         a += 1
#         # continue
#     elif nums1[a] > nums2[b]: 
#         outputnums.append(nums2[b])
#         b += 1
#     else:
#         outputnums.append(nums1[a])
#         a += 1
#     print(a , b)

# if num2 == 0: print(outputnums[num1])
# #python3解法：
# # else: print((outputnums[num1] + outputnums[num2]) / 2)
# #python2解法：
# else: print((float(outputnums[num1]) + float(outputnums[num2])) / 2)




