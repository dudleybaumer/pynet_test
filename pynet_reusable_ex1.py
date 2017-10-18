"""

Reusable Code Ex1
------------------

1. Write a program with three functions (func1, func2, func3)
2. Use the if __name__ technique to separate the importable code from the executable code
3. Create a main() function and call it.
4. Execute the program from the command line. Verify main() function executes
5. Go into the Python shell and import the module. Verify main() function does NOT execute.
6. In the Python shell look at dir(), __name__, and module.__name__
7. Execute pylint on your code.
"""

from __future__ import print_function

def func1():
  print ("Hello World")

def func2():
    print ("Donkeys in Distress")

def fun3():
    print ("Galaxy Jack")

if __name__ == “__main__”:
  main()
