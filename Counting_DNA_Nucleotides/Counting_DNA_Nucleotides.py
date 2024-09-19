class nucleotide_string_count:
    def __init__(self, A, C, G, T):
        self.A = A
        self.C = C
        self.G = G
        self.T = T

def count_nucleotides(nucleotide_count, DNA_String):

    for nucleotide in DNA_String:
        if nucleotide == "A": nucleotide_count.A +=1
        if nucleotide == "C": nucleotide_count.C +=1
        if nucleotide == "G": nucleotide_count.G +=1
        if nucleotide == "T": nucleotide_count.T +=1
    
    return nucleotide_count

def main():

    DNA_String_1 = open("Counting_DNA_Nucleotides/rosalind_dna.txt").read()

    nucleotide_count_1 = nucleotide_string_count(0 ,0, 0, 0)

    nucleotide_count_1 = count_nucleotides(nucleotide_count_1, DNA_String_1)

    print(nucleotide_count_1.A, nucleotide_count_1.C, nucleotide_count_1.G, nucleotide_count_1.T)

if __name__ == '__main__':
    main()