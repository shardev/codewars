def longestSlideDown(pir):
    sum = 0
    index = 0
    
    for i in range(len(pir)):
        changed = False
        while(changed != True):
            mx = max(pir[i])
            index2 = pir[i].index(mx)

            if index2 - 1 == index or index2 + 1 == index or i == 0:
                sum += mx
                changed = True
                index = index2
            else:
                pir[i][index2] = -99999
    return sum