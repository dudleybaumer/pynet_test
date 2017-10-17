"""
Functions Ex1
--------------

a. Construct a function that has three parameters x, y, z
b. z has a default value of 20
c. Return x + y + z
d. Call this function using all three positional arguments
e. Call this function using named arguments x, y (let z be the default)
f. Call this function with one positional argument and two named arguments.
g. Call this function using three strings.
h. Call this function using three lists.
"""


def my_func(x, y, z=20):
  print (x + y + z)

my_func(3, 4, 1)
my_func(x=4, y=5)
my_func (3, y=5, z=1)
my_func(x="calling", y="a", z="stringcheese")

list1 = [1, 3]
list2 = [5, 1]
list3 = [10, 1]

my_func(list1, list2, list3)
