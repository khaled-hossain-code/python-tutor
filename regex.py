import re

pattern = ["term1","term2"]
text = "This is a text with term1, not with is the another term around"

print re.search("Hello",text)
#when no pattern is found None is returned

match = re.findall("is",text)
print match.start()