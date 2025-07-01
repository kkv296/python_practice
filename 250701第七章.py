#第7章
import os
os.system('cls' if os.name == 'nt' else 'clear') 

#input输入
message=input("tell me something, and i will repeat it back to you:\n")
print(message)

name=input("plz enter your namr:")
print(f"\nhello,{name}!")

promt="if you share your name,we can personalize the message you see."
promt+="\nwhats your name?"
name=input(promt)
print(f"hello,{name}")

age=input("how old are u?")
age=int(age)
print(age>=18)

number=input("enter a number,i will tell you if its even or odd:")
number=int(number)
if number%2==0:
    print(f"\nthe number {number} is even")
else:
    print(f"\nthe number {number} is odd")

#7.1
car=input("what kind of car would you like to rent?")
print(f"let me see if i can find a {car}")

#7.2
people_number=input("how many people?")
people_number=int(people_number)
if people_number>8:
    print("no empty table")
else:
    print("there is empty table")

#7.3
number=input("enter a number")
number=int(number)
if number%10==0:
    print("its an integer number of 10 ")
else:
    print("its not an integer of 10")

#while循环
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

prompt="\ntell me something ang i will repeat it back to you"
prompt+="\nenter 'quit' to end the program."
message=""
while message!='quit':
    message=input(prompt)

if message!='quit':
    print(message)
#需要两次检测

#更优雅的写法(哨兵控制)
prompt="\ntell me something ang i will repeat it back to you"
prompt+="\nenter 'quit' to end the program."
message=input(prompt)
while message!='quit':
    print(message)
    message=input(prompt)

#使用flag
prompt="i will repeat it back,enter'quit'to end"
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

#使用break
prompt="\nenter the name of a city you have visited"
prompt+="\nenter'qhit'when finished"
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f"id love to go to {city.title()}")

current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)
#7.4
while True:
    topping=input("enter your pizza topping:")
    if topping=='quit':
        break
    print(f"add {topping}")

#7.5
age=input("enter your age")
age=int(age)
if age<3:
    print("free")
elif age<12:
    print("10 dollar")
else:
    print("15 dollar")

unconfirmes_users=["alice","brian","candace"]
confirmed_users=[]
while unconfirmes_users:
    current_user=unconfirmes_users.pop()
    print(f"verifying users:{current_user.title()}")
    confirmed_users.append(current_user)
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets=['pet','cat','dog','goldfish','cat','rabbit']
print(pets)
while'cat'in pets:
    pets.remove('cat')
print(pets)

responses={}
polling_active=True
while polling_active:
    name=input("\nwhats your name?")
    response=input("\nwhich mountain would you like to climb?")
    responses[name]=response
    repeat=input("would u like to let another person respond?yes or no")
    if repeat=='no':
        polling_active=False
print("\npoll results")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")

#7.8
sandwich_orders=["niurou","pacon","salami"]
finished_orders=[]
for sandwich in sandwich_orders:
    print(f"i made your {sandwich} sandwich")
    finished_orders.append(sandwich)
print(finished_orders)

#7.9
sandwich_orders=["niurou","pastrami","pastrami","pacon","salami","pastrami"]
print("pastrami is sold out")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)

#7.10
dic={}
active=True
while active:
    name=input("whats your name?")
    place=input("where would you go for vacation?")
    dic[name]=place
    repeat=input("/nanother person?yes or no")
    if repeat=='no':
        active=False
print(dic)
for name,place in dic:
    print(f"{name} want to go {place} for vacation")