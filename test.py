# import pdb

# def add(a, b):
#     pdb.set_trace()  # وضع نقطة التوقف هنا
#     return a + b

# result = add(2, 3)
# print (result)
# import logging
# logging.basicConfig(level=logging.DEBUG)

# def add(a, b):
#     logging.debug(f"a: {a}, b: {b}")
#     return a + b

# result = add(2, 3)
# print(result)  # سيتم طباعة 5

# n = 10 # number of layers in the pyramid
# row = "*"

# while n > 0:
#     print(" " * n + row)
#     row += "**"
#     n -= 1

input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
    print(input_string[index])
    index += 1