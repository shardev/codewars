#Complete the function scramble(str1, str2)
# that returns true if a portion of str1 characters 
# can be rearranged to match str2, otherwise returns false.

def scramble(s1, s2):
    for letter in s2:
        if letter in s1:
            i = s1.find(letter)
            if i == len(s1) -1: s1 = s1[:i] + '' 
            else : s1 = s1[:i] + '' + s1[i+1:]
        else: return False
    return True