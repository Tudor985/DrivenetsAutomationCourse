# vlan, ipv4, ipv6 = 0, 0, 0
# device_IP = 1
# print ("\r")
#
# for x in range(1,41):
#   hex_x_value = hex(x).split('x')[-1]
#   print ("interface ge100-0/0/{}".format(x))
#   print ("admin-state enabled")
#   print ("fec rs-fec-528-514")
#   print ("access-list ipv4 acl-ipv4 direction in")
#   print ("access-list ipv6 acl-ipv6 direction in")
#   print ("ipv4-address 156.{}.{}.{}/24".format(x, x, device_IP))
#   print ("ipv6-address 156:{}:{}::{}/64".format(x, hex_x_value, device_IP))
#   print ("vlan-id {}".format(x))
#   print ("top")
# vlan = 0
# for x in range(1, 3):
#   for y in range(1, 251):
#     vlan1 = vlan + y
#     print("interface ge100-0/0/1.{}".format(vlan1))
#     print ("ipv4-address 199.{}.{}.2/24".format(x, y))
#     print ("ipv6-address 199:{}:{}::2/64".format(x, y))
#     print ("vlan-id {}".format(vlan1))
#     print ("top")
#   vlan += 250
# for x in range(1,133):
#   print ("interface ge100-0/0/0.{}".format(x))
#   # print ("admin-state enabled")
#   print ("admin-state enabled")
#   print ("top")
# loopback = 0
# for x in range(1, 13):  # loopback addresses
#   for y in range(1, 251):
#     loopback1 = loopback + y
#     print("interface lo{}".format(loopback1))
# print ("ipv4-address 133.{}.{}.133/32".format(x, y))
# print ("ipv6-address 133:{}:{}::133/128".format(x, y))
# print ("admin-state disabled")
# print ("admin-state enabled")
# print ("top")
# loopback += 250
# for x in range(1066, 4066):
#   print("no interfaces ge100-0/0/3.{}".format(x))
# protocols
#   bgp 111
#     router-id 111.111.111.111
# for x in range(1, 5):
#   for y in range(1, 251):
#     print ( '''
#     neighbor 199.{}.{}.1
#       remote-as 50001
#       description eBGP
#       bfd
#         admin-state enabled
#         min-rx 50
#         min-tx 50
#         multiplier 3
#       !
#       address-family ipv4-unicast
#         maximum-prefix 1500 threshold 80
#         remove-private-as
#         soft-reconfiguration inbound
#       !
#     !
#     '''.format(x, y))
# vlan = 0
# for x in range(1, 3):
#   for y in range(1, 251):
#     print ("ipv4-address 199.{}.{}.2/24".format(x, y))
#     print ("ipv6-address 199:{}:{}::2/64".format(x, y))
#     print ("vlan-id {}".format(vlan1))
#     print ("top")
#   vlan += 250
# for x in range(250, 301):
#     print("no interface ge100-0/0/1.{}".format(x))
# print ("network-type point-to-point")
# print ("!")
# for x in range(3, 41):
#     print("interface ge100-0/0/{} admin-state enabled".format(x))
# ============================
# Silviu ACL
#
# vlan, ipv4, ipv6 = 0, 0, 0
#
# vlan = 0
# for x in range(1, 101):
#   vlan1 = vlan + x
#   hex_x_value = hex(x).split('x')[-1]
#   print("interface ge100-0/0/0.{}".format(vlan1))
#   print ("ipv4-address 100.{}.0.1/24".format(x))
#   print ("ipv6-address 100:{}:0::1/64".format(hex_x_value))
#   print ("vlan-id {}".format(vlan1))
#   print ("top")
#
#
#
# for x in range (1, 101):
#   # hex_x_value = hex(x).split('x')[-1]
#   print ("access-lists ipv4 acl-ipv4_{}".format(x))
#   for y in range(1, 251):
#     print("rule {} allow dest-ip 155.1.{}.0/24".format(y, y))
#   for z in range(251, 501):
#     t = z - 250
#     print("rule {} allow dest-ip 155.2.{}.0/24".format(z, t))
#   print ("top")
#
#
#
# for x in range(1, 100):
#   vlan1 = vlan + x
#   print("interface ge100-0/0/0.{}".format(x))
#   print ("access-list ipv4 acl-ipv4_1 direction in".format(x))
#   print ("top")
# for x in range(1, 100):
#     as_bgp = 55000
#     as_bgp = as_bgp + x
#     print ("neighbor 100.{}.0.2 remote-as {} address-family ipv4-unicast".format(x, as_bgp))
#     print ("!")
#     print ("!")
# for x in range(1, 101):
#   print ("protocols ospf area 0 interface ge100-0/0/0.{} network-type point-to-point".format(x))
#
#
# neighbor 100.1.0.2 remote-as 101 address-family ipv4-unicast
#   print("rule {} allow protocol tcp(0x06) src-ports {}".format(x,srcport))
#   # print ("ipv4-address 156.{}.{}.{}/24".format(x, x, device_IP))
#   # print ("ipv6-address 156:{}:{}::{}/64".format(x, hex_x_value, device_IP))
#   # print ("vlan-id {}".format(x))
#   # print ("top")
# print ("access-lists ipv4 acl-ipv4 rule 2000 deny")


