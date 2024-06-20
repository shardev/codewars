# Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?
# ! = 2
# ? = 3
def findWeight(inputString):
    sum = 0
    for letter in inputString:
        if letter == '!':
            sum += 2
        elif letter == '?':
            sum += 3
    return sum

def balance(left, right):
    return 'Left' if findWeight(left) > findWeight(right) else 'Right' if findWeight(left) < findWeight(right) else 'Balance'

