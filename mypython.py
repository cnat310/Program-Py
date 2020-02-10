#####!/usr/bin/python...commented out to match program requirement of $python mypython.py
#print "Hello World!"
#Chris Nat CS 344 Winter 2020 Python Exploration

#This program shows how file creation can be done much easier in a higher level language like python. The key concept that I took away from lecture is that C is very fast at computation while python is very fast to code. The lecture explains how computation can be performed in C while file creation can be done in python.

#from kite.com/python/docs/random.choice...import random and string to use the random letter assignment below
import random
import string

#create 3 files using w+....from guru99.com/reading-and-writing-files-in-python.html
fileA = open("fileAlpha", 'w+')
fileB = open("fileBeta", 'w+')
fileC = open("fileCharlie", 'w+')

#creating a python "list" of the files...geeksforgeeks.org/python-list/
files = [fileA, fileB, fileC]

#python for loop... geeksforgeeks.org/python-for-loops/
for file in files:
	#using a generator expression so that a for loop can be used as an argument in .join()
	#explanation from stackoverflow.com/questions/50421524/string-join-method-used-with-for-loop
	s = "".join(random.choice(string.ascii_lowercase) for n in range(10))
	#from leacture on mixing languages, pretty straight forward exmample to build strings to meet project criteria for adding newline character at end of file
	file.write(s + "\n")
	file.close()

#from guru99 source above, open files in read 'r'
fileA = open("fileAlpha", 'r')
fileB = open("fileBeta", 'r')
fileC = open("fileCharlie", 'r')

#I had to recreate the list from above
files = [fileA, fileB, fileC]
	
for file in files:
	#read first 10 characters from the line
	readLine = file.read(10)
	print readLine
#1 - 42 inclusive
randNum1 = random.randint(1,43)
print randNum1

randNum2 = random.randint(1,43)
print randNum2

#simple multiplication
print randNum1 * randNum2