# Subinterfete

# vlan, ipv4, ipv6 = 0, 0, 0
# for x in range(1, 256):
#   vlan1 = vlan + x
#   hex_xv_alue = hex(x).split('x')[-1]
#   print(f"interface ge100-0/0/12.{vlan1}")
#   print ("admin-state enabled")
#   print (f"ipv4-address 100.{x}.0.2/24")
#   print (f"ipv6-address 100:{hex_xv_alue}::2/64")
#   print (f"vlan-id {vlan1}")
#   print ("top")
#
# index_octet = 0
#
#
# for x in range(257, 512):
#   vlan1 = vlan + x
#   index_octet += 1
#   hex_xv_alue = hex(x).split('x')[-1]
#   print(f"interface ge100-0/0/12.{vlan1}")
#   print ("admin-state enabled")
#   print (f"ipv4-address 101.{index_octet}.0.2/24")
#   print (f"ipv6-address 100:{hex_xv_alue}::2/64")
#   print (f"vlan-id {vlan1}")
#   print ("top")


# for session_id in range (1, 5):
#     for y in range (1, 10):
#         print(f'services port-mirroring session Tudor{session_id} destination-interface ge100-0/0/19 source-interface bundle-{y}')
#
#
# def create_Port_Mirroring(sessionID, min, max):
#   for x in range(min, max):
#     print("services port-mirroring session ",sessionID, f"destination-interface ge100-0/0/19 source-interface bundle-{x}")
#
# create_Port_Mirroring('Tudor1',1,11)
#
#


# BGP

# vlan, ipv4, ipv6 = 0, 0, 0
# for x in range(1, 256):
#   vlan1 = vlan + x
#   print(f"protocols")
#   print(f"bgp 65000")
#   print(f"address-family ipv4-unicast")
#   print(f"exit")
#   print(f"neighbor 110.1.0.{x}")
#   print(f"address-family ipv4-unicast")
#   print(f"labeled-unicast")
#   print(f"exit")
#   print(f"remote-as 65000")
#   print(f"description TO_IXIA1")
#   print(f"update-source ge100-0/0/12.{vlan1}")
#   print(f"top")


# vlan, ipv4, ipv6 = 0, 0, 0
# for x in range(1, 9):
#   for vlan1 in range(1, 11):
#     print(f"interface ge100-0/0/{x}.{vlan1}")
#     print ("admin-state enabled")
#     print (f"vlan-id {vlan1}")
#     print ("top")
#

#
# for vlan1 in range(1, 11):
#     print(f"services port-mirroring session Tudor1 destination-interface ge100-0/0/19 source-interface ge100-0/0/1.{vlan1}")
#     print(f"services port-mirroring session Tudor2 destination-interface ge100-0/0/20 source-interface ge100-0/0/2.{vlan1}")
#     print(f"services port-mirroring session Tudor3 destination-interface ge100-0/0/21 source-interface ge100-0/0/3.{vlan1}")
#     print(f"services port-mirroring session Tudor4 destination-interface ge100-0/0/22 source-interface ge100-0/0/4.{vlan1}")
#     print(f"services port-mirroring session Tudor5 destination-interface ge100-0/0/23 source-interface ge100-0/0/5.{vlan1}")
#     print(f"services port-mirroring session Tudor6 destination-interface ge100-0/0/24 source-interface ge100-0/0/6.{vlan1}")
#     print(f"services port-mirroring session Tudor7 destination-interface ge100-0/0/25 source-interface ge100-0/0/7.{vlan1}")
#     print(f"services port-mirroring session Tudor8 destination-interface ge100-0/0/26 source-interface ge100-0/0/8.{vlan1}")
#     print(f"services port-mirroring session Tudor9 destination-interface ge100-0/0/27 source-interface ge100-0/0/9.{vlan1}")

