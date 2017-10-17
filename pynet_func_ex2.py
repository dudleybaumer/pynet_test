"""
Functions Ex2
--------------

Expand on functions exercise 1.

a. Create a list with three numbers
b. Use *args to call the function
c. Create a dictionary that has three keys of x, y, and z
d. Call the functions using **kwargs
"""
def my_func(x, y, z):
    print(x + y + z)

my_list = [1, 3, 5]
my_func(*my_list)

my_dict = {
  'x' : 7,
  'y' : 3,
  'z' : 1
}

my_func(**my_dict)
