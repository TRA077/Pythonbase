print('Hello World') 
#This is the print function that prints anythying within brackets. Any string value must be put in bracket so as to print the string.

var=1 
print(var)
#Here var is a variable or a memory space that stores a value 1 in this example.

var=2 
print(var)
#This shows that value of variable is not permanent and ranges from 1 to 2.

a1,a2,a3=1,"Mango",'tree'
print(a1,a2,a3)
#We see that we could assign multiple variables multiple values and simultaneously print them using Python.

a1=a2=a3='Tree'
print(a1)
print(a2)
print(a3)
#This is Multiple assignment and we assign multiple varaibles same value i.e. tree.

#Datatypes are data or values stored in a variable. They are of 6 types: Number, String,List, Tuple, Dictonary.

#Operators are used for performing different operations on variables, values, and expressions.
b1,b2=20,10
#Arithematic operators perfom arithematic operations.They are:+,-,*,/,%.
print(b1+b2) #Addition
print(b1-b2) #Subtraction
print(b1*b2) #Multiplication
print(b1/b2) #Division
print(b1%b2) #Mod operation: It returns the remainder of the operation and is always positive.
#Like here we divided 20 by 10 and remainder is 0.
print(b2%b1) #Since 20 can't divide 10 remainder is 10.

#Strings could also be added.
print(a2+a3)
print(a2+" "+a3) #We could add space between the strings using double quotes and space in between them.

c1="Python Programming"
print(c1[10]) #This is slicing, here we could get the word in String at the 11th position since in python indexing starts from zero. 
#So it gives 1st g in c1.
#To make indexing more clear we note that the index of the first P in c1 is 0 and that of y is 1 and t is 3 and so on.
#Space is also considered as a string so its index in c1 is 6.
#Thus if we want to get nth position we slice it to n-1. Like for 8th position we slice it as 7.
print(c1[7]) #we could see that 2nd P at 8th position is printed.

#Slicing can also be done for a row of strings and we could print a particular part of the string.
print(c1[0:5])#The left side to colon is the index position from where we want to start and the right is the final index position + 1
#Here we start from 0 index and index position we want to end +1 i.e. 4 is o's index so we give 4+1=5 in right side.
#If we want to print python we write:
print(c1[0:6])#as python ends at index 5 so we give 5+1=6 and starts from index 0.
#To print programming:
print(c1[7:18])
# We could also do the below to print programming ie to print everything after index 7:
print(c1[7:])
