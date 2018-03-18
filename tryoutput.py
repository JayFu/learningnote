def outprint(temp):
    for i in range(len(temp)):
        if i % 10 ==9 :
            print(temp[i])
        elif i == len(temp):
            print(temp[i])
        else:
            print(temp[i], end=" ")

if __name__ == '__main__':
    tttm = list(range(40))
    outprint(tttm)