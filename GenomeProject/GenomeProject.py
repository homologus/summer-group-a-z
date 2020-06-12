f  = open("EcoliGenome.txt" , "r")
x = f.read()
WhatINeed = x[191:258] 
WhatINeed = WhatINeed.rstrip("\n")
WhatINeed.replace("\n", "")
print(WhatINeed)
i = 0
Amino = ""
while i <= int( len(WhatINeed)):
	AminoLoop = WhatINeed[i:i+3]
	print(AminoLoop)
	print(AminoLoop[0: 2])
	if AminoLoop[0: 2] ==  "GC":
		Amino = Amino + 'A'
	elif AminoLoop[0: 2] ==  "CT":
		Amino = Amino + 'L'
	elif AminoLoop[0: 2] == "GG":
		Amino = Amino + 'G'
	elif AminoLoop[0: 2] == "CG":
		Amino = Amino + 'R'
	elif AminoLoop[0: 2] == "AC":
		Amino = Amino + 'T'
	elif AminoLoop[0: 2] == "CC":
		Amino = Amino + 'P'
	elif AminoLoop[0: 2] == "TC":
		Amino = Amino + 'S'
	elif AminoLoop[0: 2] == "GT":
		Amino = Amino + 'V'
	elif AminoLoop == "ATG":
		Amino = Amino + 'M'
	elif AminoLoop[0: 2] == "AT":
		Amino = Amino + 'I'
	elif AminoLoop == "TTT" or AminoLoop  == "TTC":
		Amino = Amino + 'F'
	elif AminoLoop == "TTA" or AminoLoop == "TTG":
		Amino = Amino + 'L'
	elif AminoLoop == "AGT" or AminoLoop == "AGC":
		Amino = Amino + 'S'
	elif AminoLoop == "AGA" or AminoLoop == "AGG":
		Amino = Amino = 'R'
	elif AminoLoop == "GAA" or AminoLoop == "GAG":
		Amino = Amino + 'E'
	elif AminoLoop == "GAT" or AminoLoop == "GAC":
		Amino = Amino + 'D'
	elif AminoLoop == "AAA" or AminoLoop == "AAG":
		Amino = Amino + 'K'
	elif AminoLoop == "AAT" or AminoLoop == "AAC":
		Amino = Amino + 'N'
	elif AminoLoop == "CAG" or AminoLoop == "CAA":
		Amino = Amino + "Q"
	elif AminoLoop == "CAC" or AminoLoop == "CAT":
		Amino = Amino = 'H'
	elif AminoLoop == "TAT" or AminoLoop == "TAC":
		Amino = Amino + 'Y'
	elif AminoLoop == "TGT" or AminoLoop == "TGC":
		Amino = Amino + 'C'
	elif AminoLoop == "TGG":
		Amino = Amino + 'W'
	else:
		Amino = Amino + '*'
	i+=3

print("\n")
print(Amino)
f.close()
