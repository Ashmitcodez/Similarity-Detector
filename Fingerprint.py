def RightMin(Values):
    Index = 0 
    for i in range(len(Values)):
        MinVal = min(Values)
        if MinVal == Values[i]:
            Index = i

    return (MinVal,Index)

def Window(w,Array):
    Output = []
    if w > len(Array):
        return [Array]
    
    for i in range(len(Array) - w + 1):
        Data = Array[i:(i+w)]
        Output.append(Data)
    return Output


def Fingerprint(w, Array):
    """
    Computes the fingerprint of the input sequence using the winnowing algorithm.
    """
    Windows = Window(w, Array)
    FingerprintValues = []
    FingerprintPositions = []
    
    i = 0
    while i < len(Windows):
        Win = Windows[i]
        MinVal, RelPos = RightMin(Win)
        AbsPos = i + RelPos  # Convert relative position to absolute
        
        # Ensure unique positions are stored
        if AbsPos not in FingerprintPositions:
            FingerprintValues.append(MinVal)
            FingerprintPositions.append(AbsPos)
        i += 1
    
    return [FingerprintValues, FingerprintPositions]

