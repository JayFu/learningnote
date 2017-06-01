
s = 'babcbabcbaccba'

THE_ANSWER = 42
T = [THE_ANSWER]

for c in s:
    T.append(c)
    T.append(THE_ANSWER)

m = 0

c, r, size = 1, 2, len(T)
P = [0, 1] + [None] * (size-2)
maxIndex , maxCount = 0, 1

for i in range(2, size):
    print(P)
    print(i, c, m, r)
    m = c*2 - i
    if r > i and P[m] < r-i:
        P[i] = P[m]
        print('case1')
        continue

    count = min(i, size-i-1)
    for n in range((1 if r <= i else r + 1 - i), count + 1):
        if T[i+n] != T[i - n]:
            count = n - 1
            print('case2')
            break

    c = i
    r = i + count
    P[i] = count
    if count > maxCount:
        maxCount = count
        maxIndex = i - count

maxIndex = maxIndex // 2

print(s[maxIndex:maxIndex+maxCount])

 