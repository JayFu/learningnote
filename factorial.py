#输入整数n，计算s=1!+2!……+n!的末尾六位数
n = input()
#初始化数据
b = 1
s = 0
#计算阶乘之和模块
for i in n:
    for j in n:
        b = b * j
        s = s + b

#将阶乘之和末尾六位数字输出
m = str(s)
for j in 6:
    j = 0 - j
    print(m[j])

