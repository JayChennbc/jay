# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py
# Questions (Answer these in the homework2.py file as comments):
# 1) What’s the difference between Git, GitHub, and Git Bash?
	#Git, is a terminal that runs locally on your computer. It can be used to make new directories, sorting files, and more. Github is an online platform where users can store their git repositories remotely and interact with those of other users. Git Bash is a version of Git with a Bash shell environemtn for Windows users, so they can code in a similar language to Mac users.
# 2) What’s the difference between the terminal and the command line?
	#The terminal is the place where you can interact with your computer system. The command line is where you actually type out the actions you want to perform.
# 3) How does Windows PowerShell differ from Git Bash?
	#Windows PowerShell operates using a different shell language than Git Bash. Powershell is specifically geared to windows and uses different commands from Git Bash, using language that is more generally used (in not just windows but also Mac, linux-unix).
# 4) What’s the difference between Anaconda, conda, and Python?
	#Python is a computer programming language. Conda is an "environment manager" that can be used with multiple programming languages including Python. Anaconda is a base of many different coding "packages" and tools that can be used with many computer languages.
# 5) What is VS Code? 
	#VS code is a free to use, computer code editor that supports many languages. 
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
	#Jupyter Notebook is essentially the older version of Jupyter Lab. In Notebook, one opens code one file at a time, limiting what they are working with, whereas Jupyter Lab allows you to open multiple notebooks, terminals, files, and more on a tab system so you can do more with the space.
# 7) What does ~/ mean?
	# ~/ refers to your root directory/home base or users/yangc/ on my computer.
# 8) What’s the difference between an absolute path and a relative path?
	#An absolute path locates a file/directory starting at the root directory whereas a relative path locates a file/directory from your current directory (i.e. relative to where you currently are).
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
	#ABSOLUTE: cd ~/python_decal_fa25/jay ~/python_decal_fa25/course_assignments/homework2
	#RELATIVE: cd ../course_assignments/homework2
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
	# ../
# 11) What would rm ./ do in your current directory? (Don’t try it!)
	# It would removre your current directory
# 12) What do the following commands do?
# git add: It saves your current repository to a staging area 
# git commit: This "commits" your current changes to become a recorded version in your local repository.
# git push: This adds your committed changes from a local repository to a remote one.
# 13) What's the difference between "git add ." and "git add <file>"?
	# git add . saves all files whereas git add <file> only saves that specified file to the staging area.
# 14) What do "git status" and "git log -1" do?
	#git status shows the status of your repository (like whether stuff needs saving or more), and git log -1 gives you more information like your git commit number.
# 15) What’s the difference between cloning a repository and pulling from it?
	#Cloning a repository saves a local version on your computer that will note respond to remote changes, but pulling from a remote repository updates a local one with the latest changes to its sister remote one.
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
	#For some reason I had a "lecture_notes" folder in my name repository and got it confused with the one that we made in classs, so for a while I did not know where my test.py file went. I went to office hours and was made aware of the duplicate name and was given further clarification on directory trees and paths to help me move the file to where I needed it to be.
# 17) What’s a question you still have? What’s something you’re confused about?
	#I did not catch the difference between the if, elif, else conditionals, and I guess I am not totally understanding of the def, add, return functions (like the examples we did in class seemed all very random, showing me the capacity of what they could do, but I don't think I could personally replicate them just yet).
# 18) Tell me a fun fact!
	#If Pranathi is grading this, I am also involved in Barestage! I am cast in Alice by Heart and a new member of Baretroupe. What a small world :)
# 19) Print your favorite math expression you've learned in Python so far. 
print(5 ** 3) # (gives the asnwer 125) ** raises the first number to the power of the second number. What an easy computer calculator alternative.
# (Hint: Use print() and add a comment explaining what it does.)