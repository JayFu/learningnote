# 乒乓序列从1开始计数，始终向上计数或倒数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和第28个要素。

# 1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6

# 实现一个返回乒乓序列第n个元素的函数乒乓。

def pingpong(n):
    """返回乒乓序列的第n个元素
    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(10)
    4
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    mask_n, output_n = 0, 0

    for i in range(n):
        if (i % 7 == 0) or (i % 10 == 7):
            if mask_n == 0: mask_n = 1
            else: mask_n = 0
        if mask_n == 1: output_n += 1
        else: output_n -= 1
    
    return output_n

if __name__ == '__main__':
    import doctest
    doctest.testmod()