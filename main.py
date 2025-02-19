# main.py
from Winnow import winnow
from FindMatchPositions import FindMatchPositions  
from Fingerprint import Fingerprint  
from hash31 import hash31  
from RightMin import RightMin  
from HashList import HashList  
from Kgram import Kgram  
from StripString import StripString  
from Window import Window  
from SimilarityScore import SimilarityScore  
import os

# Function to get the list of files in a directory
def get_files_in_directory(directory):
    # Get all files from the directory, ignoring subdirectories
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

# Function to compare files (this will use the `find_match_positions` and `similarity_score` functions)
def compare_files(fingerprints, files, k, s):
    matches = []
    nf = len(files)
    for i in range(nf):
        for j in range(i + 1, nf):
            fp1 = fingerprints[i]
            fp2 = fingerprints[j]

            # Find matching positions (returns two lists: matchpos1, matchpos2)
            matchpos1, matchpos2 = FindMatchPositions(fp1, fp2)  
            
            # Get the file lengths (for similarity calculation)
            s1length = len(fp1)  # Use actual length of the fingerprint list
            s2length = len(fp2)

            # Calculate similarity scores (in percentage) for both lists of positions
            sim1 = SimilarityScore(matchpos1, k, s1length) * 100  # Correct function call
            sim2 = SimilarityScore(matchpos2, k, s2length) * 100  # Correct function call

            # Check if similarity meets the threshold and store results
            max_similarity = max(sim1, sim2)
            if max_similarity > s:
                matches.append((files[i], files[j], sim1, sim2))

    return matches

# Function to display the match results
def print_results(matches):
    print('\nMatches found:')
    for match in matches:
        print(f'{match[0]:<30} ({match[2]:.1f}%)   {match[1]:<30} ({match[3]:.1f}%)')

def main():
    # Step 1: Get user input for the directory, thresholds, etc.
    directory = input('Enter the directory (or press Enter for current directory): ')
    if not directory:
        directory = '.'  # Default to current directory if empty

    k = int(input('Enter the noise threshold k: '))
    t = int(input('Enter the guarantee threshold t (where t >= k): '))
    s = float(input('Enter the similarity threshold s (e.g., 80 for 80%): '))

    # Step 2: Get files from the specified directory
    files = get_files_in_directory(directory)

    # Step 3: Generate fingerprints for all files using the winnow function
    fingerprints = []
    for filename in files:
        fp, file_length = winnow(filename, k, t)  # Assuming winnow returns fingerprint and file length
        fingerprints.append(fp)

    # Step 4: Compare files to find matches
    matches = compare_files(fingerprints, files, k, s)

    # Step 5: Print the results
    print_results(matches)

if __name__ == '__main__':
    main()
