class DestinationNotFoundError(Exception):
    pass

class InsufficientBatteryError(Exception):
    pass

def navigate_av(destinations, battery_level, miles_per_unit):
    def get_user_input():
        return input("Enter your destination: ")

    def calculate_distance(destination):
        # In a real system, this would calculate the actual distance
        # For this example, we'll use a simple dictionary
        distances = {
            "Home": 50,
            "Work": 30,
            "Supermarket": 10,
            "Park": 20
        }
        if destination not in distances:
            raise DestinationNotFoundError("Destination not found in the predefined list.")
        return distances[destination]

    def check_battery(distance):
        max_distance = battery_level * miles_per_unit
        if distance > max_distance:
            raise InsufficientBatteryError(f"Insufficient battery. Can cover {max_distance:.2f} miles. " 
                                           f"Need {distance - max_distance:.2f} more miles of charge.")

    try:
        destination = get_user_input()
        distance = calculate_distance(destination)
        check_battery(distance)
        print(f"Navigating to {destination}. Distance: {distance} miles.")
    except DestinationNotFoundError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
destinations = ["Home", "Work", "Supermarket", "Park"]
battery_level = 20  # units of battery
miles_per_unit = 2  # miles per unit of battery

navigate_av(destinations, battery_level, miles_per_unit)