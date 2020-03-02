print("Jai Mataji")
a = 10
b = 5
c = sum((a,b)) # buil in Function
print(c)

#define Functon and  return Values
def function1(a,b):
    average = (a+b)/2
    return average
v = function1(7,8)
print("Enter Two number Average is = "+str(v))

# doc string of function
def funAvr(a,b):
    """This Function will Calculate Average of Two Numbers"""
    average = (a+b)/2
    return average
print(funAvr.__doc__)

