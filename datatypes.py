#Various Data types in Python
#1. Integer
#1.1 Decimal Literals(0 to 9)
from unittest import result

a=12233446558685609970976997876765984576856587
print(a)
print(type(a))
print("a: ",a)
#1.2 Binary Literals(0-1)
#Here 0b represents Binary format
b=0b1011111110
print("b: ",b)
print("Type b is: ",type(b))
#1.3 Octal Literals(0-7)
#Here 0o is Octal format
c=0o1230347
print("c: ",c)
print("Type c is: ",type(c))
#1.4 Hexadecimal Literals(0-9, A-F)
d=0x1323424ADF
print("d: ",d)
print("Type d is: ",type(d))
#--------------------

#2. Floating type: Any decimal called floating type
A=10.0
print("A: ",A)
print("Type A is: ",type(A))
#B=1.25e2 #scientific Notation
#B=1.25e309 #maximum limit is e309
B=1.12533345456677689656775456 #Maximum 15 characters or  8bytes
print("B: ",B)
print("Type B is: ",type(B))
#--------------------------

#3.Complex Number(Real + Imaginary)
a=2+3j
print("a: ",a)
print("Type a is: ",type(a))
b=2.5+3j
print("b: ",b)
print("Type b is: ",type(b))
print(a+b)
#---------------------------------

#4.Boolean(class <bool>)
a=5
b=10
c=a>b
print("c: ",c)
print("Type c is: ",type(c))
c=a<b
print("c: ",c)
print("Type c is: ",type(c))
c=a>=b
print("c: ",c)
print("Type c is: ",type(c))
#------------------------------
#5. NoneType
import re
str1='man watt mat can van '
reg=r'm\w\w'
#reg=r'man*' to find the entire word
result=re.match(reg,str1)
print("result: ",result)
if result:
    print("result: ",result.group())
else:
    print("result:No match found ",result)
#------------------------------------------

#6.Sequence: It's a group of objects(any built-in/custom)
#Sequence(list, tuple, set, dict(dictionary), str(string(sequence of characters) bytes, bytearray)
#Classification of Sequence types:
#1.Mutable: Modification of objects/sequences-->list,set, dict,bytearray
#2.Immutable: No Modification of objects/sequences-->Tuple, Str, bytes
#6.1 List: It's a mutable sequence of objects.
#It internally uses a dynamic array to store the objects
# It Allows duplicate
# Maintains insertion order
#Example: Storing name of Employee
#List Syntax List=[]
List1=[10, "SivaJothi",20.2]
print("Value of List1: ",List1)
print("Type List1 is: ",type(List1))
List1.append(29)
print("Value of List1: ",List1)
#------------------------
#6.2 Tuple: It's a Immutable sequence of objects
# It Internally uses a fixed length array to store the objects
#It allows duplicate objects
#Maintains insertion order
#Examples: Storing name of Employee
tuple1=(11,"SivaJothi",20.2)
print("Value of tuple1: ",tuple1)
print("Type tuple is: ",type(tuple1))
#tuple1[0]=13--> It's not possible to modify the values. It's Immutable
print("Value of tuple1: ",tuple1)
#----------------------

#6.3 Set: It's a mutable, sequence of objects
#It's internally uses a hashtable(does not allow duplicate values) to store the objects
#Does not allow duplicate values
#Doesn't maintain the insertion orders
#Examples: Storing the session of users, transactional data
#What is Hashtable?: It's derived data structure that internally store the objects
# in an array of specific capacity that is known as bucket.
#How the index position of object is calculated?
#the index is calculated through Hash function
#Each hash function has the some algorithm to clculate the index(for example: Remainder theorem)
#Remainder theorem:
#bucket size=10, an element 100 is going to be stored
#100/10=0--Index Position is 0, now 100 will be stored in index position 0
#1000/10=0 index 0
#put all collision elements as linked list on that index
#In case of python, the set is internally using the hash function which has a default
#Implementation to take an object id(memory address) as unique value to represent indes()
a=3
b=12
c=5
print("ID of a: ",id(a))
print("ID of b: ",id(b))
set1={a,b,c}
print("set of a: ",set1)
print("Type set is: ",type(set1))
#-------------------------