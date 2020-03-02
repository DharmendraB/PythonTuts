print("jai mataji")

def funcargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("Now i whould like to instroduce our heroes")

    for key,value in kwargs.items():
        print(f"{key} is a {value}")

har = ["Gohil","Ramesh","Raghav","Ravat","shiv"]
Normal = "I am normal argument and the student are:"
# kw = ["Gohil":"Sir","Ramesh":"Monitor","Shiv":"Cerk"] # error becuage list is tuple string
kw = {"Gohil":"sir","Ramesh":"Monitor","Ravat":"Admin"}
funcargs(Normal, *har, **kw)
