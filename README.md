# Catch the Cheaters

**Catch the Cheaters** is a Python-based document fingerprinting and similarity detection tool designed to identify plagiarism or substantial similarities between documents. The project implements the [winnowing algorithm](https://en.wikipedia.org/wiki/Winnowing_algorithm) — a lightweight, efficient method for document fingerprinting that guarantees detection of common substrings above a specified threshold.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [License](#license)

## Overview

The goal of this project is to help educators and administrators detect potential plagiarism by comparing student submissions using document fingerprints. The system processes text by:
1. **Stripping irrelevant characters:** Converts text to lowercase and removes whitespace.
2. **Generating k-grams:** Breaks text into substrings of length `k`.
3. **Hashing k-grams:** Uses a polynomial rolling hash (the `hash31` function) to convert k-grams to integers.
4. **Windowing and Fingerprinting:** Creates sliding windows over the hash values and selects the rightmost minimum hash from each window to form the document’s fingerprint.
5. **Comparing Fingerprints:** Uses matching fingerprint positions and a similarity scoring function to detect significant overlap between documents.

This implementation was ported from MATLAB to Python while preserving the original algorithm’s integrity and behavior.

## Features

- **Document Fingerprinting:** Uses the winnowing algorithm for robust fingerprint generation.
- **Similarity Detection:** Calculates and reports a similarity score (percentage) based on overlapping fingerprints.
- **Configurable Parameters:** Supports noise threshold (`k`), guarantee threshold (`t`), and similarity threshold (`s`) for tuning sensitivity.
- **Modular Code Design:** Each processing step is split into separate, testable functions:
  - `StripString.py`
  - `Kgram.py`
  - `hash31.py`
  - `HashList.py`
  - `Window.py`
  - `Fingerprint.py`
  - `RightMin.py`
  - `FindMatchIndices.py`
  - `FindMatchPositions.py`
  - `SimilarityScore.py`
- **Command-Line Interface:** A main script (`main.py`) runs the entire pipeline, prompting the user for input parameters and the target directory.

## How It Works

The algorithm follows these five major steps:

1. **Preprocessing:**
   - **StripString:** Removes whitespace and converts all text to lowercase.
2. **K-gram Generation:**
   - **Kgram:** Divides the cleaned text into overlapping substrings of length `k`.
3. **Hashing:**
   - **HashList:** Converts each k-gram to an integer using the `hash31` function.
4. **Fingerprinting:**
   - **Window:** Organizes the list of hash values into overlapping windows.
   - **Fingerprint:** Selects the rightmost minimum hash from each window to form the document’s fingerprint.
5. **Comparison:**
   - **FindMatchPositions:** Finds matching fingerprint positions between two documents.
   - **SimilarityScore:** Calculates the proportion of matching characters (based on matching fingerprints) relative to the total document length.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/catch-the-cheaters.git
   cd catch-the-cheaters
