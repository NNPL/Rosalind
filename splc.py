#!/usr/bin/env python

"""
Author: Linh Nguyen

"""

from sys import argv

RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}


def file_reader(fasta_file):
    """
    Returns a fasta file in string format

    """
    seqs = []
    seq = []
    flag = False
    with open(fasta_file, 'r')as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    seq = "".join(seq)
                    flag = True
            elif not flag:
                seq.append(line)
            else:
                seqs.append(line)
        if seqs:
            seqs.append(line)
    return seq, seqs


def RNA_splicer(sequence, substrings):
    substrings = sorted(substrings, key=len, reverse=True)
    for strings in substrings:
        sequence = sequence.replace(strings, '')
    sequence = sequence.replace('T', 'U')
    return sequence


def RNA_translation(RNAsequence):
    codon = ''
    protein_sequence = ''
    for i in range(0, len(RNAsequence), 3):
        codon = RNA_CODON_TABLE[RNAsequence[i:i + 3]]
        if codon == 'stop':
            break
        # else:
        protein_sequence += codon
    print protein_sequence


def file_writing(protein_sequence):
    outputfile = open('splc_output.txt', 'w')
    outputfile.write(protein_sequence)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read and parse file
    targetseq, seqs = file_reader(input_text_file)

    # RNA splicing and translation
    RNAsequence = RNA_splicer(targetseq, seqs)
    RNA_translation(RNAsequence)

    # Write file
    # file_writing(protein_sequence)
