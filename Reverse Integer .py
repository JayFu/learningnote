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

        
        