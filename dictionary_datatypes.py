#In Python dictionary is a mutable sequence created with grouping of objects but with unique
#It uses hashtable data structure
#It doesn't allow duplicate values
#It's unordered(It doesn't maintain the insertion order)
#Key in dictionary must be an immutable objects
#Custom objects, List objects, tuple(hashtable)-->but they must implement hash function
dict1={2:'Siva', 3:'Jothi'}
print("Dict1 Type: ",type(dict1))
print("Dict1 Value: ",dict1)
#Custom objects, List objects, tuple(hashtable)-->but they must implement hash function
dict2={2:'Siva', (42,3):'Jothi'}
#dict1={2:'Siva', {42,3}:'Jothi'}
#Set Not allowed
print("Dict1 Type: ",type(dict2))
print("Dict1 Value: ",dict2)
#Adding Email ID
dict3={2:'Siva', (42,3):'Jothi','email':'sivajothi@gmail.com','a':'Dharma'}
print(dict3.items())
print("Dict1 Type: ",type(dict3))
print("Dict1 Value: ",dict3)
#Overridding the values:
dict4={2:'Siva', (42,3):'Jothi',2:'SivaJothi','email':'sivajothi@gmail.com','a':'Dharma'}
print(dict4.items())
print("Dict1 Type: ",type(dict4))
print("Dict1 Value: ",dict4)
#Output: Dict1 Value:  {2: 'SivaJothi', (42, 3): 'Jothi', 'email': 'sivajothi@gmail.com', 'a': 'Dharma'}

#String(Str) is an immutable sequence of characters
#Str1='Siva'
#',"" Won't work, only '''(three single quotes work in the String)
Str1='''Siva
is a youtuber'''
print("Str1 type: ",type(Str1))
print("Str1 Value: ",Str1)
#Bytes: it's an immutable sequence of integer bytes
#Usage: It's for encoded String read/write, image, audio, Video examples
#It uses internally a fixed length array
#Each index value must be in the range of 0 to 255