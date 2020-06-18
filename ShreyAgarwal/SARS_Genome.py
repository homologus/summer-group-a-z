from Bio.Seq import Seq

f = open("SARS.txt", "r")
first_line = f.readline()
string = f.readlines()
string = [item.rstrip() for item in string]
RNA = ""
RNA = RNA.join(string)
RNA = RNA[:-2]
print(len(RNA))
x = 0
Protein_Start = 0
Stop_Codon = ""
Protein_Seq = ""

read = Seq(RNA)

protein_translate = str(read.translate())

print(protein_translate)

x = protein_translate.split("*")

print(x)
