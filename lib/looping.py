#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(f"{10 - i}")
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for i in int_list:
        squared_list.append(i ** 2)
    return squared_list

def fizzbuzz():
    fizzbuzz_list = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif i % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif i % 5 == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(str(i))
    for item in fizzbuzz_list:
        print(item)
