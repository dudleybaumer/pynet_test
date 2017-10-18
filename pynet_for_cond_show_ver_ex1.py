"""

Show Version Ex1
----------------

a. Read a show version output from a router (in a file)
b. Find the router serial number in the output
c. Parse the serial number and return it as a variable. Use .split() and substr in str to 
   accomplish this
"""

from __future__ import print_function

with open("show_version.txt") as f:
    var_1 = f.read().splitlines()

for line in var_1:
    if 'Processor Board ID' in line:
        _, serial_number = line.split("Processor board ID")

print("\nSerial Number is {}\n".format(serial_number))
