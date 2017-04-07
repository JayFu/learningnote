#输入整数n，计算s=1!+2!……+n!的末尾六位数
n = input()

#计算阶乘之和模块
for i in n:
    for j in n:
        b = b * j
    s = s + b

#将阶乘之和末尾六位数字输出
m = str(s)
print(m[-6]m[-5]m[-4]m[-3]m[-2]m[-1])

