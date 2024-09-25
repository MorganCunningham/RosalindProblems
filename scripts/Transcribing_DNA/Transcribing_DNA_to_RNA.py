class RNA_String_object:
    def __init__(self, string):
        self.string = ""


def Transcribe(DNA_String, RNA_String):
    
      
    RNA_String.string = DNA_String.replace("T","U")

    return RNA_String

def main():

    DNA_String_1 = open("Transcribing_DNA/rosalind_rna.txt").read()
    RNA_String_1 = RNA_String_object("") 
    RNA_String_1 = Transcribe(DNA_String_1, RNA_String_1)
    print(RNA_String_1.string)

if __name__ == '__main__':
    main()