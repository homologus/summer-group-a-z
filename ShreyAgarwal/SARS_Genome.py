from Bio.Seq import Seq

f = open("SARS.txt", "r")
first_line = f.readline()
string = f.readlines()
string = [item.rstrip() for item in string]
RNA = ""
RNA = RNA.join(string)
print(len(RNA))
x = 0
Protein_Start = 0
Stop_Codon = ""
Protein_Seq = ""

read = Seq(RNA)

while x < len(RNA):
        if RNA[x:x + 3] == "TAA" or RNA[x:x + 3] == "TAG" or RNA[x:x + 3] == "TGA":
                Stop_Codon = RNA[Protein_Start: x + 1]
                y = Protein_Start - 3
                while y < x:
                        y = y + 3;
                        Protein_Seq = Protein_Seq.join(read[y:y + 3].translate())
                if len(Protein_Seq) > 100:
                        print(Protein_Start, x, Protein_Seq)
                Protein_Start = x + 1
                x = x + 4
        else:
                x = x + 3
        Protein_Seq = ""
        DNAUnitilStopCode = ""

