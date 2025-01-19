# word = input("enter ur word : ")
# i = 0
# word_ = ""
# while i < len(word):
#     print(f"{word[i]} *")
#     word_ = word_ + word[i] + "*" # word += word[i] + "*"
#     i = i + 1
# print(word_)

string = input("Please type in a string : ")
line = ""
for i in string:
    print(i + "*")
    line += i + "*"

print(line)