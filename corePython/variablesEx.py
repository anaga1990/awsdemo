a = 10


def te(a):
    print('value of a =>' + str(a))
    a = 20
    print('value of a =>' + str(a))


print('value of a' + str(a))

te(10)

b = 30


def testdata():
    global b
    print('value of b =>' + str(b))

    print('value of b =>' + str(b))


print('value of b in outside of Method' + str(b))

testdata()
print("-" * 60)


def large_num(*args):
    print(max(args))

def smallet_num(*args):
    print(min(args))

print()

large_num(10, -3, 30, 303, -303, 404, -20, 305)
smallet_num(10, -3, 30, 303, -303, 404, -20, 305)