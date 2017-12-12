# LeetCode上的一道简单题
# 要求输入一个整数把它反过来输出
# 很快通过了，没有坑，直接贴代码

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        Output = ''
        Input = str(x)
        i = 1
        if(Input[0] == '-'): 
            Output += Input[0]
        while i is not len(Input)+1:
            Output += Input[-i]
            i += 1
        if(Input[0] == '-'):
            Output = Output[:-1]
        if (int(Output) <= -2147483648 ) or (int(Output) >= 2147483648) : return 0
        return int(Output)
        
        