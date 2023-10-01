# Created Homework branch for the main file
cities = \
    {
        'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk'],
        'USA': ['New York', 'Los Angeles', 'Chicago'],
        'Germany': ['Berlin', 'Hamburg', 'Munich'],
        'France': ['Paris', 'Lyon', 'Marseille'],
        'UK': ['London', 'Manchester', 'Bristol']
    }
countries = list(cities.keys())
user_input = input("Enter a city: ")


def find_country(cities: dict, user_input: str):
    for key, value in cities.items():
        if user_input in value:
            print(f"{user_input.title()} in the {key}")
