def RightMin(Values):
    Index = 0 
    for i in range(len(Values)):
        MinVal = min(Values)
        if MinVal == Values[i]:
            Index = i

    return (MinVal,Index)

MinVal, Index = RightMin([3,1,-2,4,-2])
print(MinVal)
print(Index)