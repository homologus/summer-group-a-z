f = open("ECOLI_Genome.txt", "r")
string = f.readlines()
string = [element.rstrip() for element in string]
DNA = ""
DNA = DNA.join(string)
DNA_Short_String = DNA[189:254]
length = int(len(DNA_Short_String))

complement = {
	"A" : "T"
	"C" : "G"
	"T" : "A"
	"G" : "A"
}

complement_string =  ""

x = 0

while x < length:
	complement_string = complement[DNA_Short_String[x:x + 1]]
	i += 1

print(complement_string)

f.close()
