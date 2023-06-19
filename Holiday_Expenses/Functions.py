def hotel_expenses(nights):
    return nights * 90


def car_rental(days):
    if days > 7:
        return days * 35 - 50
    elif days > 3:
        return days * 35 - 20
    else:
        return days * 35


def flight_expenses(destination):
    destinations = {
        "Agadir": 20,
        "Casablanca": 25,
        "Tangier": 40,
        "Rabat": 30
    }
    return destinations.get(destination, 0)


def total_expenses(nights, days, destination):
    return hotel_expenses(nights) + car_rental(days) + flight_expenses(destination)
