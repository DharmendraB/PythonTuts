print("Jai Mataji")
i = 0
while(True):
    if i+1 < 5:
        i = i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        break
    i = i +1


while(True):
    inp = int(input("Enter a Number\n"))
    if inp > 100:
        print("Congraulation Number greater thnen 100\n")
        break
    else:
        print("try again onther number\n")

