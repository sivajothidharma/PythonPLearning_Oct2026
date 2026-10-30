#Control flow statement
#1. DecisionMaking
#1.1 If ----- Statement
#1.2 If---Else Statement
#1.3 If----Else----Else Statement

#2.Looing Statement
#2.1 For...Loop
#2.2 For....else statement
#2.3 while... loop
#2.4 while...else...statement

#3.Branching the Statement
#3.1 Break
#3.2 Continue
#3.3 Pass the statement

#IF
'''a=int(input("Number A: "))
#Check the numbers are even or not
if a%2==0:
    print(a,"Number is even")

#IF...Else
#a=int(input("Number A: "))
#Check the numbers are even or not
    if a%2==0:
      print(a,"Number is even")
    else:
      print(a,"Number is odd")
else:
    print(a,"Number is not valid")'''
#-----------
#Greatest of 3number

'''b=int(input("Number B: "))
c=int(input("Number C: "))
if a>b and a>c:
    print(a,"Number is greater")
elif b>c:
    print(b,"Number is greater")
else:
    print(c,"Number is greater")'''
#----------------------
#looping Statement
#Range
''''#r=range(12) #default start=0 ends=10 step=1 0/p: l:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#r=range(2,10) #o/p: l:  [2, 3, 4, 5, 6, 7, 8, 9]
#r=range(1,10,2) #o/p: l:  [1, 3, 5, 7, 9]
#r=range(1,10,3) #o/p: l:  [1, 4, 7]
#r=range(10,1,-1) #o/p: :  [10, 9, 8, 7, 6, 5, 4, 3, 2]
print("r: ",r)
l=list(r)
print("l: ",l)'''
#-----------
#print 1 to 100
'''for element in range(1,101):
    print(element) '''
list1=[10,15,20,22,24,27]
#A sequence to be processed
for i in list1:
    if i%2==0: #it will display only even numbers
        print(i)
    else:
        #pass
        #print('this issue passed')
        break
else:
    print(list1)