#
# import random
# import socket
# import struct
# def configure_embedded_acl(min, max, embedded_acl):
#     for x in range (min, max):
#         print(f'access-lists ipv4 Test_ACL_{x} embed-acl {embedded_acl}')
# def configure_acl_rule(min, max, acl, deny=None, allow=None):
#     for x in range (min, max):
#         if deny is not None:
#             print (f'access-lists ipv4 {acl} rule {x} deny')
#         elif allow is not None:
#             print(f'access-lists ipv4 {acl} rule {x} deny')
# def create_dscp_rules():
#     for x in range(101, 116):
#         dscp_value = random.randint(1, 64)
#         print(f'access-lists ipv4 embedded_acl_ipv4 rule {x} {random.choice(acl_list_type)} dscp {dscp_value}')
# # configure_embedded_acl(0, 100, 'EMBEDDED_ACL_IPV4_2')
# #  configure_acl_rule(min=0, max=2001, acl='TESC_SCALE_ACL', allow=True)
# acl_list_type = ['allow', 'deny']
# for x in range(150, 250):
#     ip_address_random = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
#     ip_address_random_2 = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
#     random_type = random.choice(acl_list_type)
#     print(f'access-lists ipv4 embedded_acl_ipv4 rule {x} {random_type} src-ip {ip_address_random}/32 dest-ip {ip_address_random_2}/32  ')
#
#


##Read lines in txt files:

# f = open('country.txt', 'r')
# print(f.read())
# f.close()
#
# f = open('country.txt', 'r')
# print(f.read(100))
# f.close()
#
# f = open('country.txt', 'r')
# print('1:', f.readline())
# print('2:', f.readline())
# print('3:', f.readline())
# f.close()
#
#
# f = open('country.txt', 'r')
# print('1:', f.readline(), end='')
# print('2:', f.readline(), end='')
# print('3:', f.readline(), end='')
# f.close()
#
# f = open('country.txt', 'r')
# print(f.read().splitlines())
# f.close()

# f = open('country.txt', 'r')
# print(f.readlines())
# f.close()
#
# f = open('country.txt', 'r')
# for line in f:
#     print(line, end='')
# f.close()
#


##Writing/Reading/Append to files in python:

# with open('new_file.txt', 'w') as f:
#     f.write('This is our first line\n')
#     f.writelines(['1', '2', '3'])
#
#
# with open('new_file.txt', 'r') as f:
#     print(f.read())


# with open('new_file.txt', 'w') as f:
#     f.write('This is our first line\n')
#     f.writelines(['1\n', '2\n', '3\n'])
#
# with open('new_file.txt', 'r') as f:
#     print(f.read())


# with open('new_file.txt', 'w') as f:  #<<<---- write
#     f.write('This is our first line\n')
#     f.writelines(['1\n', '2\n', '3\n'])
#
# with open('new_file.txt', 'a') as f:   #<<<---- append
#     f.write('This is our second write\n')
#     f.writelines(['1\n', '2\n', '3\n'])
#
# with open('new_file.txt', 'r') as f:   #<<<---- read
#     print(f.read())

##A simple tail -f in Python

# with open('new_file.txt', 'r') as f:   #<<<---- read
#     print(f.readline(), f.tell(), sep='')
#     print(f.readline(), f.tell(), sep='')
#     print(f.readline(), f.tell(), sep='')
#     print(f.readline(), f.tell(), sep='')
#
# len('This is our first line\n')
#
# with open('new_file.txt', 'r') as f:
#     f.seek(0)
#     print(f.readline(), end ='')
#     f.seek(0)
#     print(f.readline(), end ='')
#     f.seek(0)
#     print(f.readline(), end ='')
#
# with open('new_file.txt', 'r') as f:
#     f.seek(29)
#     print(f.readline(), end ='')
#     f.seek(29)
#     print(f.readline(), end ='')
#     f.seek(29)
#     print(f.readline(), end ='')


