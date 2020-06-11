f  = open("EcoliGenome.txt" , "r")
x = f.read()
WhatINeed = x[191:257] 
WhatINeed = WhatINeed.rstrip("\n")
print(WhatINeed)
f.close()
