word = input("entrer ur word : ").lower()

vowels = ['e', 'o', 'a']

for v in vowels : 
    if word.__contains__(v) :
        print (f"{v} found")
    else :
        print (f"{v} not found")