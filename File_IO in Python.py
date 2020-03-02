print("Jai Mataji")
# "r" -Open File for Reading Mode-Default
# "w" -Open a File For Writing Mode
# "x" -Create File if not Exist
# "a" -Add More contant toa file
# "t" -Text Mode -Default
# "b" -Binary Mode
# "+" -Read and Write File

#C = open("Gohil.txt","x")     #Create A File
f = open("Gohil.txt","r")
#Contant = f.read()
# print(Contant)
# print(f.readline())
# print(f.readlines())

#for line in f:
# print(line,end="")
Contant = f.read(60)
print(Contant)
f.close()