# import pickle
#
# complex_obj = {1:[1, 's',4.5], 'a':{7,3,'a'}, 9.9:{1:'a', 'b':2, 'c':6}}
# print(complex_obj)
#
# with open('obj.pkl', 'wb') as f:
#     pickle.dump(complex_obj, f)
#

##Functions

# def append_val(val, lst):
#     lst.append(val)
#
# my_lst = [1,2,3]
# append_val(4,my_lst)
# print(my_lst)


##Global Variables

# a = 1  #<<<--- Global variable
# def func(b):
#     print(a,b)
#
# func(4)
#
#
# a = 1   #<<<--- Global variable
#
# def func(b):
#     c = a * b  #Local variable - Local to the function
#     print(a, b, c)
#
# func(4)


# a = 1   #<<<--- Global variable
#
# def func(b):
#     a = 2  #Local variable - Local to the function
#     print(a, b)
#
# func(4)
# print(a) #<<-- prints Global variable
#


# a = 1   #<<<--- Global variable
#
# def func(b):
#     a += 2  #not possible to change local variable: incearca sa adauge 2 la Global 'a' ( Local 'a' pointeaza catre obiectul global)
#     print(a, b)
#
# func(4)
# print(a)


# a = 1   #<<<--- Global variable
#
# def func(b):
#     a = 1
#     a += 2  #Posibil pentru ca pointeaza catre o alta variabila Locala: 'a = 1 + 2' iar 'b = 4'
#     print(a, b)
#
# func(4)
# print(a)


# a = 2 #<<<--- Global variable

# def func(a, b):
#     a += 2
#     print(a, b)
#     return a
# a = func(a, 4)
# print(a)


## ARGs

## sum_integers_list.py

# def my_sum(my_integers):
#     result = 0
#     for x in my_integers:
#         result += x
#     return result
#
# list_of_integers = [1, 2, 3]
# print(my_sum(list_of_integers))

##This implementation works, but whenever you call this function you’ll also need to create a list of arguments to pass to it.
##This can be inconvenient, especially if you don’t know up front all the values that should go into the list.

##This is where *args can be really useful, because it allows you to pass a varying number of positional arguments. Take the following example:

## sum_integers_args.py

# def my_sum(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         result += x
#     for y in args:
#         result += y
#     return result
#
# print(my_sum(1, 2, 3))

##In this example, you’re no longer passing a list to my_sum().
## Instead, you’re passing three different positional arguments. my_sum() takes all the parameters that are provided in the input and packs them all into a single iterable object named args.
##Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer, such as integers:

# Lists

## Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a tuple.
## A tuple is similar to a list in that they both support slicing and iteration.
## However, tuples are very different in at least one aspect: lists are mutable, while tuples are not. To test this, run the following code.
##This script tries to change a value of a list:

##The value located at the very first index of the list should be updated to 9.
##If you execute this script, you will see that the list indeed gets modified:

# change_list.py
# my_list = [1, 2, 3]
# my_list[0] = 9
# print(my_list)

# Tuples

## Here, you see the same values, except they’re held together as a tuple.
## If you try to execute this script, you will see that the Python interpreter returns an error:
## This is because a tuple is an immutable object, and its values cannot be changed after assignment.
## Keep this in mind when you’re working with tuples and *args.

# # change_tuple.py
# my_tuple = (1, 2, 3)
# my_tuple[0] = 9
# print(my_tuple)


# def my_sum(a=0,b=0,c=0):
#     return a + b + c
# print(my_sum(1,2,3))
# print(my_sum(1))


# class MyClass:
#     class_counter = 0
#     def __init__(self, class_name, class_type):
#         self.class_name = class_name
#         self.class_type = class_type
#         self.class_id = MyClass.class_counter
#         MyClass.class_counter += 1
#         self.students = []
#
#         def append_student(self, student):
#             self.students.append(student)
#
#         def extend_students(self, students):
#             self.students.append(student)
#
#         def remove_student(self, student):
#             if student in self.students:
#                 self.students.remove(student)
#
#         def __print_student(idx, student):
#             print('\t', idx, '. ', student, sep='')
#
#         def print_class(self):
#             print('ClassName:', self.class_name)
#             print('Class Type:', self.class_type)
#             print('Class ID:', self.class_id)
#             print('Students')
#             [MyClass.print_student(idx, student) for idx, student in enumerate(self.students)]
#
#         MyClass
#         __main__.Myclass
#         c1 = MyClass('class_1', 'Python')
#         c2 = MyClass('class_2,', 'OO')
#         c1.extend_students(['Ofir', 'Yoni', 'Tudor'])
#

