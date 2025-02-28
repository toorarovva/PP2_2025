import math
import time
#1:
def multiply_list(lst):
    print(math.prod(lst))

#2:
def count_case(s):
    upper = lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
    print(upper, lower)

#3:
def is_palindrome(s):
    print(s == s[::-1])

#4:
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}")

#5:
def all_true(tpl):
    print(all(tpl))

multiply_list([2, 3, 4])
count_case("Hello World") 
is_palindrome("lol")
delayed_sqrt(25100, 2123)
all_true((True, True, False))