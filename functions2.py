#functions with a parameter with default value and return value
#def add(num1=0,num2=0): #It will assign the parameter value left to right by default
def add(num1=0,num2=0,*args):
    result=num1+num2
    result1 = num1*num2
    print("Num1 is : ",num1)
    print("Num2 is : ",num2)
    print("args is : ",args)
    print("sum: ",result)
    print("Multipilication: ", result1)
#add(20,2)
add(20,2)