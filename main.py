name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print(f"Hello {name}! He is {age} years old and your city is {city}.")
print("Hello {name}! He is {age} years old and your city is {city}.".format(name=name, age=age, city=city))
print(f"Hello %(name)s! He is %(age)i years old and your city is %(city)s." % {"name": name, "age": age, "city": city})
