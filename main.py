# Print Hello world
# print("hello world")

# Generate a list of squares of numbers from 1 to 10.
# Print the numbers from 1 to 10.
# for i in range(1, 11):
#     print(i,end=" ")

# Find the maximum of three numbers.
# n1 = int(input("n1:"))
# n2 = int(input("n2:"))
# n3 = int(input("n3:"))
# print(max(n1,n2,n3))

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

# Write a program to swap two numbers.
# a = input("Enter a value a= ")
# b = input("Enter a value b= ")
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
# num = int(input())
# prime = True
# for i in range(2, num):
#   if num % i == 0:
#     prime = False
#     break
# if prime:
#   print("Prime")
# else:
#   print("Not prime")

# N = int(input())

# def sieve_of_eratosthenes(N):
#     is_prime = [True] * (N + 1)
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, int(N**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i*i, N + 1, i):
#                 is_prime[j] = False

#     primes = [i for i in range(2, N + 1) if is_prime[i]]
#     return primes
# result = sieve_of_eratosthenes(N)
# print(*result)




# Create an array of integers and calculate the sum of its elements.
# nums = list(map(int,input().split()))
# print(sum(nums))

# Find the largest number in an array of integers.
# nums = list(map(int, input().split()))
# largest = max(nums)
# print(largest)

# Reverse the contents of an array without using built-in functions.
# n = int(input())
# arr = list(map(int, input().split()))

# start = 0
# end = n - 1

# while start < end:
#     arr[start], arr[end] = arr[end], arr[start]
#     start += 1
#     end -= 1
# print(*arr)

# Implement a method to merge two sorted arrays into one sorted array.
# def merge_arrays(arr1, arr2):
#     result = []
#     i, j = 0, 0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1

#     while i < len(arr1):
#         result.append(arr1[i])
#         i += 1

#     while j < len(arr2):
#         result.append(arr2[j])
#         j += 1

#     return result

# arr1 = list(map(int, input("Enter arr1 : ").split()))
# arr2 = list(map(int, input("Enter arr2 : ").split()))
# output = merge_arrays(arr1, arr2)

# print("Merged Sorted Array:", sorted(output))
