print("jai Mataji")
#File Write Mode and write contant
'''f = open("GohilDB.txt","w")
f.write("Hello Gohil Dharmendra")
f.close()'''

#Apend Contant in File EX.
# f =open("GohilDB.txt","a")
# a = f.write("\n How are You??")
# print(a)
# f.close()

# Lenght Retun of file
'''f = open("GohilDB.txt","w")
a = f.write("Hello Gohil")
print(a)
f.close()'''

# Handle Read And Write Both
f = open("GohilDB.txt","r+")
print(f.read())
f.write("\nHow are you?")
f.close()




