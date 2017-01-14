def decorator(func):
    
    def wrapper_func():
        print "This is is before func execution"

        func()

        print "This line after func"
    
    return wrapper_func #0x003B0F828 when func passed to decorator()
                        #0x002C7F908 when func2 passed to decorator()

def func():
    print "I am a manually decorated"

func() #0x003B0F7B8
decoratedFunc = decorator(func)
decoratedFunc() #0x003B0F828
func = decoratedFunc #0x003B0F828
func()#this way manually decorator can be done

#@decorator means call decorator function and pass func2 into it and replace the returned function 
@decorator
def func2():
    print "I am automatically decorated"

func2() #0x002C7F908