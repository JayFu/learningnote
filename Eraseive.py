if __name__ == '__main__':
    nnn = 27
    listrange = int(nnn * 10 * 1.15)
    # numberlist = [True for i in range(int(listrange+2))]
    # listrange = 34
    numberlist = [True for i in range(listrange+2)]
    templist = [2]
    temp = 2
    for i in range(nnn - 1):
        # print(temp)
        for j in range(listrange):
            if j % temp == 0: 
                numberlist[j] = False
                # print("temp = ", temp)
        for k in range(listrange+2):
            if k == 1: continue
            if numberlist[k] == True:
                temp = k
                if temp is not 1: templist.append(temp)
                numberlist[k] = False
                break
    # for k in range(listrange):
    #     if numberlist[k] == True:
    #         temp = k
    #         if temp is not 1: templist.append(temp)
    print(templist)    
