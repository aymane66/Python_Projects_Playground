import Functions as f

print("------------- Holiday Expenses -------------")
print("---- Hotel: ")
while True:
    nights = input("Nights: ")
    try:
        nights = int(nights)
        break
    except ValueError:
        print("Invalid input! Please enter a valid number of nights.")

print("---- Car rental: ")
while True:
    days = input("Days: ")
    try:
        days = int(days)
        break
    except ValueError:
        print("Invalid input! Please enter a valid number of days.")

print("---- Flight destination: ")
print("Destination options: Agadir - Casablanca - Rabat - Tangier")
while True:
    destination = input("Destination: ")
    if destination in ["Agadir", "Casablanca", "Rabat", "Tangier"]:
        break
    else:
        print("Invalid destination! Please choose from the provided options.")

print("-------------- Total expenses --------------")
print(f"Hotel expenses: {f.hotel_expenses(nights)} USD")
print(f"Car rental expenses: {f.car_rental(days)} USD")
print(f"Flight expenses: {f.flight_expenses(destination)} USD")
print()
print(f"Total: {f.total_expenses(nights, days, destination)} USD")