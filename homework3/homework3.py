#homework3.py

#3.1 --- Say Goodbye ---
# def say_goodbye(name):
#    return(print("Goodbye,", name))
# name = "Jay"
# say_goodbye(name)

# #3.2 --- Area of a Circle---
# def area_circle(r):
#    return(print(pi*(r**2)))
# pi = 3.14
# area_circle(r = 3) #28.26

# #4.1 --- Subtract, Multiply, Divide ---
# def subtract(a, b):
#     return(print(a - b))
# subtract(a=16, b=5)  #11
# def multiply(a, b):
#     return(print(a * b))
# multiply(a=2, b=3) #6
# def divide(a, b):
#     return(print(a / b))
# divide(a = 10, b = 2)   #5.0

# #5.1 --- What Should I Wear? ---
# def fire_fit_check(temperatures):
#     return(print((min(temperatures), max(temperatures))))
# temperatures = [15, 17, 19, 27, 31, 24, 21]
# fire_fit_check(temperatures)   #(15, 31)

# #5.2 --- Check if it's the Weekend ---
# def is_weekend(day):
#     if day == 6 or day == 7:   #lol 6 7
#         return(print("True"))
#     else:
#         return(print("False"))
# day = int
# is_weekend(7)

# #5.3 --- Fuel Efficiency Calculator ---
# def fuel_efficiency(miles, gallons):
#     return(print(miles / gallons))
# fuel_efficiency(miles=40, gallons = 8) #5.0 miles per gallon

# #5.4 --- Secret Code ---
# def secret_code(int):
#                 #(int % 10) gives last digit
#                 #(int // 10) gives number without the last digit
#                 #multiply (int % 10) to 10^(number_digits - 1)
#                 #add that to (int // 10)
#     number_digits = len(str(int))  #makes number a "word" whose character count can be shown
#     return(print((int//10)+((int%10)*(10**(number_digits-1)))))
# secret_code(157387) #715738

# #6.1 --- Oski Stole Your Power ---
# def raise_exponent(x, y):
#             #for i in range(2) --> print(x*x)
#             #for i in range(3) --> print(x*x*x)
#             #multiply x's y times
#     answer = 1 
#     for i in range(y):
#         answer *= x
#     return(print(answer))
# raise_exponent(2,4)

# #6.2.1 --- For Loops ---
#     #1
def minimum_value_for(list):
    list2 = [1001, 5, 7, 8, 10, 99, 1]
    small_num = list2[0]
    for int in list2:                          
        if int < small_num:
            small_num = int
    return(print(small_num))
minimum_value_for(list)
    #2
def maximum_value_for(list):
    list1 = [1, 7, 8, 10, 99, 1001, 5]
    big_num = list1[0]
    for int in list1:
        if int > big_num:
            big_num = int
    return(print(big_num))
maximum_value_for(list)

#6.2.2 --- While Loops ---
    #1
def minimum_value_while(list):
    list = [9999, 5, 7, 3, 10, 12, 8]
    small_num = list[0]
    index = 1
    while index < len(list):
        if small_num < list[index]:
            index += 1
        elif small_num <= list[index]:
            small_num = list[index]
            index += 1
        elif small_num >= list[index]:
            small_num = list[index]
            index += 1
    return(print(small_num))
minimum_value_while(list)
#     #2
def maximum_value_while(list):
    list = [8, 5, 7, 3, 10, 9999, 8]
    big_num = list[0]
    index = 1
    while index < len(list):
        if big_num > list[index]:
            index += 1
        elif big_num <= list[index]:
            big_num = list[index]
            index += 1
    return(print(big_num))
maximum_value_while(list)

# #6.3 --- Calculate the Sum ---
def sum_digits(number):
    total=0
    for individual_digit in str(number):
        total += int(individual_digit)
    return(print(total))
sum_digits(425)

#7.1 --- In Your VS Code Terminal ---
#(favorite code: minimum_value using a while loop 6.2.2.1)
#minimum_value(list)
#list = [9999, 5, 7, 3, 10, 12, 8]
# print(f"The result of minimum_value using a while loop(6.2.2.1) with a list = [9999, 5, 7, 3, 10, 12, 8] is {3}")





        

