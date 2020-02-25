def longest_consec(strarr, k):
    out = ""
        res = []
    
        if len(strarr) == 0 or k > len(strarr) or k <= 0:
            return out
    
        for i in range(0, len(strarr)):
            lng = 0
            for j in range (i, i+k):
                lng += len(strarr[j])
            
            res.append([i, lng])
