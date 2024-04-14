#filter() =    creates a collection of elements from an iterable,
#for which a function returns true
# filter(function, iterable)

friends = [("Rachel",19),
           ("Monica", 18),

            ("Phoebe", 17),

            ("Joey", 16),

            ("Chandler",21),

            ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies: print(i)

#another example:cars which are ford and above 2022
cars = (("Car_1", "Ford", 2022),
        ("Car_2", "Toyota", 2021),
        ("Car_3", "Ford", 2023),
        ("Car_4", "Honda", 2020),
        ("Car_5", "Ford", 2022))

filter_company = lambda car: car[1] == "Ford"
filtered_cars = list(filter(filter_company, cars))
filter_year = lambda car: car[2] >= 2022
filtered_year = list(filter(filter_company, filtered_cars))

for car in filtered_year:
    print(car)