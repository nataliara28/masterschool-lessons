# Boolean lesson

# print(type(False))

# Comparison Operators

print(3 == 5) # equal to
print(3 != 5) # not equal to
print(3 < 5) # smaller/ less than
print(3 > 5)
print(3 <= 5)
print(3 >= 5)


# Boolean variables
temperature = 3

is_cold = temperature < 10

print('is_cold: ', is_cold)


# Logical Operators => and, or, not

num = int(input("Write a number: "))

# if num > 0 or num < 20: # or - and
#    print("number is between 0 and 20")
# else:
#    print("out of range")


if not (num > 0 and num < 20):
    print('out of range')
else:
    print('number is between 0 and 20')



# --------------------------------------------------------------------------

# Exercise: Baking Scenario

# --------------------------------------------------------------------------

# Find out what you can bake based on your ingredients.

# INGREDIENTS
flour = True
chocolate_chips = False
eggs = True
bananas = False
banana_flavoring = True
cream_cheese = True
vanilla_extract = False
lemon_juice = True

can_bake_chocolate_chip_cookies = flour and chocolate_chips and eggs
can_bake_banana_bread = flour and eggs and (bananas or banana_flavoring)
can_bake_cheesecake = cream_cheese and eggs and (vanilla_extract or lemon_juice)


# # RESULTS
print("Can I bake chocolate chip cookies?", can_bake_chocolate_chip_cookies)  # Output:
print("Can I bake banana bread?", can_bake_banana_bread)  # Output:
print("Can I bake cheesecake?", can_bake_cheesecake)  # Output:


# Bonus: Decide to make pancakes if you don't have specific ingredients for other recipes
# For pancakes you just need flour and eggs

can_make_pancakes = flour and eggs and not(chocolate_chips, bananas, banana_flavoring, cream_cheese, vanilla_extract, lemon_juice)


print('Should I bake pancakes? ', can_make_pancakes)


# Boolean functions
def all_above_100(numbers):
   # Loop through the list
   for num in numbers:
       # Check if it’s above 100
        if num <= 100:
           return False
   return True # If the loop completes, all numbers are above 100

result = all_above_100([123, 345, 133, 23, 156, 678])
print(result)