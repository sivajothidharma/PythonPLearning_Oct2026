#Int
#Float
#Assignment
#

#5. Boolean Operators
#AND, OR, NOT
a=5
b=10
c=20
print("a greaterthan b :",a>b)
print("a Less than b :",a<b)
print("a is equal to b :",a==b)
print("a is not equal b :",a!=b)

#6. Membership Operator(in),(Not in)
search=input("Enter a string  to search:")
search=int(search) #Integer conversion
list1=[10,20,30,40,50]
if search in list1:
    print("The string is present in the list")
    print(search)
else:
    print("The string is not present in the list")
    print(search)

#7.Identity Operator(is)
a='siva'
print("ID of a is :",id(a))
b=input()
print("ID of b is :",id(b))
c=input()
print("ID of c is :",id(c))
print(a is b)

#Bitwise Operator:
#Bitwise Complement
#AND
#XOR
#NOT
#Uniary
