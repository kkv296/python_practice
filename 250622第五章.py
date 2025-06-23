#第五章
alien_color=["green","yellow","red"]
for color in alien_color: 
    if(color=="green"):
        print("5 score")
    elif(color=="yellow"):
        print("10 score")
    else:
        print("15 score")

#fruit
fafruits=["liulian","watermellon","apple"]
checks=["liulian","watermellon","apple","strawberry","peach"]
for check in checks:
    if(check in fafruits):
        print(f"you really like {check}!")

#plain pizza
requested_toppings=[]
print(bool(requested_toppings))
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("finished making your pizza!")
else:
    print("are you sure you want a plain pizza?")

#5.8
users=["admin","b","c","d","e"]
for user in users:
    if(user=="admin"):
        print("hi admin,would you like to see a status report?")
    else:
        print(f"hello,{user},thank u for logging in again.")

#5.9
users=[""]
if users:
    for user in users:
        if(user=="admin"):
            print("hi admin,would you like to see a status report?")
        else:
            print(f"hello,{user},thank u for logging in again.")
else:
    print("we need to find some users!")

#5.10
current_users=["a","b","c","d","e"]
current_users_lower=[user.lower() for user in current_users]
new_users=["d","e","f","g","h"]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("plz input new name")
    else:
        print("its ok")
#5.10(new)
current_users=["a","b","c","d","e"]
new_users=["d","e","f","g","h"]
for new_user in new_users:
    if new_user.lower() in [u.lower() for u in current_users]:#更简洁
        print("plz input new name")
    else:
        print("its ok")

#5.11
lists=[1,2,3,4,5,6,7,8,9]
for l in lists:
    if l == 1:
        houzhui = "st"
    elif l==2:
        houzhui = "nd"
    elif l==3:
        houzhui = "rd"
    else:
        houzhui = "th"
    print(f"{l}{houzhui}")