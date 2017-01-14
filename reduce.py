series = range(10)
#n1,n2,n3.....n9
#find n1+n2+n3+.....+n9
'''
1,2,3,4,5,6,7,8,9
1+2=3
3+3=6
6+4=10
10+5=15
15+6=21
21+7=28
28+8=36
36+9=45
'''
sum = reduce(lambda x,y:x+y,series)  #output 45
print sum

#find max
numbers = [23,234,555,234,654,23434,546565,78785646546]
maximum = reduce(lambda x,y:x if x>y else y, numbers)
print maximum