f  = open("EcoliGenome.txt" , "r")
x = f.readlines()
x = [item.rstrip() for item in x]
s = ""
s = s.join(x)
WhatINeed = s[190:256]
i = 0
Amino = ""
print(WhatINeed)

WithTwoUnits = {"GC" : "A", "CT" : "L", "GG": "G", "CG" : "R", "AC": "T", "CC" :
"P", "TC" : "S", "GT" : "V", "AT": "I"}
#run WithAllThreeUnits first
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
