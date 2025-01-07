# Dictionary
# Key value pairs

# Create or Initialize
example = {
    #"key": "value any type"
    'basket': ['apples', 'oranges'],
    'price': 45,
    'paid': False,
    1: True
}

# constructor dict()
example2 = dict(
    basket=['apples'],
    price=45,
    paid=True
)


# Accessing data
print(example['basket'])

print(example.get('prices'))

if example.get('prices') == None:
    print('we dont prices yet')
    example['prices'] = [23, 45, 56]

print(example)

duplicate_keys = {
    "key_1": 23,
}
duplicate_keys['key_1'] = True
print(duplicate_keys["key_1"])




# Add an item
example["name"] = "Natalia Rico"
# print(example)

# Remove an item
del example["name"]
print(example)
example.pop('basket')
print(example)


# Modify
example["names"] = 'Natalia R'
print(example)

students = {}

students["name"] = "Maria"
students["password"] = 12345
print(students)

if "password" in students:
    print("Security")



# Iterating

dogs = {
     "dog_001": {
         "name": "Buddy",
         "breed": "Golden Retriever",
         "age": 5,
         "owner": {
             "name": "Alice Johnson",
         },
     },
     "dog_002": {
         "name": "Max",
         "breed": "Beagle",
         "age": 3,
         "owner": {
             "name": "Bob Smith",
         },
     },
     "dog_003": {
         "name": "Bella",
         "breed": "German Shepherd",
         "age": 4,
         "owner": {
             "name": "Charlie Davis",
         },
     }
  }

# Just want the keys:
print(dogs.keys())

# Key
for key in dogs:
    print(key)

# Values
for value in dogs.values():
    print(value)

# Items
for key, value in dogs.items():
    print(key, value)


# Just want the keys in dog_001
for key in dogs['dog_001']:
    print(key)


# Just want the values in dog_001
for value in dogs['dog_001'].values():
    print(value)


# Just want the items in dog_001
for key, value in dogs['dog_001'].items():
    print(f"{key}, {value}")


# Retrieve the owner of a specific dog
owner_dog_1 = dogs['dog_001']['owner']['name']

print(owner_dog_1)


# Create a dictionary representing a vehicle with keys "brand", "model", and "year".
# Add a new key "color" with the value "blue".
# Change the "year" to the current year.
# Print out all keys, all values, and the full dictionary.

# Step1
vehicle = {
    'brand': 'Audi',
    'model': 'Q3',
    "year": 2012
}

# Step2
vehicle['color'] = "blue"

print(vehicle)

#Step3
vehicle['year'] = 2025

#Step4
# Print out all keys, all values, and the full dictionary.

print("keys", vehicle.keys())
print("values", vehicle.values())
print("Full", vehicle)