#homework5.py

#3.1 --- Vocabulary Review ---
#1. Git is like google drive for code, where you can store different versions of something while Github is an online platform for hosting Git repositories.
#2. The Terminal is the interface on the user's computer that allows them to interact with the computer while the command line is where command is actually typed out on the terminal.
#3. A local repository stores a version of your code on your own computer while a remote repository stores a version of your code on an online platform like Github
#4. Version control is again like google drive, where you can store different versions of something and go back to previous versions if needed.
#5. A staging area is where you make final changes to code before committing it to a remote repository.
#6. git add adds changes made in the staging area
#7. git commit saves changes from a local repository
#8. git push uploads changes from a local repository to a remote one
#9. git status shows status of git repository
#10. git pull downloads changes from a remote repository to a local one
#11. pwd means "print working directory" and shows your current directory and how you got there
#12. ls means "list" and shows all files and folders in the current directory
#13. cd means "change directory" and lets you move to a different directory
#14. nano allows you to change text in files on your terminal
#15. touch creates a new file
#16. mv moves files
#17. rm deletes files
#18. cat shows the contents of a file

#3.2 --- A Directory Tree ---
#1. pwd
#2. ls
#3. cd ../brianna_repo
#4. mv homework.py ~/python_decal/brianna_repo ~/python_decal/judy_decal/homework
#5. cd ../judy_decal/homework
#6. nano homework.py
#7. git add homework.py --> git commit -m "added homework.py" --> git push origin main
#8. git pull homework.py first to upload the changes from the remote repo to your local repo. The error means that there are unsaved changes
    #that would not have been added to the git commit
#9. (assuming that you are currently in homework/)
     #cd ~/python_decal/judy_decal/homework ~/Recent

#3.3 --- Draw Your Directory Tree (IRL Photo not here) ---

# #4.1 --- Data Types ---
def checkDataType(something):
    print(type(something))
checkDataType(something = 1) #<class 'int>
checkDataType(something = 'hello') #<class 'str'>

#4.2 --- Conditionals ---
def even_or_odd(input):
    if input%2 == 0:
        print("even")
    else:
        print("odd")
even_or_odd(input=4) #even
even_or_odd(input=5) #odd

# #5 --- Loops ---
numbers = [1, 2, 3, 4, 5]
def loop_sum(numbers):
    total = 0
    for i in numbers:
        total +=i
    return(total)
print(loop_sum(numbers)) #15

# #6 --- Homework 4 Review ---
# #6.1 --- Lists ---
listabc= ['a', 'b', 'c']
def duplicate_list(listabc):
    duplicated = []
    for item in listabc:
        duplicated.append(item)
        duplicated.append(item)
    return duplicated
print(duplicate_list(listabc))

# #6.2 --- Debugging ---
def square(num):         #missing the :
    return num*num 

#7 --- Running Your Code ---
#favorite function (Loops)
numbers = [1, 2, 3, 4, 5]
def loop_sum(numbers):
    total = 0
    for i in numbers:
        total +=i
    return(total)
print(loop_sum(numbers))
