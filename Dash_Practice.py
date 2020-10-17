cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh','Mars', 'New York']
populations = [680250,117070,304391,1683,8406000]
states = ['MI', 'MI','PA', 'NY']

city_tuples = zip(cityNames, populations, states) # zip takes list and creates a list of tuples

class City:
    def __init__(self, n,p,s):
        self.name = n
        self.population = p
        self.state = s
    def __str__(self):
        return '{},{} (pop: {})'.format(self.name,self.state,self.population)

print("Without using list comprehension")
cities = []
for n in city_tuples:  # for every single value(every single tuple) in the city_tuples's tuple list
    name, pop,state = n  # take a single tuple and store it in name pop and state respectfully
    cityInstance = City(name,pop, state) # now use those values to create an instance of the City class that needs those 3 arguments and store it in the variable 'cityInstance'
    cities.append(cityInstance)  # cities is now a list of City instances
    print(cities)  # prints a list of the instances

    
#Zero out cities for example below

cities = []
print("\n")


# or we can use list comprehension :-

cities = [City(n,p,s) for (n,p,s) in city_tuples]
print("Using List Comprehension",cities)     # gives same result as the print statement above BUT need to comment the above code for the code below to work
