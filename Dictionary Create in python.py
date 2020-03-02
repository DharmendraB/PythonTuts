print("Jai Mataji \nI can do it")

# Dictionay is nothing but key value pairs

d1 = {}
#print(type(d1))

d2 ={"Gohil":"veg","Ashish":"NonVeg","Pratap":"FastFood",
     "JD":{"A":"Gujarati","B":"Hindi","C":"English"}}

print(d2)
print(d2["Gohil"])
print(d2["JD"]["A"])
d2["Ravat"]="All in one"
d2.update({"Ramesh":"All in One"})

d2[123]="Bapu"
print(d2)

del d2[123]
print(d2)
print(d2.get("Gohil"))

d3 = d2.copy()
del d2["Gohil"]
print(d3)

print(d2.keys())
print(d2.items())
