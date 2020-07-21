"""
link del enunciado del punto:
https://www.hackerrank.com/challenges/write-a-function/problem
"""

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        return not leap
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return not leap
    else: 
        return leap

year = int(input())
print(is_leap(year))