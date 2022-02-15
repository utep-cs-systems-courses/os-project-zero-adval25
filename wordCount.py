#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# set input and output files
if len(sys.argv) != 3:
    print('Number of required agruments is 3: wordCount.py <input file> <output file>')
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

#execute the program with 
#subprocess.call(["python3", "./wordCount.py", inputFname, outputFname])

# check that program exists
if not os.path.exists("wordCount.py"):
    print ("wordCount.py Does Not Exist")
    exit()

if not os.path.exists(inputFname):
    print("Input Path Does Not Exist")
    exit()

if not os.path.exists(outputFname):
    print("Output Path Does Not Exist")
    exit()
    
words = []
count = []
combined = []

# read from input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        line = line.strip()
        remove_chars = ['.', ',', ';', ':', '\'', '\"', '!', '?', '-','--']
        for char in remove_chars:
            line = str.replace(line, char, ' ')
        word = line.split()
        for w in word:
            if w not in words:
                words.append(w)
                count.append(1)
            else:
                pos = words.index(w)
                count[pos]+=1

# sort word occurence combinations
for e in range(0, len(words)):
    element = words[e]+' '+str(count[e])
    combined.append(element)
combined.sort()

# write to output file
with open(outputFname, 'w') as outputFile:
    for c in combined:
        outputFile.write(c+'\n')