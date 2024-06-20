from same_arrays import same 
from fib import fibonacci, productFib
from scrambles import scramble
from longestSlideDown import longestSlideDown
from range import solution
from peaks_ import pick_peaks

def longest_consec(strarr, k):
    out = ""
    res = []
    
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return out
    
    for i in range(0, len(strarr) - k + 1):
        lng = 0
        o = ""
        for j in range (i, i+k):
            lng += len(strarr[j])
            o += strarr[j]
        res.append([i, lng, o])

    max = 0
    for i in range(0, len(res)):
        if res[i][1] > max:
            max = res[i][1]
            maxel = res[i]

    return str(maxel[2])

if __name__ == "__main__":
    #print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
    #a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    #a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

    #print(same(a1, a2))

    #print(productFib(4895))
    #print(productFib(5895))

    #productFib(4895), [55, 89, True])
    #productFib(5895), [89, 144, False]

    #print(scramble('rkqodlw', 'world'))
    
    
    #print(longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))
    #print(longestSlideDown([
    #        [75],
    #        [95, 64],
    #        [17, 47, 82],
    #        [18, 35, 87, 10],
    #        [20,  4, 82, 47, 65],
    #        [19,  1, 23, 75,  3, 34],
    #        [88,  2, 77, 73,  7, 63, 67],
    #        [99, 65,  4, 28,  6, 16, 70, 92],
    #        [41, 41, 26, 56, 83, 40, 80, 70, 33],
    #        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    #        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    #        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    #        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    #        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    #        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    #        ]))

        #print(longestSlideDown([
        #    [75],
        #    [95, 64],
        #    [17, 47, 82],
        #    [18, 35, 87, 10]])

        #print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) 
        # '-6,-3-1,3-5,7-11,14,15,17-20'

        print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3,3,3,4,3]))