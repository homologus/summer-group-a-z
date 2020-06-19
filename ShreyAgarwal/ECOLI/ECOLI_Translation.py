f = open("ECOLI_Genome.txt", "r")
string = f.readlines()
string = [element.rstrip() for element in string]
DNA = ""
DNA = DNA.join(string)
DNA_Short_String = DNA[189:254]
length = int(len(DNA))
sequence_to_use = DNA_Short_String

translation = {
	"TTT": "F",
	"TTC": "F",
	"TTA": "L",
	"TTG": "L",
	"CTT": "L",
	"CTC": "L",
	"CTA": "L",
	"CTG": "L",
	"ATT": "I",
	"ATC": "I",
	"ATA": "I",
	"ATG": "M",
	"GTT": "V",
	"GTC": "V",
	"GTA": "V",
	"GTG": "V",
	"TCT": "S",
	"TCC": "S",
	"TCA": "S",
	"TCG": "S",
	"CCT": "P",
	"CCC": "P",
	"CCA": "P",
	"CCG": "P",
	"ACT": "T",
	"ACC": "T",
	"ACA": "T",
	"ACG": "T",
	"GCT": "A",
	"GCC": "A",
	"GCA": "A",
	"GCG": "A",
	"TAT": "Y",
	"TAC": "Y",
	"CAT": "H",
	"CAC": "H",
	"CAA": "Q",
	"CAG": "Q",
	"AAT": "N",
	"AAC": "N",
	"AAA": "K",
	"AAG": "K",
	"GAT": "D",
	"GAC": "D",
	"GAA": "E",
	"GAG": "E",
	"TGT": "C",
	"TGC": "C",
	"TGG": "W",
	"CGT": "R",
	"CGC": "R",
	"CGA": "R",
	"CGG": "R",
	"AGT": "S",
	"AGC": "S",
	"AGA": "R",
	"AGG": "R",
	"GGT": "G",
	"GGC": "G",
	"GGA": "G",
	"GGG": "G", 
	"TGA": "Stop Codon",
	"TAA": "Stop Codon",
	"TAG": "Stop Codon",
	"C": "Done",
	"TG": "Done",
	"CA": "Done"
}

x = 0
Protein_Sequence = ""

while(x < length):
        y = str(sequence_to_use[x:x + 3])
        print(translation[y], )
        x = x + 3
print(sequence_to_use)
f.close()
