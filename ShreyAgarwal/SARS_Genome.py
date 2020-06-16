from Bio.Seq import Seq
f = open("SARS.txt", "r")
first_line = f.readline()
string = f.readlines()
string = [genome.rstrip() for genome in string]
RNA = ""
RNA = RNA.join(string)
read = Seq(RNA)

print(read[10:20].reverse_complement)

f.close()

