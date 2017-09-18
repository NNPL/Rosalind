#!/usr/bin/env	python

"""
Author: Linh Nguyen

This script returns the reverse complement of a given DNA string.

Argument:
[0] script
[1] a text file containing a DNA string
"""
from sys import argv


def file_reading(a_text_file):
    """
    Returns lines in string format

    Parameter: a text file
    """
    with open(a_text_file, 'r') as f:
        lines = f.read()
        lines = lines.strip()
    return lines


def complement_DNAstring(DNA_string):
    """
    Return the complement of a given DNA string.

    Parameter: a DNA string
    """

    DNA_string = DNA_string.upper()
    nt_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement_string = ''

    for ch in DNA_string:
        seq = nt_dict[ch]
        complement_string += seq
    return complement_string


def reverse_DNAstring(complement_string):
    """
    Return the reverse of a given complment DNA string.

    Parameter: a complement DNA string
    """

    reverse_complement_string = ''
    for ch in reversed(complement_string):
        reverse_complement_string += ch
    print reverse_complement_string


def writing_file(reverse_complement_string):
    """
    Returns a text file

    Parameter: a reverse complement DNA string
    """

    outputfile = open('revc_output.txt', 'w')
    outputfile.write(reverse_complement_string)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read file
    DNA_string = file_reading(input_text_file)

    # Create the reverse complement DNA string
    complement_string = complement_DNAstring(DNA_string)
    reverse_DNAstring(complement_string)

    # Write file
    # writing_file(reverse_complement_string)
