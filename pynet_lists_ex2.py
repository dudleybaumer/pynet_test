ip_addr = input("Enter IP Address: ")
ip_addr = ip_addr.split(".")
print (ip_addr)

ip_addr[-1] = 0
print(ip_addr)

my_bin = []
counter = 0

for item in ip_addr:
   my_bin.append(bin(int(ip_addr[counter])))
   counter = counter + 1

print(my_bin)
print(ip_addr)
