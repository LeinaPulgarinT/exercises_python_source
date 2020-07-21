"""
link del enunciado del punto:
https://www.hackerrank.com/challenges/py-if-else/problem
"""

num = int(input("enter a number: "))
if num % 2 == 1 and num >= 1 and num < 100:
    print("Weird")
elif num >= 2 and num < 5:
    print("Not Weird")
elif num >= 6 and num <= 20:
    print("Weird")
elif num > 20 and num <= 100:
     print("Not Weird")
else: 
    print("Invalid number, please get into a number enside range")
