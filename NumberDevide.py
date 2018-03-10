# 系列正整数，请按要求对数字进行分类，并输出以下5个数字：

# A1 = 能被5整除的数字中所有偶数的和；

# A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；

# A3 = 被5除后余2的数字的个数；

# A4 = 被5除后余3的数字的平均数，精确到小数点后1位；

# A5 = 被5除后余4的数字中最大数字。

# 输入描述:
# 每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N，随后给出N个不超过1000的待分类的正整数。数字间以空格分隔。

# 输出描述:
# 对给定的N个正整数，按题目要求计算A1~A5并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

# 若其中某一类数字不存在，则在相应位置输出“N”。

# 输入例子:
# 13 1 2 3 4 5 6 7 8 9 10 20 16 18

# 输出例子:
# 30 11 2 9.7 9

nnn = input().split(" ")
NumberList = nnn[1:]
# OutputList = [[] for i in range(5)]
# 不使用append保存在数据中，每部直接对结果数据进行处理或者预处理。
OutputList = [0 for i in range(5)]
countfor1, countfor3 = 0, 0

for i in range(len(nnn)-1):
    temp = int(NumberList[i])
    FirstEnding = temp % 5
    # 将结果保存在OutputList中，每次保存时进行处理，
    if FirstEnding == 0:
        if temp % 2 == 0: OutputList[0] += temp
    if FirstEnding == 1: 
        if countfor1 % 2 == 0: OutputList[1] += temp
        else: OutputList[1] -= temp
        countfor1 += 1
    if FirstEnding == 2: OutputList[2] += 1
    if FirstEnding == 3: 
        OutputList[3] += temp
        countfor3 += 1
    if FirstEnding == 4:
        if temp > OutputList[4]: OutputList[4] = temp
            
    # if FistrEnding == 0: OutputList[0].append(temp)
    # elif FistrEnding == 1: A1.append(temp)
    # elif FistrEnding == 2: A2.append(temp)
    # elif FistrEnding == 3: A3.append(temp)
    # else: A4.append(temp)

if OutputList[3] is not 0: OutputList[3] = OutputList[3] / countfor3
for i in range(5):
    if OutputList[i] == 0: OutputList[i] = 'N'

# print(OutputList[0], OutputList[1], OutputList[2], '{0:.1f}'.format(OutputList[3]), OutputList[4])
if OutputList[3] is not 'N':
    print(OutputList[0], OutputList[1], OutputList[2], '{0:.1f}'.format(OutputList[3]), OutputList[4])
else:
    print(OutputList[0], OutputList[1], OutputList[2], OutputList[3], OutputList[4])
# for i in range(len(A0)):
#     if A0[i] % 2 == 0: ending0 += A0[i]

# for i in range(len(A1)):
#     if (i % 2 == 0): ending1 += A1[i]
#     else: ending1 -= A1[i]

# ending2 = len(A2)

# for i in range(len(A3)):
#     ending3 += A3[i]
# if len(A3) is not 0: ending3 = ending3/len(A3)

# ending4 = max(A4)

# for i in list[A0, A1, A2, A3, A4]:
#     if i == 0: i == 'N'

# print(ending0, ending1, ending2, '{0:.1f}'.format(ending3),ending4)