"""
Classes Ex1
------------

Create a network device class. The class should have fields for
ip_addr, username, password, serial_number, model, vendor, uptime
and os_version.

Assign at least the ip_addr, username, and password field to the
object using __init__.

Create four different network device objects using this class
"""

from __future__ import print_function

class NetDevice (object):
    def __init__(self, ip_addr, username, pw, s_n="1234", model="4321", vendor="cisco", uptime="always", os_version="2.1"):
        self.ip_addr = ip_addr
        self.username = username
        self.pw = pw
        self.serial = s_n
        self.model = model
        self.vendor = vendor
        self.uptime = uptime
        self.os = os_version

my_obj1 = NetDevice(ip_addr='1.1.1.1', username= 'admin1', pw= 'password1')
my_obj2 = NetDevice(ip_addr='2.2.2.2', username= 'admin2', pw= 'password2')
my_obj3 = NetDevice(ip_addr='3.3.3.3', username= 'admin3', pw= 'password3')
my_obj4 = NetDevice(ip_addr='4.4.4.4', username= 'admin4', pw= 'password4')

print(my_obj1)
