numbers = []
shoe_sizes = []
combined = []

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please try again.")

for i in range(1, n+1):
    numbers.append(i)
    shoe_sizes.append(i + 7)
print("Numbers List:", numbers, "Shoe Sizes List:", shoe_sizes)

# combine the two lists
combined = numbers + shoe_sizes
print("Combined List:", combined)

# combine the two lists 
combined = [(numbers[i], shoe_sizes[i]) for i in range(n)]# tuplet
print("Combined List:", combined)
#add duplicates

numbers.append(1) # duplicate
shoe_sizes.append(n+7) # duplicate
print("Added Duplicates: Numbers List:", numbers, "Shoe Sizes List:", shoe_sizes)

# remove duplicates method 1
unique_numbers = []
unique_shoe_sizes = []
for nbr in numbers:
    if nbr not in unique_numbers:
        unique_numbers.append(nbr)

for nbr in shoe_sizes: 
    if nbr not in unique_shoe_sizes:
        unique_shoe_sizes.append(nbr)

print("Remove Duplicate Method 1: numbers list", unique_numbers, "Shoe Sizes List:", unique_shoe_sizes)

# remove duplicates method 2
numbers = list(set(numbers))# set()  elimine les redandance apres on a retransformer a une liste autre fois avec list()
shoe_sizes = list(set(shoe_sizes))
print("Remove Duplicate Method 2: Numbers List:", numbers, "Shoe Sizes List:", shoe_sizes)