# stein = 1
# pint = 1
#
# stein += pint
# stein = stein + pint
#
# print(stein)
#
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
#
# f = 6
#
# a += b
# c -= d
# e %= f
# print(a)
# print(c)
# print(e)
#
# a = 'Hello'
# b = ' World'
# c = '!'
# a += b + c
# print(a)
#
#
# import sys
# count = 'alpha'
# print("Size of count", sys.getsizeof(count), "bytes")
# print("Size of str(count)", sys.getsizeof(str(count)),"bytes")
#
# list_cheese = ['Cheddar', 'Stilton', 'Cornish']
# list_cheese[1] = 'De oaie'
# print(list_cheese)
# list_cheese.append('De capra')
# print(list_cheese)
# list_cheese.extend(['De vaca', 'De bivolita'])
# print(list_cheese)
#
#
#
# tupple_cheese = 'Cheddar1', 'Stilton1', 'Cornish1'
# print(tupple_cheese)
#
#
#
#
# mydict = {'Bucuresti': 'Sector3', 'Ilfov': 'Chiajna', 'Giurgiu': 'Bolintin-Deal'}
# print(mydict['Ilfov'])
#
# country = 'Romania'
# mydict[country] = 'Cluj'
# print(mydict[country])
#
# mydict = dict(Sweden='Stockholm', Norway='Oslo')
# print(mydict['Norway'])
#
#
#
#
# x=2
# y = x/3
# z = x//3
#
# print(y)  #gives 0.666666666667 <<-- "/" divide
# print(z)  #gives 0 <<-- "//" integer divide
#
#
#
# #Conditionals
#
# lista = 4
# listb = 4
# if lista == listb:
#     print("Same!")


# The comparison operator == is overloaded for different classes, and compares the values of two objects.
# If you wish to test if two variables refer to the same object, use "is".

# lista = 4
# listb = 4
# if lista is listb:
#     print("Same!")
#
#
#
# lang = ['Perl', 'Python', 'PHP', 'Ruby']
# if 'Python' in lang:
#     print('Python is in lang')
# else:
#     print('Python is not in lang')
#
#
#
# string_lang = "We luv Python"
# if 'Python' in string_lang:
#     print ("Python is in string_lang")
# else:
#     print('Python is not in string_lang')
#
# dict_lang = {'Perl':'sigils', 'Python':'indentation','PHP' :'functions', 'Ruby' :'Rails'}
# if 'Python' in dict_lang:
#     print ("Python is in dict_lang: " + dict_lang['Python'])
# else:
#     print('Python is not in dict_lang')
#
#
#
#
#
#
# lang = ['Perl', 'Java', 'PHP', 'Ruby']
# if 'Python' in lang:
#     print('Python is in lang')
# else:
#     print('Python is not in lang')
#
#
# string_lang = 'We luv Java'
# if 'Python' in string_lang:
#     print ('Python is in string_lang')
# else:
#     print('Python is not in string_lang')
#
#
# dict_lang = {'Perl':'sigils', 'Java':'indentation','PHP' :'functions', 'Ruby' :'Rails'}
# if 'Python' in dict_lang:
#     print ("Python is in dict_lang: " + dict_lang['Python'])
# else:
#     print('Python is not in dict_lang')
#
#
#
# distance = 15
# if 0 < 2 < 42 and distance != 20:
#     print('Distance to long!')
# else:
#     print('Distance to short')
#
#
# num = 42
# txt = '3'
# if int(txt) < num:
#     print('Wow!')
#


#While loops - Loop while a condition is true

# #Equality operator (==)
# line = 'done'
# while line == 'done':
#     line = input('Type"done" to complete:')
#     print('<', line, '>')
#     break  #<<-- pentru ca altfel este un endless loop
#
# #Inequality operator (!=)
#
# line = None
# while line != 'done':
#     line = input('Type"done" to complete:')
#     print('<', line, '>')



