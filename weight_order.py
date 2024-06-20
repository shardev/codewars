'''
******[1]******
# Your task is to generate a palindrome string, using the specified length n,
# the specified characters c(all characters in c must be used at least once),
# and the code length should less than: python 55 characters javascript 62 characters
def palindrome(n, c): 
    output = c
    for i in range(n - (2 * len(c))):
        output += c[0]
    
    output += c[::-1]
    return output

#palindrome(15, 'anvolim') | palindrome(15, 'voliman') | etc.
test_cases = [15, 25]
for test in test_cases:
    n_pal = palindrome(test, 'anvolim')
    print(n_pal)
    if test == len(n_pal) and n_pal == n_pal[::-1]:
        print("Test passed [👍]")

# length = 3, strng = ab
# Your palindrome is : abba

# length = 1, strng = a
# Your palindrome is : aa

# length = 51, strng = abcdefghijklmnopqrstuvwxyz
# Your palindrome is : abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba

#print(len('abcdefghijklmnopqrstuvwxyz'))
'''


'''
******[2]******
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
'''
def order_weight(weights):
    if len(weights) == 0:
        return ""

    sums = []
    weights = weights.split()

    for w in weights:
        current_weight_c_sum = 0
        for i in range(len(w)):
            current_weight_c_sum += int(w[i])
        
        sums.append((w, current_weight_c_sum))  
    
    sums = sorted(sums, key=lambda item: (item[1], item[0]))
    
    output = ""
    for w in sums:
        output += f'{w[0]} '
    return output.strip()


print(order_weight("56 65 56 74 100 99 68 86 180 90"))

# '11 2000 10003 22 123 1234000 44444444 9999' 
# '11 11 2000 10003 22 123 1234000 44444444 9999'