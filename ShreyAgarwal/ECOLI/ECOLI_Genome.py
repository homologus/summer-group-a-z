f = open("ECOLI_Genome.txt", "r")
string = f.readlines()
string = [element.rstrip() for element in string]
DNA = ""
DNA = DNA.join(string)
print(DNA)
f.close()
