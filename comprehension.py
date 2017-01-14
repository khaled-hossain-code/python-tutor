#list comprehension
numbers = range(10)
name = "khaled"
greet ="Hello how are you"

evenNum = [num for num in numbers if num % 2 == 0]
print evenNum
letters = [letter for letter in name]
print letters
words = [word for word in greet.split()]
print words
#list comprehension within a list comprehension
#square all the values of numbers and multiply by its own square
newNumbers = [x*x for x in [x**2 for x in numbers]]

print newNumbers