# myl = [23, 67, 32, 9, 77]
# while myl:
#     print(myl.pop() * 2)  # pop() on a list removes and returns the last item ( 77 x 2, 9 x 2, etc.)
#
#
# i = 1
# j = 120
# while i < 42:
#     i = i * 2
#     if i > j: break
# else:
#     print('Loop expired:',i)
# print('Final value:',i)
#
#
# # For Loops - iterate trough a sequence - often a list or tuple
#
#
# farms = ['Home Farm', 'Mocky', 'Scales End', 'Brown sugar']
# squirls = [43, 51, 44, 2]
# rabbits = [2, 6, 9 ,8]
# moles = [12, 8, 13, 44]
#
# for f, s, r, m in zip(farms, squirls, rabbits, moles):
#     print('Total for', f, ':', s + r + m)





## Config Scale 2000 L2vpn over same policy of SR-TE (DN + Juniper)

# for x in range(1102, 3102):
#     print ("network-services vpws instance vpws_{}".format(x))
#     print ("description TO_Juniper interface ge100-0/0/18.{}".format(x))
#     print ("pw 11.11.11.11 sr-te policy pol1 admin-state enabled ignore-mtu-mismatch enabled pw-id {}".format(x))
#     print ("top")

# for x in range(1102,3102):
#   print ("interface ge100-0/0/18.{}".format(x))
#   print ("admin-state enabled")
#   print(" l2-service enabled")
#   print ("vlan-id {}".format(x))
#   print ("top")

# for x in range(1102,2102):
#     print ("set interfaces ge-0/0/0 unit {} enable".format(x))
#     print ("set interfaces ge-0/0/0 unit {} encapsulation vlan-ccc".format(x))
#     print ("set interfaces ge-0/0/0 unit {} vlan-id {}".format(x, x))
#     print ("set interfaces ge-0/0/0 unit {} family ccc".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} virtual-circuit-id {}".format(x, x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} mtu 1514".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} ignore-encapsulation-mismatch".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} ignore-mtu-mismatch".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} pseudowire-status-tlv".format(x))



# for x in range(2102,3102):
#     print ("set interfaces ge-0/0/0 unit {} enable".format(x))
#     print ("set interfaces ge-0/0/0 unit {} encapsulation vlan-ccc".format(x))
#     print ("set interfaces ge-0/0/0 unit {} vlan-id {}".format(x, x))
#     print ("set interfaces ge-0/0/0 unit {} family ccc".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} virtual-circuit-id {}".format(x, x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} mtu 1514".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} ignore-encapsulation-mismatch".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} ignore-mtu-mismatch".format(x))
#     print ("set protocols l2circuit neighbor 44.44.44.44 interface ge-0/0/0.{} pseudowire-status-tlv".format(x))



# print(list(filter(lambda x: not x.startswith("__"), dir(set))))
# print(list(filter(lambda x: not x.startswith("__"), dir(list))))
# print(list(filter(lambda x: not x.startswith("__"), dir(tuple))))
# help(tuple)

import requests

# f = open("frankenstein.txt", "wb")
# r = requests.get("https://www.gutenberg.org/cache/epub/84/pg84.txt")
# r = requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt%22")
# f.write(r.content)
# f.close()

# frankenstein = ("https://www.gutenberg.org/cache/epub/84/pg84.txt")
# dracula = ("https://www.gutenberg.org/cache/epub/345/pg345.txt%22")
#
# def save_local_copy(book_url, book_name):
#     """
#     Count all words
#     :param book:
#     :return:
#     """
#     r = requests.get(book_url)
#     f = open(book_name, "wb")
#     f.write(r.content)
#     f.close()
#



# num1 = 90
# num2 = 30
# print('{0:.2f}%'.format((num2 / num1 * 100)))

#Prima Varianta ( input intotdeauna urmeaza un string si atunci variabilele trebuie definite ca integer )

# x = input("Numarul de teste ramase: ")
# y = input("Numarul de teste efectuate: ")
# z = input("Numarul total de teste: ")
#
#
# # calculating %
#
# P1 = (int(x) / int(z)) * 100
# P2 = (int(y) / int(z)) * 100
# print(P1, P2)

#A doua varianta ( fara input si cu variabilele definite ca integer )

# x = 6
# y = 49
# z = 55
#
#
# # calculating %
#
# P1 = (x / z) * 100
# P2 = (y / z) * 100
# print(P1, P2)

#A treia varianta ( fara input si cu variabilele definite ca integer si procentaj cu 2 zecimale )

