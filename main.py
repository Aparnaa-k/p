# patient = input()
# age = int(input())
# print("We check in a patient named", patient,". He's", age, "years old and is a new patient.")

# Full_name = input("What is your full name? ")
# Fav_color = input("What is your favorite color? ")
# print(Full_name, "likes", Fav_color)

# Weight = int(input("Enter the weight in pounds: "))
# weight_in_kg = Weight*0.45
# print(Weight, "pounds is", weight_in_kg, "kilograms")

# print("""First program - Python print function
# It declares likek this:
# print('What to print')""")

# name = input("What is your name? ")
# print("Hello " + name +  " How are you? ")

# a = input("Enter a value a")
# b = input("Enter a value b")
# temp = a
# a = b
# b = temp
# print(a, b)

# a = int(input())
# b = int(input())
# add = a + b
# print(add)

# num = input()
# first = num[0]
# second = num[1]
# add_digit = int(first)+ int(second)
# print(add_digit)

# word =input()
# count = 0
# for i in word:
#   if i == "a":
#     count += 1
#     if count != 2:
#       print("False")
#     else:
#       print("True")

# word = input()
# count = 0

# for i in word:
#   if i == "a":
#     count += 1
# if count == 2:
#   print("True")
# else:
#   print("False")

# age = int(input())

# years_left = 90 - age
# days_left = years_left * 365
# months_left = years_left * 12
# weeks_left = years_left * 52

# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.)

# "Find the maximum of three numbers.
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#   print(a)
# elif b > a and b > c:
#   print(b)
# else:
  # print(c)
  
# # Count the number of vowels in a given string.
# word = input()
# count = 0
# for i in word:
#   if i == "a" or i == "e" or i == "i" or i == "o":
#     count += 1
# print(count)

# # Generate a list of squares of numbers from 1 to 10.
# list = []
# for i in range(1, 11):
#   list.append(i**2)
# print(list)

# # Write a program to swap two numbers."
# a = int(input())
# b = int(input())
# temp = a
# a = b
# b = temp
# print(a, b)

# "Write a program to reverse a string.
# word = input()
# reverse = ""
# for i in word:
#   reverse = i + reverse
# print(reverse)

# Print the multiplication table of a given number.
# num = int(input())
# for i in range(1, 11):
#   print(num, "x", i, "=", num*i)

# Print the odds numbers from 1 to n"
# n = int(input())
# for i in range(1, n+1):
#   if i % 2 != 0:
#     print(i)

# Check whether a string is a palindrome.
# word = input('Enter the word->  ')
# palindrome = word == word[::-1]
# if palindrome:
#   print("True")
# else:
#   print("False")

# Calculate the factorial of a given number.
# num = int(input())
# factorial = 1
# for i in range(1, num+1):
#   factorial *= i
# print(factorial)

# Print Fibonacci series up to the 10th term.
# a = 0
# b = 1
# for i in range(10):
#   print(a, end=",")
#   c = a + b
#   a = b
#   b = c

# Check if a number is prime or not.
num = int(input())
prime = True
for i in range(2, num):
  if num % i == 0:
    prime = False
    break
if prime:
  print("Prime")
else:
  print("Not prime")