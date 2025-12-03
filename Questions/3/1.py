# 1. The Classic FizzBuzz
# This is a famous introductory problem that's perfect for combining these concepts.
# The Task: Write a program that uses a loop to print the numbers from 1 to 100.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz"


fiz = []
buzz = []
fizzbuzz = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        fizzbuzz.append(num)
    elif num % 3 == 0:
        fiz.append(num)
    elif num % 5 == 0:
        buzz.append(num)


print(fiz)
print(buzz)
print(fizzbuzz)

