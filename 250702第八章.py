#第八章函数
import os
os.system('cls' if os.name == 'nt' else 'clear') 

def greet_user(username):
    print(f"hello!,{username.title()}")
greet_user("jesse")
greet_user("sarah")

#8.1
def display_message(theme):
    print(f"the theme is {theme.title()}")
display_message("function")

#8.2
def favorite_book(title):
    print(f"one of my favorite book is {title.title()}")
favorite_book("alice in wonderland")

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}.")
describe_pet("hamster","harry")#hamster:仓鼠

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}.")
describe_pet(animal_type='hamster',pet_name='harry')

def describe_pet(pet_name,animal_type='dog'):
#有默认值的形参放在后面，为了让输入的实参与无默认值的形参位置对应
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}.")
describe_pet(pet_name='harry')

#8.3
def make_shirt(size,word):
    print(f"size is {size}")
    print(f"word is {word}")
make_shirt('M','hello')

#8.4
def make_shirt(word='I love python',size='L'):
    print(f"size is {size}")
    print(f"word is {word}")
make_shirt()
make_shirt(size='M')
make_shirt('hello')

#8.5
def describe_city(name,country='china'):
    print(f"{name.title()} is in {country.title()}")
describe_city('chongqing')
describe_city('chengdu')
describe_city('seoul','korea')

def get_formatted_name(first,last,middle=''):
    if middle:
        full=f"{first} {middle} {last}"
    else:
        full=f"{first} {last}"
    return full.title()
musician1=get_formatted_name('jimi','lee','hendrix')
musician2=get_formatted_name('jin','taehyung')
print(musician1,'\n',musician2)

def build_person(first,last):
    person={'first':first,'last':last}
    return person
musician=build_person('jimi','hendrix')
print(musician)

def build_person(first,last,age=None):
    person={'first':first,'last':last}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)

def get_formatted_name(first_name,last_name):
    full=f"{first_name} {last_name}"
    return full.title()
while True:
    first=input("full name?enter'q'to quit")
    if first=='q':
        break
    last=input("last name?enter'q'to quit")
    if last=='q':
        break
    formattedname=get_formatted_name(first,last)
    print(f"hello,{formattedname}")

#8.6
def city_country(name,country):
    thread=f"{name},{country}"
    return thread
while True:
    i_name=input("name?")
    if i_name=='q':
        break
    i_country=input("country?")
    if i_country=='q':
        break
    i_thread=city_country(i_name,i_country)
    print(i_thread)

#8.7and8.8
def make_album(singer,album_name,number=None):
    dic={'singer':singer,'album_name':album_name}
    if number:
        dic['number']=number
    return dic
while True:
    i_singer=input("singer?")
    if i_singer=='q':
        break
    i_album_name=input("album name?")
    if i_album_name=='q':
        break
    number=input("number?")
    if number=='q':
        break
    i_album=make_album(i_singer,i_album_name,number)
    print(i_album)

def greet_users(names):
    for name in names:
        msg=f"hello,{name.title()}"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)

def print_models(unprinted,completed):
    while unprinted:
        current=unprinted.pop()
        print(f"{current} is printing")
        completed.append(current)
def show_completed(completed):
    for model in completed:
        print(f"{model} has been printed")
unprinted=['phone case','robot pendant','dodecahedron']
completed=[]
print_models(unprinted[:],completed)
#[:]表示创建的副本，不会破坏原列表
show_completed(completed)
print(unprinted)

#8.9
def show_message(text):
    for every_texy in text:
        print(every_texy)
list=['hi','hello','gay']
show_message(list)

#8.10
def show_message(text,new_text):
    for every_text in text:
        print(every_text)
        new_text.append(every_text)
list=['hi','hello','gay']
new_text=[]
show_message(list,new_text)
print(list,'\n',new_text)

#8.11
def show_message(text,new_text):
    while text:
        every_text=text.pop()
        print(every_text)
        new_text.append(every_text)
list=['hi','hello','gay']
new_text=[]
show_message(list[:],new_text)
print(list,'\n',new_text)

def make_pizza(*toppings):
#星号*表示创建元组
    print("making pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(size,*toppings):
    print(f"making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

def build_profile(first,last,**user_info):
#两个星号**表示创建字典，包含函数收到的其他所有明值对
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

#8.12
def sandwich_order(*foods):
    print("here are the menu:")
    for food in foods:
        print(f"customer have ordered {food}")
sandwich_order('egg')
sandwich_order('egg','mushroom')
sandwich_order('egg','cheese','beaf')

#8.13
def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('sun','key',location='china',field='physics',gender='male')
print(user_profile)

#8.14
def make_car(manufacturer,model,**car_info):
    car_info['manufacturer']=manufacturer
    car_info['model size']=model
    return car_info
car1=make_car("telsla","y",price=15)
car2=make_car('byd','qin',price=15,color='white')
car3=make_car('xiaopeng','u')
print(car1,car2,car3)

import pizza
#导入整个模块的函数
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushroom','green peppers','extra cheese')

#导入模块的特定函数
from pizza import make_pizza
make_pizza(10,'egg')

#函数或者模块改名
from pizza import make_pizza as mp
mp(6,'beaf')

import pizza as p
p.make_pizza(11,'bacon')

#导入模块所有函数
from pizza import *
make_pizza(16,'pepp')