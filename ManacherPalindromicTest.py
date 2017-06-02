# -*- coding: utf-8 -*-
s = 'ababa'

import pdb

# THE_ANSWER = 42
# T = [THE_ANSWER]

# for c in s:
#     T.append(c)
#     T.append(THE_ANSWER)

# m = 0

# c, r, size = 1, 2, len(T)
# P = [0, 1] + [None] * (size-2)
# maxIndex , maxCount = 0, 1

# for i in range(2, size):
#     print(P)
#     print(i, c, m, r)
#     m = c*2 - i
#     if r > i and P[m] < r-i:
#         P[i] = P[m]
#         print('case1')
#         continue

#     count = min(i, size-i-1)
#     for n in range((1 if r <= i else r + 1 - i), count + 1):
#         if T[i+n] != T[i - n]:
#             count = n - 1
#             print('case2')
#             break

#     c = i
#     r = i + count
#     P[i] = count
#     if count > maxCount:
#         maxCount = count
#         maxIndex = i - count

# maxIndex = maxIndex // 2
# print(s[maxIndex:maxIndex+maxCount])

#预处理
s='#'+'#'.join(s)+'#'

RL=[0]*len(s)
MaxRight=0
pos=0
MaxLen=0
for i in range(len(s)):
    print(RL)
    print(i, MaxRight, RL[i], pos)
    # pdb.set_trace()
    if i<MaxRight:
        
        RL[i]=min(RL[2*pos-i], MaxRight-i)
    else:
        RL[i]=1
    #尝试扩展，注意处理边界
    while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
        RL[i]+=1
    #更新MaxRight,pos
    if RL[i]+i-1>MaxRight:
        MaxRight=RL[i]+i-1
        pos=i
#更新最长回文串的长度
    # MaxLen=max(MaxLen, RL[i])
    if RL[i] > MaxLen: 
        OutPalStr = s[i - RL[i] // 2:i + RL[i] //2] 
        print(i)
    MaxLen = max(MaxLen, RL[i])

OutPalStr = OutPalStr.replace("#", "")
print(OutPalStr)


 