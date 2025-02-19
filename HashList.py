def hash31(Values,hashsize=2**20):
    h = 0
    i = 0
    while i<len(Values):
        h = Values[i] + 31*h
        h = h % hashsize
        #Set h equal to the remainder of h divided by the hashsize.
        i = i + 1
    return h

def HashList(InputArray):
    OutputArray = []
    for i in range(len(InputArray)):
        # Converting each string to a list of ASCII values
        ascii_values = [ord(char) for char in InputArray[i]]
        # Passing the list of ASCII values to hash31
        temp = hash31(ascii_values)
        OutputArray.append(temp)
    return OutputArray
