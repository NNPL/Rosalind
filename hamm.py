#!/usr/bin/env	python

"""
Author: Linh Nguyen

Argument:
[0] script
[1] a text file containing two strings
"""

from sys import argv


def file_reading(a_file):
    """
    Returns a list of lines in string format

    Parameter: a text file
    """

    lines = open(a_file, 'r').read()
    lines = lines.split('\n')
    return lines


def calculating_hamm_distance(lines):
    """
    Returns the hamm distance between two strings.

    Parameter: a list of lines in string format.
    In this case there are only 2 lines; 2 strings.

    """
    sequence1 = lines[0]
    sequence2 = lines[1]

    if len(sequence1) != len(sequence2):
        raise ValueError("The two given strings do not have a equal length!")

    hamm_distance = 0
    for x, y in zip(sequence1, sequence2):
        if x != y:
            hamm_distance += 1

    print hamm_distance


def writing_file(hamm_distance):
    """
    Returns a text file containing the hamm distance in string format.

    Parameter: the hamm distance between 2 strings
    """

    outputfile = open('hamm_output.txt', 'w')

    outputfile.write(str(hamm_distance))
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read file
    lines = file_reading(input_text_file)

    # Calculate the hamm distance
    hamm_distance = calculating_hamm_distance(lines)

    # Write file
    # writing_file(hamm_distance)
