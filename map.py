def square(x):
    return x**2

numbers = range(10)

#map takes a function and iterable, returns a new iterable applying the function on each element
squareNum = map(square,numbers)
print numbers
print squareNum

#the above can be achieved by lambda expression
lambdaSquare = map(lambda x:x**2,numbers)
print lambdaSquare

#map with multiple lists
a = [1,2,3]
b = [4,5,6] #len of both list has to be equal to do such kind of operation
#map( {lambda arg1,arg2: return arg1+arg2}, a as arg1, b as arg2 )
adder = map(lambda x,y:x+y,a,b) # adder = [ a[0]+b[0], a[2]+b[2], a[2]+b[2] ]
print adder