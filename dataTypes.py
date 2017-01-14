#list are arrays of JS
list1 = ['a',1]
print list1
list2= list()
list2.append("hello")
list2.append("world")
print list2
    
    #list comprehension
capitals = [x.upper() for x in list2]
print capitals
#dictionaries are objects of JS
dict1 = {'a':1,'b':2,'c':3}
print dict1
    #dictionary comprehension
squres = {k:v**2 for k,v in dict1.items()}
print squres
keys = {k for k in dict1.keys()} #creating a set from dictionary keys
print keys
dict2 = dict()
print dict2
#tuples
tuple1 = ("khaled",32,"Software Engineer")
print tuple1
tuple2 = tuple([1,2,3,'jump'])
print tuple2
#sets are combination of unique value, which helps in union , intersection
set1 = {'a','b','c'}
set1.add('z')
print set1
set2 = {'c','d','e'}
set2.discard('c')
print set2
    #set comprehension
codes = {ord(x) for x in set2}
print codes