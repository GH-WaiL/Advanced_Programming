name = input("Please enter your name: ")

if name == 'VIP' :
    print("Enjoy the show for free!")
else :
    Ticket = int(input("How many tickets would you like to buy? "))
    TicketPrice = 15.50
    TotalCost = Ticket * TicketPrice
    print("The total cost is " , TotalCost)
    print("Enjoy your tickets!")