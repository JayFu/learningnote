#输入整数n，计算s=1!+2!……+n!的末尾六位数
#期望输入：20        40
#期望输出：820313    940313
n = input()
n = int(n)
#初始化数据

x = 0
#j = 1
#计算阶乘之和模块
for i in range(n):
    i += 1
    b = 1
    for j in range(i):
        b *= (j+1)
    x += b
#    print('x=',x)

#将阶乘之和末尾六位数字输出
m = str(x)
for j in range(6):
    j = 0 - (j + 6)
    print(m[j], end='')

#输入20时输出出现811149%
