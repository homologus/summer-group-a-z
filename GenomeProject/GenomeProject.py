f  = open("EcoliGenome.txt" , "r")
x = f.read()
WhatINeed = x[191:257] 
WhatINeed = WhatINeed.rstrip("\n")
print(WhatINeed)
i = 1
Amino = ""
while i <= int( len(WhatINeed)):
	AminoLoop = WhatINeed[i, i+2]
	if AminoLoop[i, i+2] ==  "GC":
		Amino = Amino + 'A'
	elif AminoLoop[i, i+2] ==  "CT":
		Amino = Amino + 'L'
	elif AminoLoop[i, i+2] == "GG":
		Amino = Amino + 'G'
	elif AminoLoop[i , i+2] == "CG":
		Amino = Amino + 'R'
	elif AminoLoop[i, i+2] == "AC":
		Amino = Amino + 'T'
	elif AminoLoop[i, i+2] == "CC":
		Amino = Amino + 'P'
	elif AminoLoop[i, i+2] == "TC":
		Amino = Amino + 'S'
	elif AminoLoop[i, i+2] == "GT":
		Amino = Amino + 'V'
	elif AminoLoop == "ATG":
		Amino = Amino + 'M'
	elif AminoLoop[i, + i+2] == "AT":
		Amino = Amino + 'I' 
f.close()
