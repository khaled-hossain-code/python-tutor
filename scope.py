x = 20

def adder():
    x = 3
    print "first x = " + str(x)

def mul():
    global x
    x = 4;
    print "this is global x = " + str(x)

adder()
mul()
print "Global x is "+ str(x)