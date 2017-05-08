#输入整数阵列和目标，输出可以相加得到目标的两个数字的下标
#输入nums = [2, 7, 11, 15],target = 9
##因为num[0]+num[1]=2+7=9
#输出[0, 1]
class Solution(object):
    def twoSum(self, nums, target):
        outputlist = ''
        for i in range(len(nums)):
            for j in range(i, len(nums)):
#                if nums[i]+nums[j]==target: print([i, j])
#该题为LeetCode上算法题，测试该网站代码以return作为答案标准，不能使用print
#                if nums[i]+nums[j]==target: return [i, j]
#测试解答发现期望解只有一个，但是不能使用同一个元素
                if nums[i]+nums[j]==target: 
                    if i == j: continue
                    return [i, j]

#在LeetCode上解答的第一个算法题，运行时间为5102ms，击败了5.35%的提交者
