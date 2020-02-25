class Values:
    pos = -1
    val = -1

    def __init__(self, pos, val):
        self.pos = pos
        self.val = val
    
def pick_peaks(arr):
    objs = []
    peaks = []
    prev_peak = -1

    for i in range (len(arr)):
        objs.append(Values(i, arr[i]))
    
    objs.sort(key=lambda x: x.val, reverse= True)

    for i in range(len(objs)):
        
        if objs[i].pos == 0 or objs[i].pos == len(arr) - 1:
            continue

        if prev_peak + 1 == objs[i].pos or prev_peak - 1 == objs[i].pos:
            # next value is peak
            continue

        if objs[i].val <= arr[objs[i].pos - 1] or objs[i].val < arr[objs[i].pos + 1]:
            # next value is greater
            continue

        if objs[i].val == arr[objs[i].pos + 1]:
            # platou detected
            cc = 1
            while objs[i].pos + cc < len(arr) - 1 and objs[i].val >= arr[objs[i].pos + cc]:
                cc += 1

            if arr[objs[i].pos + cc] > objs[i].val:
                continue

        # peak detected
        peaks.append(objs[i])
        prev_peak = objs[i].pos
    
    peaks.sort(key=lambda x: x.pos)
    
    pos = []
    val = []
    for i in range(len(peaks)):
        pos.append(peaks[i].pos)
        val.append(peaks[i].val)

    return {'pos' : pos, 'peaks' : val }