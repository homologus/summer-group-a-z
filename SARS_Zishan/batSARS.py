fastaFile = open("batSARS_fasta.fasta", "r")
removingTheFirstLine = fastaFile.readline()
theCompleteGenomeInList = fastaFile.readlines()
theCompleteGenomeInList = [item.rstrip() for item in theCompleteGenomeInList]
theCompleteGenome = ""
theCompleteGenome = theCompleteGenome.join(theCompleteGenomeInList)
print(len(theCompleteGenome))
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
count = 0
while i < len(theCompleteGenome):
        if theCompleteGenome[i: i+3] == "TAA" or theCompleteGenome[i: i+3] == "TAG" or theCompleteGenome[i: i+3] == "TGA":
                DNAUntilStopCode = theCompleteGenome[startOfProtein: i+1]
                x = startOfProtein - 3
                while x < i:
                        x += 3;
                        try:
                                Amino += WithAllThreeUnits[theCompleteGenome[x:x+3]]
                        except KeyError:
                                try:
                                        Amino += WithTwoUnits[theCompleteGenome[x: x+2]]
                                except KeyError:
                                        print(theCompleteGenome[x: x+3])
                if len(Amino) > 100:
                     	print("Start of Protein: ", startOfProtein, "End of Protein: ", i, "Protein Sequence: ", Amino)
                startOfProtein = i + 1
                i+=4
        else:
                i+=3
        Amino = ""
        DNAUnitilStopCode = ""
        TheDNAStrand = ""

