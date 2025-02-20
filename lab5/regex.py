import re
#1:
def fun1(stringg):
        x = "ab?"
        if re.search(x,  stringg):
                return 'have a match'
        else:
                return('no match')

print(fun1("ab"))
print(fun1("abc"))
print(fun1("accc"))
print(fun1("bcc"))

#2:
def fun2(stringg):
        y = "ab{2,3}"
        if re.search(y,  stringg):
                return 'have a match'
        else:
                return('no match')
print(fun2("ab"))
print(fun2("abbbbcdd"))


#3:

import re

stringg = input("Enter string: ")

if re.search(r"[a-z]+_[a-z]+", stringg):
    print("have a match")
else:
    print("no match")


#4:
def fun4(stringg):
        y = r"[A-Z][a-z]+"
        if re.search(y,  stringg):
                return 'have a match'
        else:
                return('no match')
print(fun4("AbAb"))
print(fun4("abbbbcdd"))

#5:
def fun5(stringg):
        y = "a.*?b$"
        if re.search(y,  stringg):
                return 'have a match'
        else:
                return('no match')
print(fun5("AbAb"))
print(fun5("abbbbcdb"))

#6:
stringg = 'Hello, and today is my birthday, lol'
print(re.sub("[ ,.]", ":", stringg))

#7:
def fun7(stringg):
    words = stringg.split("_")
    result = words[0]
    for word in words[1:]:
           result += word.capitalize()
    print(result)
fun7("lol_lol_mm_kk")

#8:

def fun8(stringg):
    words = re.findall(r'[A-Z][a-z]*', stringg)  
    print(words)  

fun8("HelloWorld")
fun8("Mybirthday")

#9:
import re

def fun9(stringg):
    result = re.sub(r"([A-Z])", r" \1", stringg).strip()  
    print(result)  

fun9("HelloWorld")       

#10:
def fun10(stringg):
    result = re.sub(r'([A-Z])', r'_\1', stringg).lower()  
    print(result.strip("_"))  

fun10("HelloWorld")
fun10("Howareyou")


