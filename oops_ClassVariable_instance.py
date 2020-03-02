print("jai mataji")

class Emp:
    no_leave = 5
    pass

Gohil = Emp()
DB = Emp()
Gohil.Name = "Dharmendra"
Gohil.std = 5
DB.Name = "Sample Name"
DB.std = 10
print(Emp.no_leave)
print(Gohil.__dict__)
Gohil.no_leave = 10
print(Gohil.__dict__)
print(Emp.no_leave)
Emp.no_leave = 15
print(Emp.no_leave)
