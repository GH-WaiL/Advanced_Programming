TotalAmount = float(input("Total amount: "))
if TotalAmount <= 0 :
    print("Total amount can't be negative !!")
    exit()

nbItems = int(input("Number of items: "))
if nbItems <= 0 :
    print("Number of items can't be negative !!")
    exit()

Day = input("Day of the week: ")

weekDays = ["monday" , "thursday" , "wednesday" , "tusday" , "friday"]
weekEnds = ["saturday" , "sunday"]

Day = Day.lower()

if Day not in weekDays and Day not in weekEnds :
    print("Invalid Day !!!!!!!")
    exit()
dis = 0
if Day in weekEnds :
    dis += 0.2
else :
    dis += 0.1
if nbItems > 5 :
    dis += 0.05
discount = TotalAmount - TotalAmount*dis
print("Total price after discount: " , discount, " dinars")