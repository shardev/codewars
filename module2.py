def same(array1, array2):
    out = []
    if len(array1) != len(array2) or len(array1) == 0 or len(array2) == 0:  
        return False

    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            if array1[i]*array1[i] == array2[j]:
                out.append([array1[i], array2[j]])
                array2.pop(j)
                break

    if len(out) == len(array1):
        return True
    else:
        return False

