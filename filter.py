#filter only returns those numbers which condition returns True

series = range(10)

even = filter(lambda x: x%2==0, series)
print even

greaterThan3 = filter(lambda x: x>3,series)
print greaterThan3