"""
Loops Ex1
1.  Create a list containing the values 1-49
2.  Loop over this list, printing each value
3.  Use continue to skip over 13 (not print it)
4.  Break when you hit 39 (stop printing after this and exit the loop)
"""

my_list = list(range(1,50))

for x in my_list:
    if x == 13:
        continue
    print(x)
    if x == 39:
        break
