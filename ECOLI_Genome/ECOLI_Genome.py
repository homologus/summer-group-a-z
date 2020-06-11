f = open("ECOLI_Genome.txt", "r") 
x = f.readline()
while x:
    print(x)
    x = f.readline()
f.close()
