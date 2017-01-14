def genCubes(n): #0x00312D240
    for x in range(n):
        yield x**3

threeCubes = genCubes(3)

print threeCubes #generator object gencubes at 0x0034CE480

for x in threeCubes:
    print x

def genFibo(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b

for num in genFibo(10):
    print num