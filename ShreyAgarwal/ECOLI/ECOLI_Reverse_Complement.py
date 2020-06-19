f = open("ECOLI_Genome.txt", "r")
first_line = f.readline()
x = f.readlines()
x = [genome.rstrip() for genome in x]
DNA = ""
DNA = DNA.join(x)
DNA_Short_String = DNA[189:254]
sequence_to_use = DNA_Short_String

def Reverse_Complement(seq):
    reverse_complement = ""
    for letter in seq:
        if letter == "A":
            reverse_complement += "T"
        elif letter == "T":
            reverse_complement += "A"
        elif letter == "G":
            reverse_complement += "C"
        else:
            reverse_complement += "G"
    return (reverse_complement[::-1])


print("The reverse complement of the sequence is " + Reverse_Complement(sequence_to_use) + ".")

length = int(len(sequence_to_use))

translation ={'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L', 'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y', 'TAC':'Y', 'TAA':'STOP', 'TAG':'STOP', 'TGT':'C', 'TGC':'C', 'TGA':'STOP', 'TGG':'W',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAT':'H',
'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGT':'R', 'CGC':'R', 'CGA':'R','CGG':'R',
'ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T',
'AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R',
'GTT':'V','GTG':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
'GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGC':'G','GGA':'G','GGG':'G',
'AA': ' ', 'TG': ' '};

x = 0

Protein_Sequence = ""

while (x < length):
    Protein_Sequence += translation[sequence_to_use[x:x + 3]]
    x = x + 3
print("The protein translation of the reverse complement is " + str(Protein_Sequence) + ".")

f.close()
