#1:
def to_ounces(grams):
    ounces = 28.3495231 * grams
    print(ounces)

#2:
def f_to_c(f):
    c = (5 / 9) * (f - 32)
    print(c)

#3:
def solve(numheads, numlegs):
    x = (4 * numheads - numlegs) 
    y = numheads - x  
    return x, y

#4:
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]

#5:
def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            for perm in permutations(s[:i] + s[i+1:]):
                result.append(s[i] + perm)
        return result

#6:
def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    print(reversed_sentence)

#7:
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8:
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


#9:
import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


#10:
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

#11:
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

#12:
def histogram(nums):
    for num in nums:
        print('*' * num)

#13:
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

#14:
to_ounces(340)
f_to_c(267)
print(permutations("ABC"))
histogram([1,2,5])
guess_the_number()











