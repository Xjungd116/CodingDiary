# While Loops
### About while loops:
1. a structure allow to loop through and execute a black of code multiple times.
```Shell
# example

i = 1
while i <= 5:
    print(i)
    i += 1
    # a += b: add b value to a

print("Done with loop")
```
Run file:
```Shell
1
2
3
4
5
Done with loop
```

# For Loops
### About for loops:
1. Allow loop over a different collections of items
```Shell
for number in range(3, 10):
    print(number)

friends = ["Kat", "Jin", "Kevin"]
for index in range(len(friends)):
    print(friends[2])


friends = ["Kat", "Jin", "Kevin"]
for index in range(5):
    if index == 0:
        print("first interation")
    else:
        print("Not first")
```
Run file:
```Shell
3
4
5
6
7
8
9
Kevin
Kevin
Kevin
first interation
Not first
Not first
Not first
Not first
```

# Nasted Loops
