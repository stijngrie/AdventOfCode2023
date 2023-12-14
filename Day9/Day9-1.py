file1 = open('Day9/Day9-Input.txt', 'r')
Lines = file1.readlines()

answer = 0
# Build down
for line in Lines:
    firstSequence = list(line.replace("\n", "").split(" "))
    for index, num in enumerate(firstSequence):
        firstSequence[index] = int(num)
    
    sequences = []
    sequences.append(firstSequence)
    depth = 0
    allZero = False
    while not allZero:
        newSequence = []
        current = sequences[depth]
        for index, num in enumerate(current):
            if index + 1 != len(current):
                newSequence.append(current[index + 1] - current[index])
        sequences.append(newSequence)
        depth += 1
        # Check if all zero
        checkNotZero = False
        for num in newSequence:
            if num != 0:
                checkNotZero = True
        if not checkNotZero:
            allZero = True

    # Build back up
    sequences.reverse()
    first = True
    for index, sequence in enumerate(sequences):
        if first:
            sequence.append(0)
            first = False
        else:
            sequence.append(sequence[-1] + sequences[index-1][-1])
    answer += sequences[-1][-1]
print(answer)