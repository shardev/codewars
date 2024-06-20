def parse(data):
    curr = 0
    outList = []
    for el in data:
        if el == 'i':
            curr += 1
        elif el == 'd':
            curr -= 1
        elif el == 's':
            curr = curr ** 2
        elif el == 'o':
            outList.append(curr)
    
    return outList

print(parse("iiisdoso"))