#第六章
alien_0={"color":"green","points":5}
print(alien_0["color"])
print(alien_0["points"])
new_points=alien_0["points"]
print(f"you just earned {new_points} points!")
alien_0["x_position"]=0
alien_0["y_position"]=25
print(alien_0)

alien_0["speed"]="fast"
print(f"origin position:{alien_0['x_position']}")
if alien_0["speed"]=="slow":
    x_increment=1
elif alien_0["speed"]=="medium":
    x_increment=2
else:
    x_increment=3
alien_0["x_position"]=alien_0["x_position"]+x_increment
print(f"new position:{alien_0['x_position']}")

del alien_0["points"]
point_value=alien_0.get("points","no point value assigned")
#指定的值有可能不存在时，使用get
print(point_value)

#6.1
person={"first_name":"key","last_name":"v","age":22,"city":"beijing"}
print(person)

#6.2
fa_figure={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5
    }
print(f"a fa_figure is {fa_figure["a"]}")

for key,value in fa_figure.items():
    print(f"key:{key}")
    print(f"value:{value}")

for name,figure in fa_figure.items():
    print(f"{name.title()}'s favorite figure is {figure}.")
for figure in fa_figure.values():
    print(figure)

friends=["phil","sarah","a"]
for name in fa_figure.keys():
    if name in friends:
        favorite=fa_figure[name]
        print(f"{name.title()},i see u love {favorite}")
    else:
        print(f"{name},please take our poll!")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
    
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
for language in set(favorite_languages.values()):
#set可以剔除重复项
    print(language.title())

#6.5
dictionary={"nile":"egypt","huanghe":"china","changjiang":"china"}
for river in dictionary.keys():
    print(f"the {river.title()} runs through {dictionary[river].title()}")

for river,country in dictionary.items():
    print(river,country)

#嵌套
aliens=[]
#创建30个绿色外星人 range时创建序列，例如range(1，11)
for alien_number in range(30):
    new_alien={"color":"green","points":5,"speed":"slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"total number of aliens:{len(aliens)}")

for alien in aliens[0:3]:
    alien["color"]="yellow"
    alien["speed"]="medium"
    alien["points"]=10
for alien in aliens[:5]:
    print(alien)

users={
    "aeinstein":{
        "first":"albert",
        "last":"einstein",
        "location":"princeton"
    },

    "mcurie":{
        "first":"marie",
        "last":"curie",
        "location":"paris"
    },
}
for username,user_info in users.items():
    print(f"\nUsername : {username}")
    full_name=f"{user_info["first"]} {user_info["last"]}"
    location=user_info["location"]
    print(f"full name : {full_name.title()}")
    print(f"location : {location.title()}")

#6.7
people={
    "keykey":{"first_name":"key","last_name":"v","age":22,"city":"beijing"},
    "beibei":{"first_name":"bei","last_name":"a","age":24,"city":"seoul"},
    "nonnon":{"first_name":"non","last_name":"s","age":26,"city":"hongkon"},
    }
for peo,info in people.items():
    print(f"hi,{peo}")
    full_name_new=f"{info["first_name"]} {info["last_name"]}"
    age=info["age"]
    city=info["city"]
    print(full_name_new,age,city)

#6.8
wangcai={"owner":"a"}
qianqian={"owner":"b"}
pets=[wangcai,qianqian]
for i in pets:
    print(i["owner"])
#定义字典用“=”，键与值之间用“：”

#6.9
fa_place={
    "a":["beijing","seoul"],
    "b":["shanghai","shenzhen"],
    "c":["chongqing"],
    }
for name,place in fa_place.items():
    print(name)
    for p in place:
        print(p)

