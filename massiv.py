# Create a list of dictionaries representing cities
cities = [
    {"name": "New York", "population": 8398748, "area_sq_km": 468.9},
    {"name": "Los Angeles", "population": 3990456, "area_sq_km": 1302},
    {"name": "Chicago", "population": 2705994, "area_sq_km": 606.1},
    {"name": "Houston", "population": 2320268, "area_sq_km": 637.5},
    {"name": "Phoenix", "population": 1680992, "area_sq_km": 1340},
]

# Sort the cities by population in ascending order
sorted_cities_by_population = sorted(cities, key=lambda x: x["population"])

# Print the sorted cities
for city in sorted_cities_by_population:
    print(f"{city['name']}: Population - {city['population']}")

# Sort the cities by area in descending order
sorted_cities_by_area = sorted(cities, key=lambda x: x["area_sq_km"], reverse=True)

# Print the sorted cities
for city in sorted_cities_by_area:
    print(f"{city['name']}: Area - {city['area_sq_km']} sq km")