height = int(input("height : "))
if height < 0 :
    print("height invalid")
    exit()

width = int(input("width : "))
if width < 0 :
    print("invalid width")
    exit()

print ((" " + "#" * width) * height)

