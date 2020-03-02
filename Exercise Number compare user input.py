print("Jai Mataji")

n=18
countno = 1
print("Your Guesess Limit is 9 be careful")
while(countno <=9):
    une = int(input("Please Enter Number\n"))
    if n>une:
        print("Please enter Greater Number")

    elif n<une:
        print("Please enter Smallest Number")
    else:
        print("Congrats you won game")
        break
    print("Your Left Guesess is", 9 - countno)
    if countno == 9:
        print("Sorry Game over Try again")

    countno = countno + 1


