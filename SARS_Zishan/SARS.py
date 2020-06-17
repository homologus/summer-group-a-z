from Bio.Seq import Seq

fastaFile = open("SARS_fasta.fasta", "r")
removingTheFirstLine = fastaFile.readline()
theCompleteGenome = fastaFile.readlines()
i = 0
startOfProtein = 0
DNAUntilStopCode = ""
Amino = ""
TheDNAStrand = ""
WithTwoUnits = {"GC" : "A", "CT" : "L", "GG": "G", "CG" : "R", "AC": "T", "CC" :
"P", "TC" : "S", "GT" : "V", "AT": "I"}
WithAllThreeUnits = {
"ATG": "M", "TTT": "F",  "TTC": "F", "TTA": "L", "TTG": "L", "AGT": "S",  "AGC": "S",
"AGA": "R",  "AGG": "R",  "GAA": "E",  "GAG" : "E", "GAT": "D",  "GAC": "D", "AAA": "K",
"AAG" : "K", "AAT":"N", "AAC": "N", "CAG": "Q", "CAA": "Q", "CAC": "H",  "CAT": "H",
"TAT": "Y", "TAC": "Y", "TGT": "C", "TGC": "C", "TGG": "W",
 "TAA": "*",  "TAG": "*", "TGA": "*"
}

while i < len(theCompleteGenome):
	if theCompleteGenome[i: i+3] == "TAA" or "TAG" or "TGA":
		DNAUntilStopCode = theCompleteGenome[startOfProtein: i+1]
		x = startOfProtein
		while x < i:
	       		try:
                		Amino += WithAllThreeUnits[DNAUntilStopCode[i:i+3]]
        		except KeyError:
                		Amino += WithTwoUnits[DNAUntilStopCode[i: i+2]]
			finally:
				x += 3
		if len(Amino) > 100:
			print("Start of Protein: ", startOfProtein, "End of Protein: ", i, "Protein Sequence: ", Amino)
		startOfProtein = i+1 
	i+=3
	Amino = ""
	DNAUnitilStopCode = ""
	TheDNAStrand = ""
