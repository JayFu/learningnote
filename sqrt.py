


def sqrt(x):
    if x < 0:
        print('Error')
        return 0
    i = 0
    while i * i < x:
        i += 1
    
    if i * i == x: return i
    else:
        return i - 1

if __name__ == '__main__':
    temp = int(input())
    print(sqrt(temp))
