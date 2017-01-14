from collections import Counter

l = [1,1,1,2,2,2,3,3,3,4,4,44,4,5,55,5,5,5,55]
print Counter(l)

name = "asdfljfajsdfjlrenugopalAiar"
print Counter(name)

greet = "Hello EveryOne! How are you All. So How is your children. Stay Happy EveryOne!"
c = Counter(greet.split())
print c
print c.most_common(3) #most common first three words in all of these sentences
print c.most_common()[:-3:-1]# least common element from the last 2
print sum(c.values()) #14 means 14 words are in greet senstence
print list(c) #list all the keys means unique elements or words

