#递归实现阶乘

def F_Muti(a):
    if a == 1:
        return 1
    else:
        return a * F_Muti(a - 1)

n = int(input())
n = F_Muti(n)
print(n)
