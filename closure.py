def hello(name="khaled"):
    
    def greet():
        print "yo man!"+ name
    
    def salute():
        print "Good Morning,Sir! ,"+name

    if name=="khaled":
        return greet
    else:
        return salute

khaled = hello()
sabbir = hello("sabbir")

khaled()
sabbir()