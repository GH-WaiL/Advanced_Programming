price = float(input("Please type in a price: "))

if price < 0 : 
    print("Invalid price !!!!!!")
    exit()
    
Dinars = int(price)
Centimes = int((price - Dinars) * 100)

print("Dinars: " , Dinars)
print("Centimes: " , Centimes)