"""
RegEx Ex1
----------

1. Use the 'show interface fa4' output (in the file 'show_int_fa4.txt').

2. Use regular expressions extract the following:
    a. packets input/output
    b. bytes input/outputi
"""

from __future__ import print_function 
import re

with open("pynet_regex_ex1.txt") as f:
    output = f.read()

packets_in = re.search(r"(\d+) packets input, (\d+) bytes", output, flags=re.M)
packets_out = re.search(r"(\d+) packets output, (\d+) bytes", output, flags=re.M)

print (packets_in.group())
print (packets_out.group())


