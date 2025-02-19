def FindMatchPositions(f1, f2):
    """
    Compares two fingerprints and determines the positions in each
    that contain matching hash values.

    Parameters:
    f1: A 2D list representing the first fingerprint (hash values in row 1, positions in row 2)
    f2: A 2D list representing the second fingerprint (hash values in row 1, positions in row 2)

    Returns:
    p1: A list of positions in f1 where matching hash values are found in f2
    p2: A list of positions in f2 where matching hash values are found in f1
    """

    hash1, pos1 = f1  # Extracting hash values and positions from f1
    hash2, pos2 = f2  # Extracting hash values and positions from f2

    # Initialising empty lists to store matching positions
    p1 = []
    p2 = []

    # Using a nested for loop for finding positions in f1 where the hash matches a value in f2
    for i in range(len(hash1)):  
        for j in range(len(hash2)):  
            if hash1[i] == hash2[j]:  # Compare hash values
                if pos1[i] not in p1:  # Ensure unique positions
                    p1.append(pos1[i])

    # Same process as before but this time finding positions in f2 where the hash matches a value in f1
    for j in range(len(hash2)):  
        for i in range(len(hash1)):  
            if hash2[j] == hash1[i]:  
                if pos2[j] not in p2:  
                    p2.append(pos2[j])

    return p1, p2
