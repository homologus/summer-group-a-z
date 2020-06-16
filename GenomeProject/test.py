f  = open("EcoliGenome.txt" , "r")
a = f.readline()
x = f.readlines()
x = [item.rstrip() for item in x]
s = ""
s = s.join(x)


g = open("gffForEcoli.txt", "r")
commentedLines = 7
linesChecked = 0
while linesChecked < commentedLines:
	linesChecked+=1
	z = g.readline()
found = False;
while not found :
	readingLine = g.readline()
	TurnToList = list(readingLine.split("\t"))
	if TurnToList[2] != 'CDS':
		readingLine = ""
		continue
	else :
		firstDigit = int(TurnToList[3]) - 1
		LastDigit  = int(TurnToList[4])
		found = True
WhatINeed = s[firstDigit: LastDigit]
i = 0
Amino = ""
print(WhatINeed)

WithTwoUnits = {
"GC" : "A", "CT" : "L", "GG": "G", "CG" : "R", "AC": "T", "CC" :
"P", "TC" : "S", "GT" : "V", "AT": "I"
}

WithAllThreeUnits = {
"ATG": "M", "TTT": "F",  "TTC": "F", "TTA": "L", "TTG": "L", "AGT": "S",  "AGC": "S",
"AGA": "R",  "AGG": "R",  "GAA": "E",  "GAG" : "E", "GAT": "D",  "GAC": "D", "AAA": "K", 
"AAG" : "K", "AAT":"N", "AAC": "N", "CAG": "Q", "CAA": "Q", "CAC": "H",  "CAT": "H", 
"TAT": "Y", "TAC": "Y", "TGT": "C", "TGC": "C", "TGG": "W",
 "TAA": "*",  "TAG": "*", "TGA": "*"
}

while i < int(len(WhatINeed)):
	try:
		Amino += WithAllThreeUnits[WhatINeed[i:i+3]]
	except KeyError:
		Amino += WithTwoUnits[WhatINeed[i: i+2]]
	i+=3
print (Amino)
f.close()
g.close()
