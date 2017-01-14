try:
    f = open("test1",'r')
except:
    print "File does not exist"
else:
    print "File is openned"
finally:
    print "Finally Close the file"


while True:
    try: 
        r = int(raw_input("Please Enter an Int: "))
    except:
        print "Incorrect, Please Try again"
        continue
    else:
        print "that's an Int"
        break
    
    print r