people = int(input("How many people need a ride? "))
peopleInTaxi = int(input("How many people fit in one taxi? "))

if peopleInTaxi != 0 :
  nbTaxi = people // peopleInTaxi 
  if people % peopleInTaxi != 0 :
    nbTaxi = nbTaxi + 1 
    
  print(f"Number of taxis needed is :{nbTaxi}")
else :
  print(" The people can't fit in the taxi ")
