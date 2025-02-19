# winnow.py
from StripString import StripString  # Ensure this matches the exact function name in StripString.py
from Kgram import Kgram  # Ensure this matches the function name in Kgram.py
from HashList import HashList  # Ensure this matches the function name in HashList.py
from Window import Window  # Ensure this matches the function name in Window.py
from Fingerprint import Fingerprint  # Ensure this matches the function name in Fingerprint.py

def winnow(filename, k, t):
    """
    Winnow creates a document fingerprint from the contents of a document
    using the parameters k and t, where k represents the noise threshold
    and t the guarantee threshold, for the winnowing algorithm.
    
    Arguments:
    - filename (str): The name of the file to process.
    - k (int): The noise threshold, a positive integer.
    - t (int): The guarantee threshold, a positive integer such that t >= k.
    
    Returns:
    - tuple: A tuple (fp, filelength), where:
        - fp (list): The document fingerprint as a list of integers.
        - filelength (int): The length of the stripped document (whitespace removed).
    """
    
    # Calculate the window size, based on the values of t (guarantee threshold) and k (noise threshold)
    w = t - k + 1
    
    # Read the contents of the document (file) into a string
    with open(filename, 'r') as f:
        s = f.read()
    
    # Strip out unnecessary characters (e.g. whitespace), also convert to lowercase
    s = StripString(s)
    filelength = len(s)
    
    # Create k-grams from the string
    kgrams = Kgram(k, s)
    
    # Find the hash values for all k-grams
    hashes = HashList(kgrams)
    
    # Use a window of size w to generate a sequence of windows from the hashes
    windows = Window(w, hashes)
    
    # Create the fingerprint by selecting the rightmost minimum from each window
    # along with its position. Each value/position combination is added to the fingerprint only once.
    fp = Fingerprint(w,windows)
    
    return fp, filelength
