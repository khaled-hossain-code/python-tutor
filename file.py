f = open("test.txt") #this line opens a file called test.txt in present directory in read mode

#print f.read() #this line prints the first line of the test file and the cursor moves forward to next line

#f.seek(0) #this will take the cursor to 0 line of the file
#print f.read() 

#f.seek(3)
print f.readlines() #it returns all the lines in a list

