#!/usr/bin/env	python

"""
Author: Linh Nguyen

"""
from sys import argv


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


def file_reading(Fasta_file):
    """
    """
    seq = []
    with open(Fasta_file, 'r') as f:
        for line in nonblank_lines(f):
            if not line.startswith('>'):
                seq.append(line)
    seq = "".join(seq)
    return seq


def reverse_complement(DNA_string):
    """
    Return the complement of a given DNA string.

    Parameter: a DNA string
    """

    DNA_string = DNA_string.upper()
    nt_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = ''

    for ch in reversed(DNA_string):
        nt = nt_dict[ch]
        reverse_complement += nt
    return reverse_complement


def reverse_palindrome_finder(DNAseq):
    """
    Return: a list of position and length of every reverse palindrome in
    the string having length between 4 and 12.

    parameter:
    DNAseq: a DNA sequence string

    """

    results = []

    length = len(DNAseq)
    for i in range(length):
        for j in range(4, 13):
            if i + j > length:
                continue
            s1 = DNAseq[i:i + j]
            s2 = reverse_complement(s1)
            if s1 == s2:
                results += [i + 1, j]

    for i in range(len(results) - 1):
        if i % 2 == 0:
            print '%s %s' % (results[i], results[i + 1])

    return results


def write_file(palindrome_list):
    outputfile = open('revp_output.txt', 'w')
    line = ''
    for i in range(len(palindrome_list) - 1):
        if i % 2 == 0:
            line += '%s %s\n' % (palindrome_list[i], palindrome_list[i + 1])
    outputfile.write(line[:-1])
    outputfile.close()


if __name__ == '__main__':
    fastafile = argv[1]

    DNAsequence = file_reading(fastafile)
    reverse_palindrome_finder(DNAsequence)
    # write_file(palindrome_position_and_length_list)
