#1:
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\mmm'  

print("Only directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])

print("\nOnly files:")
print([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

print("\nAll directories and files:")
print(os.listdir(path))

#2:
import os

def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = r'C:\Users\User\OneDrive\Рабочий стол\mmm'  
check_access(path)


#3:
import os

def path_info(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist")


path = r'C:\Users\User\OneDrive\Рабочий стол\mmm\b.cpp'  
path_info(path)


#4:
import os

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        print("Number of lines:", sum(1 for _ in file))

path = r'C:\Users\User\OneDrive\Рабочий стол\mmm'

print(os.listdir(path))

count_lines(os.path.join(path, 'b.cpp'))

#5:
def write_list_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(str(item) + '\n')

my_list = ['apple', 'banana', 54]  
write_list_to_file('output.txt', my_list)

print("List written to output.txt")

#6:
import string

for letter in string.ascii_uppercase: 
    with open(f"{letter}.txt", 'w', encoding='utf-8') as file:
        file.write(f"This is {letter}.txt\n")

print("26 text files created successfully.")


#7:
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
        dest.write(src.read())

copy_file('output.txt', 'lol.txt')

print("File copied successfully.")

#8:
import os

def delete_file(path):
    if os.path.exists(path):  
        if os.access(path, os.W_OK):  
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print(f"File '{path}' is not writable. Cannot delete.")
    else:
        print(f"File '{path}' does not exist.")


file_path = r'C:\Users\User\OneDrive\Рабочий стол\mmm\b.cpp'  
delete_file(file_path)


