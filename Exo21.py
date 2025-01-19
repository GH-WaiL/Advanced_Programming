from math import sqrt

def length(lst):
    l = 0 
    for i in lst:
        l += 1
    return l

# 
def mean_func(lst):
    if lst == []:
        return 0
    s = 0
    for i in lst:
        s += i
    return s / len(lst)
    # we can also use the sum function return sum(lst) / len(lst)

def range_of_list(lst):
    if lst == []:
        return 0
    # we can use this return max(lst) - min(lst)
    max = lst[0]
    min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max - min

def median(lst):
    if lst == []:
        return 0
    lst.sort()
    if len(lst) % 2 == 1:
        return lst[length(lst) // 2]
    return (lst[length(lst) // 2 - 1] + lst[length(lst) // 2]) / 2

def standard_deviation(lst):
    if lst == []:
        return 0
    mean = mean_func(lst)
    s = 0
    for i in lst:
        s += (i - mean) ** 2
    return sqrt((s / length(lst))) 
    # or return (s / length(lst)) ** 0.5



def print_all(lst):
    statistics = {
        "length": length(lst),
        "mean": mean_func(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }
    print("Initial List:", lst)
    print("Length of List:", statistics["length"])
    print("Mean of List:", statistics["mean"])
    print("Range of List:", statistics["range"])
    print("Median of List:", statistics["median"])
    print("Standard Deviation of List:", statistics["standard_deviation"])

# test the functions
print()
numbers = [1, 2, 3, 4, 5]
print_all(numbers)

print()
numbers = []
print_all(numbers)

print()
numbers = [2]
print_all(numbers)

print()
numbers = [-1 , -2 , -3 , -4 , -5]
print_all(numbers)

print()
numbers = [1.2, 2.3, 3.4, 4.5, 5.6]
print_all(numbers)