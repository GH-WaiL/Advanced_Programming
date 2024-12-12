
cityPopulation = []

city = input("city 1 : ")
i = 2
while city.lower() != "stop" :
    cityPopulation.append([city , len(city)*1000000])
    city = input(f"city {i} : ")
    i += 1

cityPopulation.sort(key=lambda x: x[1] , reverse=True)
print(cityPopulation)