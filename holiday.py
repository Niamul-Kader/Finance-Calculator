def hotel_cost(num_nights):
    # Assume £150 per night
    return 150 * num_nights


def plane_cost(city_flight):
    # Prices for different cities
    if city_flight == "New York":
        return 400
    elif city_flight == "London":
        return 300
    elif city_flight == "San Francisco":
        return 500
    else:
        return 250  # Default price if city not found


def car_rental(rental_days):
    # Assume £60 per day
    return 60 * rental_days


def holiday_cost(city_flight, num_nights, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    return total_hotel_cost + total_plane_cost + total_car_rental_cost


city_flight = input("Enter the city you will be flying to (e.g., New York, London, San Francisco): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))


total_cost = holiday_cost(city_flight, num_nights, rental_days)
print("\nHoliday Details:")
print("Destination:", city_flight)
print("Number of Nights at Hotel:", num_nights)
print("Number of Days for Car Rental:", rental_days)
print("Total Cost:", total_cost)