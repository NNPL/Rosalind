#!/usr/bin/env	python

"""
Author: Linh Nguyen

Argument:
[0] script
[1] a file containing two lines of DNA strings
"""
from sys import argv


def file_reading(Fasta_file):
    """
    Returns a list of lines in string format

    Parameter: a text file
    """

    with open(Fasta_file, 'r') as f:
        lines = f.read()
        lines = lines.split('\n')
    return lines


def motif_finder(lines):
    """
    Returns all start position of the motif in a list

    """
    DNAstring = lines[0]
    motif = lines[1]

    motif_length = len(motif)
    pos_list = []
    num_frames = len(DNAstring) - motif_length + 1
    for i in range(num_frames):
        frame = DNAstring[i:i + motif_length]
        if frame == motif:
            startpos = i + 1
            pos_list.append(str(startpos))
    print " ".join(pos_list)


def writing_file(pos_list):
    """
    Returns a text file containing a string of start positions of the motif

    Parameter: a list of start positions (integers)
    """

    outputfile = open('subs_output.txt', 'w')
    line = ''
    for pos in pos_list:
        line += str(pos) + ' '
    line = line[:-1]  # to remove the last white space
    outputfile.write(line)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read file
    lines = file_reading(input_text_file)

    # Find motif in a DNA string
    pos_list = motif_finder(lines)

    # Write file
    # writing_file(pos_list)
