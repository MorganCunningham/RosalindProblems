class fasta_string:
    def __init__(self, name, string, gc_content):
        self.name = name
        self.string = string
        self.gc_content = gc_content

def create_sequence_list(file):
        sequence_list = list()
        for sequence in file:
            #This will fail if the fasta file # is different from 4. Needs a different method to detect the name. i.e. get string
            # first occurence of /n
            sequence_name = sequence[0:13]
            #print(sequence_name)
            sequence_string = sequence[13:len(sequence)].replace("\n", "")
            
            sequence_temp = fasta_string(sequence_name, sequence_string, 0)

            sequence_list.append(sequence_temp)
            
        return sequence_list


def get_gc_content(sequence):

    sequence.gc_content = (float((sequence.string.count("G") + sequence.string.count("C")))/float(len(sequence.string)))*100
    

def main():
    file = open("data/rosalind_gc.txt").read()
   
    file = file.split(">")
    file.remove("")

    sequence_list = create_sequence_list(file)
    
    largest_gc = ["name", 0]
    
    for sequence in sequence_list:
        get_gc_content(sequence)

        if largest_gc[1] == 0:
            largest_gc[0] = sequence.name
            largest_gc[1] = sequence.gc_content

        else:
            if sequence.gc_content > largest_gc[1]:
                largest_gc[0] = sequence.name
                largest_gc[1] = sequence.gc_content

    print(largest_gc)

if __name__ == '__main__':
    main()