# Mission - 1 (Clearing the Field)

def find_cleaned_(city_list):
    set_of_cities = set(city for city in city_list)
    cleaned_list = sorted(list(set_of_cities))
    return cleaned_list

cities = ["Mariupol", "Kharkiv", "Kyiv", "Severodonetsk", "Lysychansk", "Bakhmut", "Izium", "Kherson", "Zaporizhzhia", "Lviv", "Donetsk", "Luhansk", "Kharkiv", "Severodonetsk", "Izium" ]
cleaned_list = find_cleaned_(cities)
print(f"\nCleaned list: {cleaned_list}\n")

# Mission - 2 (High Alert Identification)

previous_intel = { "Mariupol", "Crimea", "Odessa", "Luhansk", "Bakhmut"}

assistance_requiring_cities = previous_intel.union(cleaned_list)
print(f"\nAid requiring cities: {assistance_requiring_cities}")

low_alert_cities = previous_intel ^ set(cleaned_list)
print(f"\nLow alert cities: {low_alert_cities}")

high_alert_cities = previous_intel.intersection(cleaned_list)
print(f"\nHigh alert cities: {high_alert_cities}\n")

# Mission - 3 (Detailed City Intel)

city_data = [("Kyiv", 3850000, 270), ("Kharkiv", 1551000, 130), ("Lviv",524401, 190), ("Odessa", 1667050, 160), ("Bakhmut", 2335000, 60), ("Mariupol", 8000000, 250), ("Luhansk", 4005000, 200)]

high_alert_cities_info = {city: details for city in high_alert_cities for details in city_data if details[0] == city}
print(f"\nInformation of cities with high alert: {high_alert_cities_info}")

total_population = sum([details[1] for details in high_alert_cities_info.values()])
print(f"\nTotal population: {total_population}")

total_aid_requests = sum([details[2] for details in high_alert_cities_info.values()])
print(f"\nTotal aid requests: {total_aid_requests}\n")

# Mission - 4 (Tracking Supply Distribution)

supplies = [("Kyiv", "Food", 500), ("Kursk", "Medicines", 200), ("Lviv", "Water", 300), ("Chelyabinsk", "Blankets", 100), ("Kharkiv", "Food", 150), ("Luhansk", "Tents", 600), ("Vladivostok", "Water", 400)]

supply_details = {details[0]: {details[1]: details[2]} for details in supplies}
print(f"\nSupply details: \n{supply_details}\n")