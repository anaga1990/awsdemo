"""
for for String
"""
data = "i am in Python"
for a in data:
    print(a)

"""
for for LIST 
"""
names = ["naga", "venu", "lakshmi"]
print(names)
for name in names:
    if name == "naga":
        print(name.upper())
    print(name)

"""
for for Dictionary 
"""

map = {1: "naga", 2: "venu", 3: 'java'}
print(map)
for k in map:
    print(str(k) + " ==>" + str(map[k]))

print("^" * 30)
for k, v in map.items():
    print(k, v)
