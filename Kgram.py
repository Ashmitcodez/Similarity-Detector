def Kgram(k,String):
    Output_Array = []
    for i in range(len(String)-k+1):
        str = String[i:i+k]
        Output_Array.append(str)

    if k > len(String):
        Output_Array.append(String)
    return Output_Array
