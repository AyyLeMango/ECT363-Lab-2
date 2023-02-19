"""
Dillon Stan
2/14/2023
ECT363 Lab 2

1. What’s the difference between abs() and fabs() 

fabs() always returns a floating point number, but abs() will return a floating-point or an integer depending on the input.

2. What can Triple Quotes do? 

Triple quotes are used to create a block comment in a Python program, although technically it is not a comment because it is still read by the interpreter and is considered a multi-line docstring. In contrast, comments which are denoted by the hash symbol are ignored by the interpreter.

3. What’s the difference between a list, tuple and dictionary? 

Lists can be edited, whereas tuples cannot be edited after creation. Lists are contained by square brackets, while tuples are contained by parentheses. A dictionary is a hybrid of a list and a tuple, which contains a set of keys which cannot be edited (but can be removed), each paired with a value which can be edited. Dictionaries are contained by curly brackets.

4. Write a python script to create a dictionary, and have the following operations: 
display the values find the maximum value and display it 
find the minimum value and display it 
add a new key-value pair to the dictionary and display it 
remove a key-value pair from the dictionary, display the updated one 
save the dictionary data in a .txt file create functions to (1) read a .txt file, (2) write a .txt file, (3) save a .txt file 
create a function to check if a specific letter exist in a .txt fiel

"""


import random
import json

def rd(fname):
    var=open(fname, "a+")
    var.seek(0)
    print(var.read())

def wrt(fname, arg):
    var=open(fname, "a+")
    var.write(json.dumps(arg))
    

def cls(fname):
    with open(fname, 'a+') as file:
        file.close()

def chk(fname):
    f=open(fname, "a+")
    f.seek(0)
    check=f.read()
    if "a" in check:
        print("String in text file")
    else:
        print("String not found in text file")

dictionary={}
for i in range(0,10):
    dictionary[i]=random.randint(0,100)
print(dictionary)
minimum=100
inkey=0
maximum=0
xkey=0
for i in range(0,10):
    if dictionary[i]>maximum:
        maximum=dictionary[i]
        xkey=i
    if dictionary[i]<minimum:
        minimum=dictionary[i]
        inkey=i
print("Maximum value is: ", maximum," at key value: ", xkey)
print("Maximum value is: ", dictionary[max(dictionary, key=dictionary.get)]," at key value: ", max(dictionary, key=dictionary.get))

print("Minimum value is: ", minimum," at key value: ", inkey)
print("Minimum value is: ", dictionary[min(dictionary, key=dictionary.get)]   ," at key value: ", min(dictionary, key=dictionary.get))
dictionary["hello"]='world'
print(dictionary["hello"])
del dictionary[0]

try:
    print(dictionary[0])
except KeyError:
    print("Probably KeyError: 0, because key doesn't exist.")
else:
    print("It thinks dictionary[0] still has a value!")

rd("lab2.txt")
wrt("lab2.txt",dictionary)
rd("lab2.txt")
chk("lab2.txt")
cls("lab2.txt")


"""
lab2=open("lab2.txt","a+")
lab2.write(json.dumps(dictionary))
lab2.seek(0)
check=lab2.read()
if "{" in check:
    print("String in text file")
else:
    print("String not found in text file")
print(check)
"""