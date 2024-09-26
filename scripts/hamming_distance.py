#Count point mutations
class dna_strings:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

def main():

    with open('data/rosalind_hamm.txt') as file:
            string1 = file.readline()
            string2 = file.readline()
  
    strings = dna_strings(string1, string2)

    difference_count = 0
    #test case. expected output = 7
    #strings = dna_strings('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT')


    for i in range(len(strings.string1)):
        if strings.string1[i]!= strings.string2[i]: difference_count+=1

    print(difference_count)



if __name__ == '__main__':
    main()