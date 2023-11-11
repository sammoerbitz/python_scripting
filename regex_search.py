# Script that searches all .txt files in a folder for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

import re
import os
import sys

# Get the folder path from the user
print("Enter the folder path to search: ")
folderPath = input()

# Get the regex from the user
print("Enter the regex to search for: ")
regex = input()

# Compile the regex
regex = re.compile(regex)

# Loop through all files in the folder
for filename in os.listdir(folderPath):
    # Check if is a txt file
    if not filename.endswith('.txt'):
        continue
    print("Searching file: " + filename)
    # Open the file
    file = open(os.path.join(folderPath, filename))
    # Loop through each line in the file
    for line in file.readlines():
        # Check if the line matches the regex
        if regex.search(line):
            # Print the line
            print(line)
    # Close the file
    file.close()
