#!/usr/bin/env	python

"""
Author: Linh Nguyen

Argument:
[0] script
[1] a text file containing two strings
"""


from __future__ import division
from sys import argv


def file_reading(a_file):
    """
    Returns a list of lines in string format

    Parameter: a text file
    """
    with open(a_file, 'r')as f:
        line = f.read()
        line = line.strip().split(" ")
        line = [int(x) for x in line]
    return line


def calc_prob(line):
    k, m, n = line
    pop = k + m + n
    max_combi = ((pop**2)-pop)/2

    k_prob = ((k-1)/max_combi) + (k*(m+n)/max_combi)
    m_prob = (((m-1)*0.75/max_combi)) + ((m*n*0.5)/max_combi)
    dom_prob = k_prob + m_prob
    print dom_prob


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read file
    line = file_reading(input_text_file)

    # Calculate the hamm distance
    calc_prob(line)

    # Write file
    # writing_file(hamm_distance)
