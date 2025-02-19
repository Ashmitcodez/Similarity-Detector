def hash31(Values,hashsize=2**20):
    h = 0
    i = 0
    while i<len(Values):
        h = Values[i] + 31*h
        h = h % hashsize
        #Set h equal to the remainder of h divided by the hashsize.
        i = i + 1
    return h

