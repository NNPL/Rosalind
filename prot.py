#!/usr/bin/env	python

"""
Author: Linh Nguyen

Argument:
[0] script
[1] a text file containing a string

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
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}


def file_reading(a_file):
    """
    Returns a long string

    Parameter: a text file
    """

    with open(a_file, 'r') as f:
        string = f.read().strip()
    return string


def protein_translation(RNAstring):
    """
    Returns a protein string

    Parameter: a RNA sequence string
    """

    codon = ''
    protein_sequence = ''
    for i in range(0, len(RNAstring), 3):
        codon = RNA_CODON_TABLE[RNAstring[i:i + 3]]
        if codon == 'stop':
            break
        else:
            protein_sequence += codon

    print protein_sequence


def writing_file(protein_sequence):
    """
    Returns a text file containing the protein sequence in string format.

    Parameter: a protein sequence string
    """

    outputfile = open('prot_output.txt', 'w')
    outputfile.write(protein_sequence)
    outputfile.close()


if __name__ == '__main__':
    # inputs
    input_text_file = argv[1]

    # Read file
    string = file_reading(input_text_file)

    # Translate a RNA sequence into protein sequence
    protein_translation(string)

    # Write file
    # writing_file(protein_sequence)