# x = 6
# y = 49
# z = 55
#
#
# # calculating %
#
# P1 = '{0:.2f}%'.format((x / z) * 100)
# P2 = '{0:.2f}%'.format((y / z) * 100)
# print(f"{P1} - Procentaj ramas de executat")
# print(f"{P2} - Procentaj executat")

#A patra varianta ( cu input si cu variabilele definite ca integer si procentaj cu 2 zecimale )


x = input("Numarul de teste ramase: ")
y = input("Numarul de teste efectuate: ")
z = input("Numarul total de teste: ")


# calculating %

P1 = (int(x) / int(z)) * 100
P2 = (int(y) / int(z)) * 100
format_percent1 = '{0:.2f}%'.format(P1)
format_percent2 = '{0:.2f}%'.format(P2)
print(f"{format_percent1} - Procentaj ramas de executat")
print(f"{format_percent2} - Procentaj executat")

##Decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

# def my_decorator(some_function):
#     def wrapper():
#         print("Something is happening before some_function() is called.")
#         some_function()
#         print("Something is happening after some_function() is called.")
#     return wrapper
#
# def just_some_function():
#     print("WoW!")
# just_some_function = my_decorator(just_some_function)
#
# just_some_function()



#pt leaf - vlan 760
#interface vxlan 1
#vxlan vlan add 760 vni 760

#vxlan vlan 760 flood vtep 10.40.188.40

#si pentru spine e fix acelasi config doar cu alt IP

#vxlan vlan 760  flood vtep 10.40.188.38 - pentru spine

# for color in range(0, 251):
#         print(f'policy To_R6_policy_{color}  admin-state enabled color {color} destination 66.66.66.66 spf path path_G priority 1 ')
#
# for color in range(251, 500):
#         print(f'policy To_R6_policy_{color}  admin-state enabled color {color} destination 66.66.66.66 spf path path_G priority 1 ')



# for destination in range(1, 256):
#         print(f'policy To_R6_policy_0  admin-state enabled color 0 destination 20.20.20.{destination} spf path path_A priority 1 ')


# for destination in range(0,251 ):
#        print(f'policy To_R6_policy_{destination}  admin-state enabled color 0 destination 6.6.7.{destination} spf path path_A priority 1 ')


# loopback = 0
# color = 0
# for x in range(4, 7):  # loopback addresses
#   for y in range(1, 251):
#     loopback1 = loopback + y
#     color1 = color + y
#     print(f'policy To_R6_policy_{loopback1}  admin-state enabled color {color1} destination 44.44.{x}.{y} spf path path_G priority 1 ')
#   loopback += 250
#   color += 250

# print("hello world")






# loopback = 0
# for x in range(6, 8):  # loopback addresses
#   for y in range(1, 256):
#     loopback1 = loopback + y
#     print("interface lo{}".format(loopback1))
#     print ("ipv4-address 44.44.{}.{}/32".format(x, y))
#     print("admin-state enabled")
#     print("top")
#   loopback += 250

# loopback = 3
# for x in range(4, 7):  # loopback addresses
#   for y in range(1, 256):
#     loopback1 = loopback + y
#     print("interface lo{}".format(loopback1))
#     print ("ipv4-address 44.44.{}.{}/32".format(x, y))
#     print("admin-state enabled")
#     print("top")
#   loopback += 250


# for x in range(4, 551):  # loopback addresses
#     print(f'interface lo{x}')
#     print("address-family ipv4-unicast")
#     print (f'prefix-sid index {x}')
#     print("!")
#     print("!")








# save_local_copy(dracula, "dracula.txt")


print(list(filter(lambda x: not x.startswith("__"), dir(dict))))

print(list(filter(lambda x: not x.startswith("__"), dir(list))))

print(list(filter(lambda x: not x.startswith("__"), dir(tuple))))
help(tuple.index)

l = [1, 2, 3, 4]
l.append(5)
l.append(6)
l[5] = 0
print(l)
print(len(l))
index = l.index(1)
print(index)

for v in l:
    print(f"value {v}, value{l[v::-1]}")

t = (1, 2, 3, 4)
t1 = (5, 6, 7)
t += t1
print(t)

catel = 1
d1 = {1: 1, 2: 2, 3: 3, 4:4, 6: 6}
d1[5] = 5
d1[1] = catel
print(d1)
print(len(d1))


for k in d1:
    print(f"key:{k}, value {d1[k]}")




