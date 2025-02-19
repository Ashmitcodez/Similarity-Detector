def FindMatchIndices(Array1,Array2):
    Output = []
    for i in range(len(Array1)):
        for j in range(len(Array2)):
            if Array1[i] == Array2[j]:
                Output.append(i)
    return Output
