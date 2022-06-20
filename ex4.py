cars = 100
space_in_car = 5.0
drivers = 30
passenger = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passanger_per_car = passenger / cars_driven

print("Cars = ", cars)
print("Space in car = ", space_in_car)
print("Driver = ", drivers)
print("Passenger = ",passenger)
print("Cars not driven = ", cars_not_driven)
print("Cars driven", cars_driven)
print("Carpool Capacity = Cars Driven * Space in Car ","\n \t \t", cars_driven, "*", space_in_car, " = ", carpool_capacity) # \n untuk garis baru, \t untuk tab
print("Average passenger per car = Passenger / Cars Driven", "\n \t \t", passenger, " / ", cars_driven, " = ", average_passanger_per_car)

print("\n" * 3)

print("There are", cars, "cars available")
print("There only", drivers, " drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We need to put about", average_passanger_per_car, "in each car")