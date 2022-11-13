import random
import numpy as np

# print random flot from a range
a = random.random()
print(a)

b = random.uniform(1, 10)
print(b)

# print random output in a list
mylist = list("ABCDOUHIYED")
c = random.choice(mylist)
d = random.sample(mylist, 3)
print(c)
print(d)

# numpy
e = np.random.rand(3)
print(e)


