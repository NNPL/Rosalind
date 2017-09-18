#!/usr/bin/env	python

"""
Author: Linh Nguyen

This script returns the reverse complement of a given DNA string.

Argument:
[0] script
[1] a fasta file
"""
from __future__ import division
from sys import argv
import re


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


def file_reading(Fasta_file):
    """
    """
    label = None
    seq = []
    with open(Fasta_file, 'r') as f:
        for line in nonblank_lines(f):
            if line.startswith('>'):
                if label:
                    seqs = "".join(seq)
                    seq = []
                    yield label, seqs
                label = line.strip(">")
            else:
                seq.append(line)


def determine_ID_with_highest_gcContent(Fasta_file):
    """
    """
    highest_gcContent = None
    for label, seq in file_reading(Fasta_file):
        gcContent = calculating_gcContent(seq)
        if gcContent > highest_gcContent:
            ID = label
            highest_gcContent = gcContent

    print "%s\n%f" % (ID, highest_gcContent)


def calculating_gcContent(seq):
    totalBaseCount = len(seq)
    print seq
    gcCount = len(re.findall('[GCgc]', seq))
    gcContent = (gcCount / totalBaseCount) * 100
    return gcContent


def writing_file(ID, gcContent):
    """
    """
    outputfile = open('gc_output.txt', 'w')
    # width of 8 characters and a precision of 6 decimal places
    gcContent = "{:8.6f}".format(gcContent)

    outputfile.write(ID + '\n' + gcContent)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Determine the ID with highest GC content
    determine_ID_with_highest_gcContent(input_text_file)

    # Write file
    # writing_file(ID, gcContent)
