from Bio.Seq import Seq

f = open("Bat_SARS.txt", "r")
first_line = f.readline()
string = f.readlines()
string = [item.rstrip() for item in string]
RNA = ""
RNA = RNA.join(string)
print(len(RNA))
x = 0

read = Seq(RNA)

protein_translate = str(read.translate())

x = protein_translate.split("*")

for element in x:
	if int(len(element)) > 100:
		print("Next Protein: ")
		print(element)
