def SimilarityScore(matched_positions, k, total_length):
    """
    Calculates a similarity score by taking a list of matched positions for a string and
    determining what proportion of characters in a string matched.

    Parameters:
    matched_positions (list): List of indices corresponding to matched positions (1-based).
    k (int): Length of each match.
    total_length (int): Total length of the original string.

    Returns:
    float: The proportion of the string that matched (between 0 and 1).
    """
    matched_chars = [0] * total_length  # Track matched characters
    
    # Mark all characters covered by each match
    for pos in matched_positions:
        for i in range(pos - 1, pos - 1 + k):  # Convert to 0-based indexing
            if 0 <= i < total_length:  # Ensure within bounds
                matched_chars[i] = 1  # Mark this character as matched
    
    # Calculate the proportion of matched characters

    matched_sum = sum(matched_chars)

    if total_length > 0:
        return matched_sum / total_length
    else:
        return 0.0

