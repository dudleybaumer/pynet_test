"""
Dict Ex1
---------

a. Create a dictionary representing a network device
b. Assign it an ip address, a username, a password, a vendor, and a model 
   field.
c. Loop over this dictionary printing out all of the keys, and values
d. Update the password to be a new value
e. Add a secret field to the dictionary
f. Use the .get() method to try to retrieve a non-existent ‘device_type’ 
   field. Return a default value of ‘cisco_ios’ when the .get() key lookup 
   fails.
"""


net_device = {'ip addr' : '2.2.2.2', 'username' : 'ac', 'password' : 'hippolover5', 'vendor' : 'cisco', 'model' : 'F5NENGL'}

for key, value in net_device.items():
    print (key, value)

net_device['password'] = 'bashful5'

for key, value in net_device.items():
    print (key, value)

net_device['secret field'] =  'MagicDemons'

for key, value in net_device.items():
    print (key, value)

device_type = net_device.get('device_type', 'cisco_ios')
print (device_type)
