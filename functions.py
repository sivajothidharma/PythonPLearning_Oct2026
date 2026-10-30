#Functions: It's a set of instructions to perform some task. it's resuable code.
#Types:
#1.Build-in functions: Functions from library like print, id,..etc
#2.User defined functions
#Properies of Functions:
#1.Functions are objects
#2.Functions can be stored into a variable
#3.You can pass function as parameters
'''def add():
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    result=num1+num2
    print("Sum of the two numbers: ",result)
add() #Executes the function'''
#------------
def add(num1,,num2):
    result=num1+num2
    return result
result1=add(num1: 10,num2: 5)
print("Sum of the two numbers: ",result1)

