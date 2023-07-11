#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


happy_new_year()

int_List = [1, 2, 3, 4, 5]


def square_integers(int_list):
    int_list = [list_item * list_item for list_item in int_list]
    return int_list


def fizzbuzz():
    num = 1
    while num < 101:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1
