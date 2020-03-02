print("Jai Mataji")

print("Enter Num1")
Num1 = input()
print("Enter Num2") # Enter String Num2 and show exception
Num2 = input()
try:
    print("The Sum of Two Number is",int(Num1)+int(Num2))
except Exception as e:
    print(e)
print("This Line is Very  Imported")
