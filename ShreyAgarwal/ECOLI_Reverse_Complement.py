f = open("ECOLI_gff.txt", "r")
first_line = f.readline()
x = f.readlines()
x = [genome.rstrip() for genome in x]
DNA = ""
DNA = DNA.join(x)

for line in DNA:
	if ("-") in line: print(line),

f.close()

