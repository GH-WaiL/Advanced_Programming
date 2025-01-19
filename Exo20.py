user_list = []

while True :
    try:
        number = int(input("Enter a number : "))
        if number == 0:
            break
        user_list.append(number)
        print(f"Current List: {user_list} Sorted List: {sorted(user_list)} Descending Order : {sorted(user_list , reverse=True)}")
    except ValueError :
        print("Invalid Input , Please Enter int")

if user_list == [] :
    exit()

mean = sum(user_list) / len(user_list)
print(f"mean : {mean}")
if len(user_list) % 2 == 1 :
    median = user_list[len(user_list) // 2 + 1]
else :
    median =( user_list[len(user_list) // 2] + user_list[len(user_list) // 2 + 1]) / 2

print(f"median : {median}")

answer = input("do you want to save list to file ? (Y/n):")
if answer.lower() == "y" :
    filename = input("file name : ")
    with open(filename , "w") as f:
        for n in user_list:
            f.write(f"{n}\n")

answer = input("do you want to load list from file ? (Y/n):")
if answer.lower() == "y" :
    try:
        filename = input("Enter filename to load: ")
        with open(filename, 'r') as file:
            for line in file:
                user_list.append(int(line.strip()))
        print(f"user_list after load : {user_list}")
    except FileNotFoundError:
        print(f"File {filename} not found.")