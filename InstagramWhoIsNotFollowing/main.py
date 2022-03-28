 
with open("takip.txt") as t:
    with open("tci.txt") as f:
        tList = t.read().split("\n")
        tciList = f.read().split("\n")
        op = []

        for i in range(len(tList)):
            if tList[i] not in tciList:
                op.append("@"+tList[i])

        print("\n".join(op))
