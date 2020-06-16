from Bio.Seq import Seq

fastaFile = open("SARS_fasta.fasta", "r")
removingTheFirstLine = fastaFile.readline()
theCompleteGenome = fastaFile.readlines()
i = 0
startOfProtein = 0
DNAUntilStopCode = ""
Amino = ""
while i < len(theCompleteGenome):
	if theCompleteGenome[i: i+3] == "TAA" or "TAG" or "TGA":
		DNAUnitilStopCode = theCompleteGenome[startOfProtein: i+1]
		Amino = Seq(DNAUntilStopCode)
		if len(Amino) > 99:
			print(Amino)
		startOfProtein = i+1 
	else:
		i+=3
