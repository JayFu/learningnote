#输入整数n，计算s=1!+2!……+n!的末尾六位数
#期望输入：20        40
#期望输出：820313    940313
n = input()
n = int(n)
#初始化数据
Out=""
x = 0
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
    i = 0 - (6 - j)
#    print(m[j], end='')
#输入20时输出出现811149%
#后续调试发现输出的位数错误
#但是修正后发现使用“end=''”无法消除百分号
#改为输出字符串
    Out+=m[i]
#    Out = Out.join(m[i])
print(Out)

#join函数返回一个字符串，为iterable可迭代对象中字符串的连接。
#如果可迭代中有任何非字符串值，包括bytes对象，则会引发TypeError。
# 元素之间的分隔符是提供该方法的字符串。