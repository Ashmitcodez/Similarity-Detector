def Window(w,Array):
    Output = []
    if w > len(Array):
        return [Array]
    
    for i in range(len(Array) - w + 1):
        Data = Array[i:(i+w)]
        Output.append(Data)
    return Output

print(Window(8,[3,1,4,1,5,9,2,6,5]))
