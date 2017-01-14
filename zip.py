a = [1,2,3,4,5]
b = [6,7,8,9,10]

print zip(a,b) #output [(1,6),(2,7),(3,8),(4,9),(5,10)]


num1 =[12,23,34,16,54]
num2 =[33,23,11,43,44]
#max =[33,23,34,43,54]
#find max from each pair of tuples of these two numbers
maxFromPair = map(lambda pair:max(pair), zip(num1,num2))
print maxFromPair

