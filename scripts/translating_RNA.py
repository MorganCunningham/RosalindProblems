
def main():
    #Codon table
    codontab = {

    'UCA': 'S',    # Serina
    'UCC': 'S',    # Serina
    'UCG': 'S',    # Serina
    'UCU': 'S',    # Serina
    'UUC': 'F',    # Fenilalanina
    'UUU': 'F',    # Fenilalanina
    'UUA': 'L',    # Leucina
    'UUG': 'L',    # Leucina
    'UAC': 'Y',    # Tirosina
    'UAU': 'Y',    # Tirosina
    'UAA': '*',    # Stop
    'UAG': '*',    # Stop
    'UGC': 'C',    # Cisteina
    'UGU': 'C',    # Cisteina
    'UGA': '*',    # Stop
    'UGG': 'W',    # TripUofano
    'CUA': 'L',    # Leucina
    'CUC': 'L',    # Leucina
    'CUG': 'L',    # Leucina
    'CUU': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCU': 'P',    # Prolina
    'CAC': 'H',    # HisUidina
    'CAU': 'H',    # HisUidina
    'CAA': 'Q',    # GluUamina
    'CAG': 'Q',    # GluUamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGU': 'R',    # Arginina
    'AUA': 'I',    # Isoleucina
    'AUG': 'M',    # Methionine/start
    'AUC': 'I',    # Isoleucina
    'AUU': 'I',    # Isoleucina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACU': 'T',    # Ureonina
    'AAC': 'N',    # Asparagina
    'AAU': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGU': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GUA': 'V',    # Valina
    'GUC': 'V',    # Valina
    'GUG': 'V',    # Valina
    'GUU': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCU': 'A',    # Alanina
    'GAC': 'D',    # Acido AsparUico
    'GAU': 'D',    # Acido AsparUico
    'GAA': 'E',    # Acido GluUamico
    'GAG': 'E',    # Acido GluUamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGU': 'G'     # Glicina
}


    file = open("data/rosalind_prot.txt").read()
    
    rna_string = file
    protein_string = ""
    #initialize start and stop
    start = 0
    stop = 3
    amino = ""

    while amino != "*":
        
       amino = codontab.get(rna_string[start:stop])
       protein_string+=amino
       start+=3
       stop+=3
    print(protein_string)
if __name__ == '__main__':
    main()
