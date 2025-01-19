import os

# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Save the list to a file")
    print("9. Load the list from a file")
    print("10. Quit")

# Function to append an element to the list
def append_element(lst):
    try:
        element = int(input("Enter the element to append: "))
        lst.append(element)
        print(f"Element {element} appended.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Function to insert an element at a specific position
def insert_element(lst):
    try:
        index = int(input("Enter the index to insert at: "))
        element = int(input("Enter the element to insert: "))
        lst.insert(index, element)
        print(f"Element {element} inserted at index {index}.")
    except ValueError:
        print("Invalid input. Please enter integers.")
    except IndexError:
        print("Index out of range. Please enter a valid index.")

# Function to pop an element
def pop_element(lst):
    try:
        index = int(input("Enter the index to pop: "))
        popped_element = lst.pop(index)
        print(f"Element {popped_element} popped from index {index}.")
    except IndexError:
        print("Index out of range. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Function to remove an element
def remove_element(lst):
    try:
        element = int(input("Enter the element to remove: "))
        lst.remove(element)
        print(f"Element {element} removed.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except ValueError:
        print("Element not found in the list.")

# Function to sort the list
def sort_list(lst):
    lst.sort()
    print("List sorted.")

# Function to reverse the list
def reverse_list(lst):
    lst.reverse()
    print("List reversed.")

# Function to search for an element in the list
def search_element(lst):
    try:
        element = int(input("Enter the element to search for: "))
        if element in lst:
            print(f"Element {element} found in the list.")
        else:
            print(f"Element {element} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Function to save the list to a file
def save_to_file(lst):
    try:
        with open("list_data.txt", "w") as file:
            file.write(str(lst))
        print("List saved to file.")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Function to load the list from a file
def load_from_file():
    if os.path.exists("list_data.txt"):
        try:
            with open("list_data.txt", "r") as file:
                lst = eval(file.read())
            print("List loaded from file.")
            return lst
        except Exception as e:
            print(f"Error loading from file: {e}")
            return []
    else:
        print("File not found. Starting with an empty list.")
        return []

# Main program function
def main():
    numbers = [1, 2, 3, 4, 5]  # Initialize the list

    while True:
        display_menu()  # Display the menu
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue

        if choice == 1:
            append_element(numbers)
        elif choice == 2:
            insert_element(numbers)
        elif choice == 3:
            pop_element(numbers)
        elif choice == 4:
            remove_element(numbers)
        elif choice == 5:
            sort_list(numbers)
        elif choice == 6:
            reverse_list(numbers)
        elif choice == 7:
            search_element(numbers)
        elif choice == 8:
            save_to_file(numbers)
        elif choice == 9:
            numbers = load_from_file()
        elif choice == 10:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

        print(f"Updated list: {numbers}")  # Display updated list

# Start the program
if __name__ == "__main__":
    main()
