from name_function import get_formatted_name

print("enter 'q' to quit")
while True:
    first=input("enter first name")
    if first=='q':
        break
    last=input("enter last name")
    if last=='q':
        break

    formatted_name=get_formatted_name(first,last)
    print(f"\tNeatly formatted name:{formatted_name}")
