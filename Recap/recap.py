# List

# Real-Life Example: Imagine you are organizing a party,
# and you need to keep track of the guests attending.
# A list is perfect for this because you have an ordered collection of names.


# List of party guests
guests = ["Peyman", "Marco", "Martha", "Marco"]



# Adding a new guest, How do we add a new guest?
guests.append('Jon')
print(guests)


# Removing a guest, how do we remove a guest from the list?
guests.remove("Marco")
guests.pop(0) # pass index or without index it will pop the last item in the list
del guests[-1]
print(guests)

# Accessing a specific guest, How do we access a specific guest?
print(guests[0]) # First index
print(guests[-1]) # last index


# When to use a list?

# When you need an ordered collection of items.
# When you might need to frequently add or remove items.
# When you need to access items by their position (index).

# Key Points:

# Lists maintain the order of elements.
# Elements can be accessed by their index (position).
# Lists are versatile and can store different data types.


# Dictionaries

# Real-Life Example:
# Continuing with the party planning,
# now imagine you need to keep track of each guest's RSVP status.
# A dictionary is ideal here because you can associate each guest's name (key)
# with their RSVP status (value).

# Dictionary of guests and their RSVP status
rsvp_status = {'Marco': "No", 'Jon': "Yes"}


# Adding a new guest's status, How do we add a new guest?
rsvp_status['Martha'] = 'Yes'

# Updating a guest's status, How do we update a guest's status?
rsvp_status['Marco'] = "Yes" # Overwrite the previous value
print(rsvp_status)

# Accessing the RSVP status of a specific guest, How do we access?
status_Jon = rsvp_status["Jon"]
print('is Jon comming to the party', status_Jon)


# When to Use a Dictionary:
# When you need to associate keys with values (like a name with an RSVP status).
# When you need to look up items based on a unique identifier (like a guest's name).
# When the order of items is not important

# Key Points:
# Dictionaries store key-value pairs.
# Keys must be unique and immutable (like strings).
# Values can be of any data type and can be changed.