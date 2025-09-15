#homework1.py
#3.1 --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) #a is an integer, a whole number with no decimals
b = 1.5
print(b)
print(type(b)) #b is a float, a number with decimals
c = 3j
print(c)
print(type(c)) #c is a complex data type, containing numbers and letters
d = "hello"
print(d)
print(type(d)) #d is a string, it contains only letters
e = [1, 2, 3]
print(e)
print(type(e)) #e is a list, it is a collection of data that is typically ordered and mutable
f = {"name": "Jay", "favorite fruit": "Mango"}
print(f)
print(type(f)) #f is a dictionary, it stores paired elements known as "key value pairs"
g = (1, 2)
print(g)
print(type(g)) #g is a tuple, it is a set of ordered elements that remains consistent
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list, a set of data whose order can be changed
i = True
print(i)
print(type(i)) #i is a bool/Boolean, it represents a logical value (true or false)
j = None
print(j)
print(type(j)) #j is a NoneType, a data type with an absence of a value, None alone is special
k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list, a collection of data in a mutable order
l = str(14)
print(l)
print(type(l)) #l is a string, despite having a whole number(datatype: integer)
m = 1e4
print(m)
print(type(m)) #m is a float, although it is not a decimal and it represents a whole number, it has that extra letter, and the terminal actually performed the math/the exponent
#1. I found 9 different datatypes
#2. Integer, float, complex, string, list, dictionary, tuple, Boolean, NoneType
#3. m and b are both floats. l and d are both strings. e, h, and k are all lists.
#4. The data type of l was string. It was not an integer (despite having the whole number 14) because of the added str() in it. So using str(), anything within those parantheses would be the string datatype.
#5. Another datatype not here is a set.
n = {1, 2, 3}
print(n)
print(type(n)) #n is a set, an unordered collection of elements. It is different from a list because instead of [] it uses {}
#3.2 --- Booleans ---
print(10>9) #True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, evaluated the "truthiness" of abc
print(bool(123)) #True, 123 are the truth I guess
print(bool(["apple", "cherry", "banana"])) #True, non-empty brackets and quotations are true
print(bool(True)) #True, self explanatory, the truthiness of "True" is true
print(bool(False)) #False, the truthiness of "False" is false
print(bool(0)) #False, 0 is considered not true by bool, absent value kind of
print(bool("")) #False, bool interprets empty quotations as false
print(bool(" ")) #True, bool interprets quotations with ANYTHING inside to be true
print(bool(())) #False, bool interprets empty parantheses as false
print(bool([])) #False, bool interprets empty brackets as false
print(bool({})) #False, bool interprets empty {} as false
print(bool(True and False)) #False, bool interprets that it is false for something to be true and false at the same time
print(bool(True and True)) #True, bool interprets something that is double "True" as true
print(bool(False and False)) #False, bool interprets something that is double "False" as false
print(bool(True or False)) #True, the or makes the bool function return the first truthy item, making true the first one
print(bool(True or True)) #True, the only two options are true
print(bool(False or False)) #False, the only two options are false
print(bool(not(False))), #True, something not false is true
print(bool(not(True))) #False, something not true is false
#Q1. Something that is comes out as true either has a value within it or is the word true. And something that returns as false either has no value within it or is the world false.
#Q2. bool(False and False) surprised me because I thought it would come out as true. Idk I think the double negative was affirming in a way, possibly making it true.
#Q3. print(2 > 1), will give true because 2 is greater than 1
#Q4. print(-10000 > 1) will give false because negative 10000 is not greater than 1
#proof below
print(2 > 1) #True
print(-10000 > 1) #False
#3.3 --- Operators ---
#3.3.1 - Arithmetic Operators -
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division
print(5 % 2) # 1, % gives the remainder of dividing the two numbers
print(3 ** 2) # 9, ** raises the first number to the exponent of whatever number comes next
print(15 // 2) # 7, // gives the closest whole number as a result of dividing the 2nd number from the first
#3.3.2 - Comparison Operators -
print(5 == 2) #False, == tells us that 5 does not equal 2
print(10 != 10) #False, 1= tells us that 10 and 10 ARE equal, so the function determines whether two things aren't
print(2 < 5) #True, 2 is less than 5, < is performing number comparison
print(12 > 5) #True, 12 is greater than 5, same as above
print(5 <= 6) #True, 5 is less than or equal to 6
print(1 >= 10) #False, 1 is not greater than or equal to 10
#3.3.3 - Assignments Operators -
x = 5
x += 5 
print(x) # 10, 5+5 = 10 x is now 10
x -= 4
print(x) # 6, 10-4 = 6, x is now 6
x *= 3
print(x) # 18, 6*3 = 18, x is now 18
#3.3.4 - Logical Operators -
#1. "And" adds together two conditions. Only returns true if both conditions are met.
print(True and True) #True
print(True and False) #False
#2. "Or" indicates two conditions, in which if one is met, the function can return as true
print(True or False) #True
print(False or False) #False
#3. "Not" indicates an inversion in truth, so something NOT false is true and something NOT true is false
print(not 0) #True
print(not "hi") #False
#More Questions:
#1. / performs divison and can result in decimal answers, whereas // only gives the whole number answer in division
#2. % gives the remainder of performing division, whereas // only gives the whole number.
#3. I would use % example below...
print(10 % 3) # 1, the remainder of 10/3 is 1
#4. Assignment operators perform the operation on the given variable with the new 2nd number and assigns that new value of that operation to the variable.
#3.4 --- Strings ---
my_string = "hello"
print(my_string) #prints: hello
print(my_string[0]) #prints: h
print(my_string[1]) #prints: e
print(my_string[2]) #prints: l
print(my_string[3]) #prints: l
print(my_string[4]) #prints: o
print(my_string[-1]) #prints: o
print(my_string[1:3]) #prints: el
print(my_string[0:5:2]) #prints: hlo
print(len(my_string)) #prints: 5
print(my_string + "goodbye") #prints: hellogoodbye
print(7 * my_string) #prints: hellohellohellohellohellohellohello
#3.4.1 - Questions -
#1. Slicing takes out specific "sub-sequences" from larger sequences typically by telling how often to slice something within a range. We sliced for manipulation 9.
#2. Below
name = "Oski"
print("Hello, my name is", name) #prints: Hello, my name is Oski
#4. The first print statement manually adds more to the statement, but the second one uses math to add it for you. F-strings are represented in the second statement which make it easier to write a longer message.
#3.5 --- Terminal Commands ---
#cd
#Changes directories. Use it to move from one folder to another
#ex)cd python_decal_fa25
#cd datatypes
#ls
#List. Shows all folders/files present in your current directory
#ex) ls homework1.py
#ls -a
#List, shows all folders/files in directories, even hidden ones
#ex) ls -a Desktop
#mkdir
#Make Directory, creates a new folder
#ex) mkdir hello!
#cat
#Concatenate, writes out all the code within a file
#ex) cat datatypes.py
#pwd
#Shows how I got to my current folder
#ex) pwd 
#cd ..
#Brings you to your root directory/home base
#ex) cd ..
#cd .
#Keeps you in your current folder
#ex) cd .
#cd~
#Similar to cd .. takes user back to home base
#ex) cd~
#cp
#Copies a file
#ex) cp datatypes.py
#mv
#Moves or renames a file
#ex) mv random_file 
#rm
#Deleting files
#ex) rm datatypes.py
#clear
#It clears the terminal
#ex) clear
#grep
#It searches for code within your terminal, kind of like ctrl f but for coding
#grep jay/
#Questions
#1. a) less <filename> displays what is in the file
   #b) echo <text> prints the text inside to the terminal
   #c) tar, compresses and archives files
#2. ls shows folders/files but ls -a shows any hidden files too
#3. A hidden file is a file that starts with a .
#4. a) -l, gives more detailed information about the file (perms, owner, size, etc)
   #b) -r, attached to rm, removes subdirectories within directories
   #c) -i, attached grep it "igores case"making the search letter case sensitive
#4 --- Running Your Script ---