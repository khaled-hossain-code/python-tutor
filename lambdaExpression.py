def add(x,y): return x+y
print add(2,3)

#assigning to a variable mul, lambda then (x,y) argument list : return x*y, it creates an anonymous function
mul = lambda x,y: x*y
print mul(2,3)

even = lambda num: num%2==0
print even(4)