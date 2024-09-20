def Reverse_DNA(DNA_String):
   
    return DNA_String[::-1]

def Complement_DNA(DNA_String_reverse, DNA_complement):

    for nucleotide in DNA_String_reverse:
        if nucleotide == "A": DNA_complement += "T"
        elif nucleotide == "G": DNA_complement += "C"
        elif nucleotide == "C": DNA_complement += "G"
        elif nucleotide == "T": DNA_complement += "A"
    return DNA_complement

def main():

    DNA_String_1 = open("Complementing_DNA/rosalind_revc.txt").read()

    DNA_string_reverse_1 = Reverse_DNA(DNA_String_1)
    DNA_complement_1 = ""
    DNA_complement_1 = Complement_DNA(DNA_string_reverse_1, DNA_complement_1)
    print(DNA_complement_1)

if __name__ == '__main__':
    main()