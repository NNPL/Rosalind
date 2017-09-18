#! /usr/bin/env python

"""
Author: Linh Nguyen

"""
from __future__ import division
from sys import argv


def file_reader(fasta_file):
    """
    Returns a fasta file in string format

    """
    seq = []
    seqs = []
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    seq = "".join(seq)
                    seqs.append(seq)
                    seq = []
            else:
                seq.append(line)
        if seq:
            seq = "".join(seq)
            seqs.append(seq)
    return seqs


def transition_transversion_ratio(seqs):
    print seqs
    transition_table = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
    seq1, seq2 = seqs[0], seqs[1]
    transition = 0
    transversion = 0

    for x, y in zip(seq1, seq2):
        if x == y:
            continue
        elif transition_table[x] == y:
            transition += 1
        else:
            transversion += 1
    ratio = (transition / transversion)
    print ratio

    return ratio


def file_writing(ratio):
    outputfile = open('tran_output.txt', 'w')
    outputfile.write(ratio)
    outputfile.close()


if __name__ == '__main__':
    fasta = argv[1]
    seqs = file_reader(fasta)
    ratio = transition_transversion_ratio(seqs)
    # file_writing(ratio)
