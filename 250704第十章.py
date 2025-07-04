#第十章
import os
os.system('cls' if os.name == 'nt' else 'clear') 

from pathlib import Path
path=Path('pi_digits.txt')
contents=path.read_text()
contents=contents.rstrip()#rstrip删除字符串末尾的空白
print(contents)

contents1=path.read_text().rstrip()#方法链式调用
print(contents1)

from pathlib import Path
path=Path('pi_digits.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line
print(pi_string)
print(len(pi_string))

from pathlib import Path
path=Path('pi_million_digits.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday=input("enter your birthday,in the form of mmddyy")
if birthday in pi_string:
    print("your birthday appears in the first million digits od pi!")
else:
    print("your birthday doesnt appear")

#10.1
from pathlib import Path
path=Path('learning_python.txt')

contents = path.read_text(encoding='utf-8')
print(contents)

lines=contents.splitlines()
string=''
for line in lines:
    string+=line
print(string)

#10.2
message='i like dogs'
message=message.replace('dog','cat')
print(message)

#10.3
from pathlib import Path
path=Path('learning_python.txt')

contents = path.read_text(encoding='utf-8')
contents=contents.replace('python','c')
print(contents)

lines=contents.splitlines()
string=''
for line in lines:
    string+=line
print(string)

from pathlib import Path
path=Path('programming.txt')
contents='i love programming\n'
contents+='i love creating new games.\n'
contents+='i also love working with data.\n'
path.write_text(contents)
#如果文件已经有内容，write_text会删除内容重新写入

#10.4
from pathlib import Path
path=Path('user_list.txt')
user_list=''
user_list=input('enter your name')
path.write_text(user_list)

#10.5
from pathlib import Path
path=Path('guest_book.txt')
guest=''
while True:
    name=input('enter your name')
    guest+=name+"\n"#'+'表示字符串拼接，确保每个名字后面换行
    tag=input('any people want to enter?')
    if(tag=='no'):
        break
path.write_text(guest)

try:
    print(5/0)
except ZeroDivisionError:
    print("you cant divide by zero!")

print("give me two numbers,i will divide them")
print("enter 'q' to quit")
while True:
    first_number=input("\nenter first number")
    if first_number == 'q':
        break
    second_number=input("\nenter second number")
    if second_number == 'q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you cant divede by 0!")
    else:
        print(answer)

from pathlib import Path
path=Path('alice.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"the file {path} doesnt exist")

from pathlib import Path
path=Path('alice.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"the file {path} doesnt exist")
else:
    words=contents.split()
    num_words=len(words)
    print(f"the file {path} has {num_words} words")
    print(words[:10])

from pathlib import Path
def count_words(path):
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry,{path} doesnt exist")
    else:
        words=contents.split()
        num_words=len(words)
        print(f"the file {path} has {num_words} words")

path=Path('alice.txt')
count_words(path)

from pathlib import Path
def count_words(path):
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry,{path} doesnt exist")
    else:
        words=contents.split()
        num_words=len(words)
        print(f"the file {path} has {num_words} words")

filenames=['alice.txt','siddartha.txt','moby_dick.txt','little_woman.txt']
for filename in filenames:
    path=Path(filename)
    count_words(path)

#10.6 and 10.7
while True:
    flag=input("enter 'q' to quit")
    if flag=='q':
        break

    try:
        first=int(input("enter the first number"))
        second=int(input("enter the second number"))
        answer=first+second
        print(answer)
    except ValueError:
        print("you should enter number!")

#10.8
from pathlib import Path
path=Path('dogs.txt')
try:
    contents=path.read_text(encoding='utf-8')
    print(contents)
except FileNotFoundError:
    print("file doesnt exist")

#10.9
from pathlib import Path
path=Path('cats.txt')
try:
    contents=path.read_text(encoding='utf-8')
    print(contents)
except FileNotFoundError:
    pass

#10.10
line='Row,row,row your boat'
print(line.count('row'))
print(line.lower().count('row'))

from pathlib import Path
import json
numbers=[2,3,5,7,11,13]

path=Path('numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)

numbers1=json.loads(contents)
print(numbers1)

username=input('whats your name?')
path=Path('username.json')
contents=json.dumps(username)#返回对象的json字符串表示
path.write_text(contents)

print(f"we will remember you when you back,{username}")

name=json.loads(contents)#读取json字符串再解析
print(name)

from pathlib import Path
import json
def get_stored_username(path):
    #如果存储了用户名，就获取它
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username=input('whats your name?')
    contents=json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path=Path('username.json')
    username=get_stored_username(path)
    if username:
        print(f"welcom back,{username}")
    else:
        username=get_new_username(path)
        print(f"we will remember you when you back,{username}")

greet_user()

#10.11
from pathlib import Path
import json
path=Path('fa_number.txt')
fa_number=input('whats your favorite number?')
contents=json.dumps(fa_number)
path.write_text(contents)

contents=path.read_text()
fa_number1=json.loads(contents)
print(f"you love {fa_number1}")

#10.12
from pathlib import Path
import json
def get_stored_number(path):
    if path.exists:
        contents=path.read_text()
        fanumber=json.loads(contents)
        return fanumber
    else:
        return None

def get_new_number(path):
    fanumber=input('whats your favorite number?')
    contents=json.dump(fanumber)
    path.write_text(contents)
    return fanumber

def print_number():
    path=Path('fa_number.txt')
    fanumber=get_stored_number(path)
    if fanumber:
        print(f"your favorite number is {fanumber}")
    else:
        fanumber=get_new_number(path)
        print(f"we remember you love {fanumber}")
print_number()

