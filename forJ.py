# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:55:42 2020

@author: D-Amparan
"""

#Basics overview for Python
#So to begin we have simple syntax that will help familiarize with what you are doing


import pandas as pd          
import numpy as np 
import math 

"""
The import simply imports additional libraries that you will need to access
for Example, numpy is an array or "table", it holds contents in each space which is refered to as index
Pandas is a new one for me as well but it allows you to create data frames easily and with a breeze (its very useful)
"""
"Now additionally this text in red is also a comment, this is ignored by the program when you run it"
#this is also a comment but the difference is that a '#' only comments on one line 
''' <------ (starting comment)semicolons
this
is 
also
a                                 comment 
but it is made using 6 semicolons 
3 
(ending comment)semicolons----->'''

#now assiging a variable is when you take the variable you name in this example t
#and its value is then 2, SO whenever you call this it prints 2 or holds 2
'''
Variable names can be anything you want from oneletter to as long as you want BUT it helps if you name them
something relevant for example
'''
t=1+1
age=21#here im keeping track of my age so we name the variable age something relevant to what we are dealing with 
myName='david' #when you want to save regular words in a variable such as names or words etc you must put them in semicolons
#reason being is because words are considered strings which are handled differently rather than numbers

'''
So that is how we hold data, furthermore lets say you want to display this data 
the way you do this is to use "print"
This display things to the console which is to the right hand side 
You can display variables or just type out want you want to print
If you want to print words it is the same concept as saving them in the variable; in between semicolons 
'''

print('This is our t value: ',t)
print("We can also add to the t when priting: ",t+1)
print("Print a integer value directly: ",100)
print("My age: ",age)

print("My name is: ",myName)
print("Your name is :", 'Jonathan')
print('I have 32 Birds')
print()
print()

"""
So from the previous example we have been handling two types of data 
int numbers       this will only apply to whole numbers from 0-infinity
string words      like i said they just represent a word, sentence etc for example : I have three birds
OTHER TYPES
float: Is similar to int but they can also have decimals so it is perfect for math
Boolean: Boolean is true or false, so they ease if statements etc 
"""
#FLOAT
t=1.001
t1=1
print("This is the difference between int and float: ", t," ",t1)


#BOOLEAN
x=True
y=False
print("Boolean values: ", x,y)
print()
print()

"""
Now we have basic functions that we can do in Python 
For Loops: For loops is a conditional statement that allows you to repeat step/s as much as you neeed
While: Same as a for loop but this will repeat the step/s while some condition is true
"""

for i in range(5):#this line reads "For i (which is zero unless stated) within range 5 do this 
    #so the for loop will repeat 5 times 0 1 2 3 4
    print(i)
print()

for c in 'Jonathan':#here go for all the data given and print each letter 
    print(c)
print()

x=10
y=20
while x<y:
    x=x+2
    print(x)
#a while loop allows you to keep going as long as the condition given is true 
print()
print()




"""
Pandas and Math

import Math allows you to access mathematical functions 
Pandas allows you to set up a data frame so a table of data 
Now Ill try to expain math as best as i can but for pandas 
I would reccomend to look on youtube because i just barely began using it a week ago so i kinda dont know it still 
"""    
#the math import which is used as math.then the name of the function you want to use then the parameter or the number inside you need 
print("Facotrial of 10: ",math.factorial(10))#for exxample here we do the math.factorial(10) we are taking the factorial of 10 and printing it 

print("Absolute value of -200: ",math.fabs(-200))
print("The square root of 10: ",math.sqrt(10))
#there is many math commands so if you need one simplt google math python and youll get everything that includes how to call it the parameters and exsample 

"""
Other Basics 
"""
#lets say you want the lenth of a particular sentence or word 
myName='David'
print("Length of my name is: ",len(myName))#to get the length we then use the command len()...within the parenthesis you enter the variable you need the length for so in this case
# we used a string but what if you need the len of a list? 

array=np.array([1,2,3,5])#here we create a simople array of 4 numbers 
print("Length of the array is: ",len(array))#we then need the length so we use the len and boom we attain the length of the given array 


