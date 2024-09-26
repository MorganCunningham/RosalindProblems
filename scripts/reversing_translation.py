
import numpy

def main():
    reverse_amino = {'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 
                     'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 
                     'C': ['TGT', 'TGC'], 
                     'W': ['TGG'], 
                     'E': ['GAA', 'GAG'], 
                     'D': ['GAT', 'GAC'], 
                     'P': ['CCT', 'CCC', 'CCA', 'CCG'], 
                     'V': ['GTT', 'GTC', 'GTA', 'GTG'], 
                     'N': ['AAT', 'AAC'], 
                     'M': ['ATG'], 
                     'K': ['AAA', 'AAG'], 
                     'Y': ['TAT', 'TAC'], 
                     'I': ['ATT', 'ATC', 'ATA'], 
                     'Q': ['CAA', 'CAG'], 
                     'F': ['TTT', 'TTC'], 
                     'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 
                     'T': ['ACT', 'ACC', 'ACA', 'ACG'], 
                     '*': ['TAA', 'TAG', 'TGA'], 
                     'A': ['GCT', 'GCC', 'GCA', 'GCG'], 
                     'G': ['GGT', 'GGC', 'GGA', 'GGG'], 
                     'H': ['CAT', 'CAC']}


    with open('data/rosalind_mrna.txt') as file:
        protein_string = file.readline().strip()
    file.close()
    print(protein_string)
    #protein_string = "MA"

    multipliers = []
    for amino in protein_string:

        multipliers.append(len(reverse_amino.get(amino)))

    #add stop codon
    multipliers.append(len(reverse_amino.get("*")))
    print(multipliers)

    modulo = numpy.prod(multipliers)%1000000
    multiplied = 1
    for number in multipliers:
        multiplied = number * multiplied

    print(multiplied%1000000)

if __name__ == '__main__':
    main()