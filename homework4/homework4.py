#homework4.py

# 3.1 --- List Operations ---
# favorite_foods = ["korean fried chicken", "french fries", "boba", "icecream", "chocolate"]
# # # 1
# # #  print(favorite_foods[1]) #prints "french fries"
# # # # 2
# # # print(favorite_foods[-1])   #prints "chocolate"
# # # 3
# favorite_foods.append("rice")  #adds "rice" to the end of the list
# # # 4
# favorite_foods.insert(0, "apple")
# # # 5
# favorite_foods.remove("boba")  #removes "boba" (3rd item)from the list
# 6
# print(len(favorite_foods))  #prints the length of the list (6)
# 7
# for food in favorite_foods:
#     print(food.upper())
# 8
favorite_foods = ["apple", "korean fried chicken", "french fries", "icecream", "chocolate", "rice"]
# Foods_1 = favorite_foods[0::5] #slices first list to make new list with just first and last items
# print(Foods_1) # Foods_1 = ["apple", "rice"]
# 9
def potato_checker(favorite_foods):
    favorite_foods = ["apple", "korean fried chicken", "french fries", "icecream", "chocolate", "rice"]
    for foods in favorite_foods:
        if "potato" in foods:
            print("A potato!")
        else:
            print("No potato!")
potato_checker(favorite_foods)       #resulted in "No potato!" x6 I hope that's okay lol

# 3.2 --- Slicing and Striding---
# numbers = range(0,21)      #ERROR 1: did not give me the listed out numbers, only "range(0, 21)"
numbers = list(range(0,21))     #FIX: put "list" in front of range to make it that datatype
# #1
def get_first_15(numbers):
    return(numbers[0:15])
# # #2
# #ERROR 2: Defined variable "numbers2" inisde the function, so printing outside the function gave an error
# #FIX: Defined "numbers2" outside the function first
numbers2 = get_first_15(numbers)
def get_every_5th(numbers2):
    return(numbers2[0::5])
print(get_every_5th(numbers2))  #prints [0, 5, 10]
# #3
numbers3 = get_every_5th(numbers2)
def reverse_and_stride(numbers3):
    numbers4 = numbers3[::-1]
    return(numbers4[::3])
print(reverse_and_stride(numbers3))  #prints [10]

# 3.3 --- Nested Lists ---
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# #3.3.1 --- Nested List Operations ---
# #1
# print(numbers[2]) #prints [7, 8, 9]
# #2
# print(numbers[0][1]) #prints 2
numbers.append([10, 11, 12]) #adds [10, 11, 12] to the end of the list
# #4
def sum_nested(numbers):
    total = 0
    for row in numbers:
        for num in row:
            total += num
    return total
print(sum_nested(numbers))  #prints 78

# 3.4 --- Create a 5x5 List ---
def create_5x5():
    list_5x5 = []
    number = 1
    for i in range(5):
        row = []
        for i in range(5):
            row.append(number)
            number += 1
        list_5x5.append(row)                 #ERROR 3: list was numbers 0-24 intead of 1-25
    return list_5x5                          #FIX: identified number = 1 first, to start from 1 and not 0
print(create_5x5()) 
# #1
def replace_multipeles_of3(list_5x5):
    for i in range(len(list_5x5)):
        for j in range(len(list_5x5[i])):
            if list_5x5[i][j] % 3 == 0:
                list_5x5[i][j] = "?"
    return list_5x5
list_5x5_no3 = replace_multipeles_of3(create_5x5())
print(list_5x5_no3)
# #2
def sum_not_multiples_of_3(list_5x5_no3):
    total = 0
    for i in range(len(list_5x5_no3)):
        for j in range(len(list_5x5_no3[i])):
            if list_5x5_no3[i][j] != "?":
                total += list_5x5_no3[i][j]
    return total
print(sum_not_multiples_of_3(list_5x5_no3))  #prints 217     

# 4 --- Dictionaries ---
# 4.1 --- Dictionary Operations ---
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
# #1                          #ERROR 4: Didn't have "Katie" with capital K, so it wasn't working
# print(ages["Katie"])        #FIX: Added capital K to "Katie"
# #2
ages["Mira"] = 100 #updates Mira's age to 100
#3
ages["Milana"] = 52 #adds Milana with age 52
#4
del ages["Mariam"] #deletes Mariam from the dictionary
# #5
def print_ages(ages):
    for name, ages in ages.items():
        print(f'{name} = {ages} years old')

#favorite function
favorite_foods = ["apple", "korean fried chicken", "french fries", "icecream", "chocolate", "rice"]
#3.1.9 --- Potato Checker ---
def potato_checker(favorite_foods):
    for foods in favorite_foods:
        if "potato" in foods:
            print("A potato!")
        else:
            print("No potato!")
potato_checker(favorite_foods) 