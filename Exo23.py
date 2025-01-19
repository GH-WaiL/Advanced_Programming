# nbr = int(input ("enter ur number : "))

# nbr_neg = nbr * -1

# while nbr_neg <= nbr :
#     if nbr_neg != 0:
#         print(nbr_neg)
#     nbr_neg += 1

try:
    n = int(input("Enter number : "))
    if n < 0:
        print("Number cannot be negative.")
        exit()
except ValueError:
    print("Invalid Input ")
    exit()

for i in range(-n , n+1):
    if i != 0:
        print(i)