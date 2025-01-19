numbers = [1, 2, 3, 4, 5]
while True:
    try:
        index = int(input("Enter index (-1 to quit) : "))
        if index == -1:
            break
        if index < 0 or index >= len(numbers):
            print("Invalid index. Please try again.")
        else:
            value = int(input("Enter new value: : "))
            #numbers.insert(index, value)
            numbers[index] = value
            print(numbers)
    except ValueError:
        print("Invalid input. Please try again.")
print("Goodbye!")