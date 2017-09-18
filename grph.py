#!/usr/bin/env	python

"""
Author: Linh Nguyen

"""
from sys import argv


def file_reading(Fasta_file):
    """
    Returns a list of lines in string format

    Parameter: a text file
    """
    records = []
    seq = []
    with open(Fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                label = line.strip(">")
                if seq:
                    seq = "".join(seq)
                    records.append((label, seq))
                    seq = []
            else:
                seq.append(line)
        if seq:
            seq = "".join(seq)
            records.append((label, seq))
    return records


def overlap_graph(records, kmer):
    """
    Returns The adjacency list corresponding to overlapping k-mer
    """
    overlaps_list = []
    for x1, y1 in records:
        for x2, y2 in records:
            if x1 != x2:
                if y1[-kmer:] == y2[:kmer] or y2[-kmer:] == y1[:kmer]:
                    print '%s %s' % (x1, x2)
                    overlaps_list.append((x1, x2))
    return overlaps_list


def writing_file(overlaps_list):
    outputfile = open('grph_output.txt', 'w')
    line = ''
    for x, y in overlaps_list:
        line += '%s %s\n' % (x, y)
    line = line[:-1]  # to remove the last white space
    outputfile.write(line)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read and parse file
    records = file_reading(input_text_file)

    # Overlap graphs
    overlaps_list = overlap_graph(records, 3)

    # Write file
    writing_file(overlaps_list)
