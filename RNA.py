#!/usr/bin/env	python

"""
Author: Linh Nguyen

"""
from sys import argv


def file_reading(a_text_file):
    """
    Returns lines in string format

    Parameters: a text file
    """
    with open(a_text_file, 'r') as f:
        lines = f.read()
        lines = lines.strip()
    return lines


def DNA_translation(DNA_string):
    """
    Returns a translated DNA string

    Parameter: a DNA string
    """

    RNA_string = DNA_string.replace('T', 'U')

    print RNA_string


def writing_file(RNA_string):
    """
    Returns a text file

    Parameter: a RNA string
    """

    outputfile = open('RNA_output.txt', 'w')
    outputfile.write(RNA_string)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read file
    DNA_string = file_reading(input_text_file)

    # Translation
    DNA_translation(DNA_string)

    # Write file
    # writing_file(RNA_string)
