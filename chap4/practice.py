#!usr/bin/python
''' the line directly above is used to make the file executable, this way instead of typing python filename.py into the terminal, you only have to type 

	./filename.py

and the file will run. you must change the permission of the file first
chmod 744 scriptname.py'''

''' Question 1: create a function that converts inches to centimeters 1in = 2.54cm?'''

def Inchtocent(inch):
  return inch*2.54

''' Question 2: Create object that will receive raw input from user by asking the user a question'''

asking = raw_input("How old are you? ")

'''Question 3: Build a dictionary with three key-value pairs. Call the value for one of the keys. Delete the dictionary?'''

hashtable = {"Harry": "Paarsch",
             "Larry": "David",
             "John": "Doe"}

hashtable["Harry"]
del hashtable

'''Question 4: Build a list of numbers and then sort it without changing the object you assigned the list to'''

numbers = [1,4,2,5,3,6]
numberssorted = sorted(numbers)


'''assign a statement to an object, then print the 3rd letter only, then the 1st through the 3rd, check the length of the statement, add two statements together, print a statements multiple times with line breaks'''

rick = "Hello World"
rick[2]
rick[0:2]
len(rick)
first = "hello"
second = "world"
Hello = first + second
print 3 *  ("This can be repeated \n")

'''strip the words from a statements'''

statement = "this is a statement"
statement.split()


'''insert and object in the middle of a print statement'''
dogs = 10
print "the %dth is not here!" % dogs


'''build a for loop to list out the names in a list'''
for names in ["chad", "john", "adam"]:
  print names

'''create the following file
the first line
the second line
the third line

then read it into python and write the contents out to another file'''
import os
out = open('InputFile.dat', 'w')
out.write(
'''the first line
the second line
the third line
''')
out.close()

#empty dataframe is necessary
lines = []
for line in open('InputFile.dat', 'r'):
  lines.append(line)

outputFile = open("outputFile.py", "w")
for n in range(0, len(lines)):
  outputFile.write(lines[n])

''' write a function the calculates n! The right answer will implement recursion'''

def Factorial(n):
  if (type(n) != int):
    print "this is not a integer"
    return n
  if (n < 0):
    print "n cannot be negative"
    return n
  if (n == 0):
    return 1
  else:
    return n * Factorial(n-1)



  
