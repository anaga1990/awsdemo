a = 'hellow naga'
print(len(a))

# To check if a certain phrase or character is present in a string
print('na' in a)

if 'naga' in a:
    print("yes, 'naga' is present")

print(a[:])
print(a[7:])
print("*" * 20)
mystr = a[::-1]
print(mystr)

s1 = "i am new to python"
listOfData = s1.split()
print(listOfData)

s2 = "i:am:new to JAVA"
print(s2.split(":"))

s2 = "I am good at testing"
print(s2.split(" ", 2))

nan = "annabathina nagarjuna"
x = nan.startswith("anna")
print(x)
x = nan.endswith('una')
print(x)

df = "    xJNqsn xjsioS QSXQS  "
print(df)
x = df.strip()
print(x)

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

na = " axhah sascas hcs "
print(na.title())
print(na.swapcase())

print("Python String count() Method")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

print(txt.index('a'))
print(txt.find('a'))
