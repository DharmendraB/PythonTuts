print("Jai Mataji \nI can do it")
# Example of set use
s = set()
print(type(s))
# Add value in set
s.add(1)
s.add(2)
s1=s.union({1,2,3,4,})

print(s,s1)
s2=s.intersection({1,2,3})
print(s,s2)
s.remove(2)
print(s)
