def solution(args):
    cc = 1
    out =  ""
    j = 0

    for i in range(len(args)):
        if i != j: continue

        while len(args) > i + cc and args[i] == args[i+cc] - cc:
            cc += 1
        
        j = i + 1 
        if cc < 3:
            out += str(args[i]) + ","
        else :
            out += str(args[i]) + "-" + str(args[i+cc-1]) + ","
            j += cc - 1
        
        cc = 1
    
    return out[:-1]
