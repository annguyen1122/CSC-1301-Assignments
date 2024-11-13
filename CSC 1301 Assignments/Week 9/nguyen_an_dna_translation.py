#Imports functions from the helper.py file.
import helper

"""
Program Description: This program takes a given DNA sequence translates it to a protein sequence.

Author: Nguyen, An
"""

#Creates a function that transcripts a DNA sequence into a mRNA sequence.
def transcription(dna_sequence):
    #Creates an empty string
    complement = ''
    # Replace Thymine with Uracil
    mrna = dna_sequence.replace("T", "U")
    # Create the Base Pair Complement
    for i in range(len(mrna)):
        if mrna[i] == "A":
            complement += "U"
        elif mrna[i] == "U":
            complement += "A"
        elif mrna[i] == "C":
            complement += "G"
        elif mrna[i] == "G":
            complement += "C"
    # Returns the complement
    return complement

#Creates a function that translates mRNA sequence to protien sequence.
def translate(mrna):
    #Creates an empty string
    protein = ''
    # Split mrna into nucleotide triplets
    nucleotide_triplets = helper.chunk(mrna, 3)
    # Replace Triplets with Amino Acids
    #For all the triplets, if it's part of the amino acid dictionary from helper, add it's corresponding value to the empty string.
    for i in nucleotide_triplets:
        if i in helper.amino_acids:
            protein += f"{helper.amino_acids[i]} "
    return protein

if __name__ == "__main__":
    #Defines the DNA sequence used.
    dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'
    #Uses the transcription function to get the mRNA sequence
    mrna = transcription(dna)
    #Uses the translate function to get the protein seuqence.
    protein_sequence = translate(mrna)

    #Prints all the sequences gathered from the program.
    print("DNA Sequence")
    print(dna)
    print("mRNA Sequence")
    print (mrna)
    print("Protein Sequence")
    print(protein_sequence)