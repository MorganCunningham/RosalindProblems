

class dna_main_sub_strings:
    def __init__(self, main_string, sub_string):
        self.main_string = main_string
        self.sub_string = sub_string


def find_substrings(dna_strings):

    positions = list()


    for i in range(len(dna_strings.main_string)):
        position = dna_strings.main_string.find(dna_strings.sub_string, i)
        
        #check if the position has been added already - find will add the same position multiple times
        if position != -1 and position+1 not in positions: positions.append(position+1)

    return positions


def main():

    file = open('data/rosalind_subs.txt').read()
    strings = file.split("\n")
    print(strings)
    #file.close()
    
    #test case. should return 2,4,10
    #strings = ['GATATATGCATATACTT', 'ATAT']

    dna_strings = dna_main_sub_strings(strings[0], strings[1])

    pos = find_substrings(dna_strings)
    
    pos_string = map(str, pos)
    pos_string = ' '.join(pos_string)
    print(pos_string)
    





if __name__ == '__main__':
    main()
