print("jai Mataji")

#user input and print *,**,*** like pyramid

intValue = int(input("Please Enter Number\n"))
boolvalue = input("Enter only 1 or 0 \n")

if boolvalue =="1":
    for i in range(0,intValue+1):
       print(i * "*")

else:
    for i in range(intValue,0,-1):
        print("*"*i)
