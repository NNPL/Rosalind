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
        line = f.read()
        calculating_nucleotides_in_sequences(line)


def calculating_nucleotides_in_sequences(a_sequence):
    """
    Returns the sum of each nucleotide

    """
    sum_A = str(a_sequence.count('A'))
    sum_C = str(a_sequence.count('C'))
    sum_G = str(a_sequence.count('G'))
    sum_T = str(a_sequence.count('T'))

    sum_nt = "%(sum_A)s %(sum_C)s %(sum_G)s %(sum_T)s" % locals()
    print sum_nt


if __name__ == '__main__':

    input_text_file = argv[1]
    file_reading(input_text_file)
