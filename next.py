def sqrGen(n):
    for i in range(n):
        yield i**2

sqrFive = sqrGen(5)

print next(sqrFive)
print next(sqrFive)
print next(sqrFive)

name = "khaled" #name is iterable but not iterator, to make it a iterator we need to pass it within iter function

nameGen = iter(name)

print next(nameGen)
print next(nameGen)
print next(nameGen)
print next(nameGen)
