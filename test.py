def decode(message_file):
    i = 0
    counterDict = {}
    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.strip().split(' ', 1)
            counterDict[int(number)] = word
            i += 1

    toAdd = []
    limitNum, stepSize = 1, 2
    while limitNum <= i:
        toAdd.append(limitNum)
        limitNum += stepSize
        stepSize += 1

    filteredCounterDict = [(key, value) for key, value in counterDict.items() if key in toAdd]
    sortedFilteredCounterDict = dict(sorted(filteredCounterDict, key=lambda x: x[0]))
    print(sortedFilteredCounterDict)
    return ' '.join(sortedFilteredCounterDict.values())

print(decode('coding_qual_input.txt'))