
word = input("Word: ")
if len(word) > 30 :
    print("invalid width >30 !!!!!!")
    exit()
pad = 30 - len(word)
leftPad = pad // 2
rightPad = pad - leftPad
print("*" + " " * leftPad + word + " " * rightPad + "*")