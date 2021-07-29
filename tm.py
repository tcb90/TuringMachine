def main():
    tm = open("tm.txt", "r")
    tape = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in tm]
    output = open("output.txt", "w+")
    # Line 1: states of TM
    # Line 2: input alphabet
    # Line 3: tape alphabet ('_' represents blank space)
    # Line 4: starting state of TM
    # Line 5: transition rules where ->
    # (in state a, read b on tape, write c to current, move to d, move head to e)
    states = lines[0].split(",")
    inputAlphabet = lines[1].split(",")
    tapeAlphabet = lines[2].split(",")
    startingState = lines[3]
    currentState = startingState
    tran = lines[4:]

    i = 0
    while i < len(tran):
        tran[i] = tran[i].split(",")
        i = i + 1

    for line in tape:
        currentState = startingState
        startTape = ['_', '_', '_', '_', '_']
        insTape = []
        for pos in line.strip('\n'):
            insTape.append(pos)
        usingTape = startTape + insTape + startTape
        i = 5
        p = 0
        while currentState != 'accept' and currentState != 'reject':
            if currentState == tran[p][0] and usingTape[i] == tran[p][1]:
                usingTape[i] = tran[p][2]
                currentState = tran[p][3]
                if tran[p][4] == 'L':
                    i -= 1
                elif tran[p][4] == 'R':
                    i += 1
                p = 0
            else:
                p += 1
            if i > len(usingTape):
                currentState = "reject"
            if p >= len(tran):
                currentState = "reject"
        if currentState == "accept":
            output.write("accept\n")
        elif currentState == "reject":
            output.write("reject\n")

    tm.close()
    tape.close()
    output.close()


if __name__ == "__main__":
    main()

