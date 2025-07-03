#第九章类
import os
os.system('cls' if os.name == 'nt' else 'clear') 
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog=Dog('willie','6')
print(f"my dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

your_dog=Dog('lucy',3)
print(f"your dog's name is {your_dog.name}")
print(f"your dog is {your_dog.age} years old")
your_dog.sit()

#9.1and9.2
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_res(self):
        print(f"name is {self.name}")
        print(f"cuisine type is {self.cuisine_type}")
    
    def open_res(self):
        print("the restaurant is opening")

restaurant1=Restaurant('mixue','ice cream')
restaurant1.open_res()
restaurant1.describe_res()

restaurant2=Restaurant('ruixing','coffee')
restaurant2.open_res()

restaurant3=Restaurant('chayan','tea')
print(f"the name is {restaurant3.name}")
print(f"the cuisine type is {restaurant3.cuisine_type}")
restaurant3.open_res()

#9.3
class User:
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.lastname=last_name

    def describe_user(self):
        print(f"first name is {self.firstname}")
        print(f"last name is {self.lastname}")

    def greet_user(self):
        print(f"hi,{self.firstname} {self.lastname}")

user1=User('willian','jimmi')
user1.describe_user()
user1.greet_user()

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you cant roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

my_new_car=Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(21)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

#9.4
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_res(self):
        print(f"name is {self.name}")
        print(f"cuisine type is {self.cuisine_type}")
    
    def open_res(self):
        print("the restaurant is opening")

    def number(self,new_number):
        self.number_served=new_number
        print(f"{self.number_served} people")
    
    def increment_number_served(self,increment_number):
        self.number_served+=increment_number
        print(f"{self.number_served} people")

restaurant1=Restaurant('mixue','ice cream')
restaurant1.open_res()
restaurant1.describe_res()
restaurant1.number(2)
restaurant1.increment_number_served(50)

#9.5
class User:
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.lastname=last_name
        self.login_attempts=0

    def describe_user(self):
        print(f"first name is {self.firstname}")
        print(f"last name is {self.lastname}")

    def greet_user(self):
        print(f"hi,{self.firstname} {self.lastname}")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attemmpts(self):
        self.login_attempts=0

user1=User('willian','jimmi')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attemmpts()
print(user1.login_attempts)

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you cant roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"this car has a {self.battery_size} -kw/h battery")
    
    def get_range(self):
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225
        print(f"this car can go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)#调用父类的方法
        self.battery=Battery()
    
    def fill_gas_tank(self):
        print("this car doesnt have a gas tank!")

    def upgrade_battery(self):
        if self.battery.battery_size!=65:
            self.battery.battery_size=65

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()

new_car=ElectricCar('tesla','y',2021)
print(new_car.get_descriptive_name())
new_car.battery.describe_battery()
new_car.upgrade_battery()
new_car.battery.describe_battery()

#9.6
class IcecreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors

    def flavors_read(self):
        print("available flavors:")
        for flavor in self.flavors:
            print(flavor)
    
icecreamstand=IcecreamStand('name','icecream','milk','tea')
icecreamstand.flavors_read()
icecreamstand.describe_res()

#9.7
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(self.privileges)

admin=Admin('key','v')
admin.greet_user()
admin.show_privileges()

from random import randint#标准库是一组模块，已经安装在系统
print(randint(1,6))

from random import choice
players=['chales','martina','michael','florence','eli']
first_up=choice(players)
print(first_up)

#9.13
class Die:
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        i=1
        while i<11:
            i+=1
            print(randint(1,self.sides))
touzi=Die()
touzi.roll_die()

touzi10=Die(10)
touzi10.roll_die()

touzi20=Die(20)
touzi20.roll_die()

#9.14
import random
from random import choices
list=[2,4,12,55,23,77,9,4,11,41,'a','d','r','z','u']
random_ele=random.choices(list,k=4)#允许重复
print(f"if your choose {random_ele},you win!")

#9.15
import random
from random import sample
options=[1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
my_ticket=random.sample(options,4)
print(f'you have choose {my_ticket}')

count=1
while True:
    count+=1
    current_ticket= random.sample(options,4)
    if current_ticket==my_ticket:
        print("win!")
        print(count)
        break





