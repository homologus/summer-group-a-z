f = open("California_SARS-CoV-2.txt", "r")
string = f.readlines()
string = [item.rstrip() for item in string]
RNA = ""
RNA = RNA.join(string)
print(RNA)
