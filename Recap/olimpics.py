# Storing Athlete Names
# Question: Which data structure would you use to store the names in order,
# and how would you access the names of the athletes who finished first and last?


athletes = ["Usain Bolt", "Yohan Blake", "justin Gatlin"]

# First place
first_place = athletes[0]
print(first_place)

# Last place
last_place = athletes[-1]
print(last_place)


# Medal Tally
# Question: Which data structure would you use to map each country to its medal tally,
# and how would you access the number of gold medals won by a specific country?

medal_tally = {
    'USA': {
        "Gold": 45,
        "Silver": 56,
        "Bronze": 23
    },
    'Spain': {
        "Gold": 75,
        "Silver": 36,
        "Bronze": 13
    }
}

# Access number of Gold medal by USA
usa_gold_medals = medal_tally["USA"]['Gold']
print(usa_gold_medals)


# Olympic data!!

olympic_data = {
    "Athletics": {
        "100m Sprint": {
            "Usain Bolt": {"country": "Jamaica", "medal": "Gold"},
            "Yohan Blake": {"country": "Jamaica", "medal": "Silver"},
            "Justin Gatlin": {"country": "USA", "medal": "Bronze"},
        },
        "Long Jump": {
            "Mike Powell": {"country": "USA", "medal": "Gold"},
            "Bob Beamon": {"country": "USA", "medal": "Silver"},
            "Carl Lewis": {"country": "USA", "medal": "Bronze"},
        },
    },
    "Swimming": {
        "200m Freestyle": {
            "Michael Phelps": {"country": "USA", "medal": "Gold"},
            "Ryan Lochte": {"country": "USA", "medal": "Silver"},
            "Paul Biedermann": {"country": "Germany", "medal": "Bronze"},
        },
        "100m Butterfly": {
            "Michael Phelps": {"country": "USA", "medal": "Gold"},
            "Chad le Clos": {"country": "South Africa", "medal": "Silver"},
            "Laszlo Cseh": {"country": "Hungary", "medal": "Bronze"},
        },
    }
}

# Retrieve and print the medal won by "Usain Bolt" in the "100m Sprint" event.

usain_bolt_medal = None
print(usain_bolt_medal)

# Change "Yohan Blake's" medal in the "100m Sprint" from Silver to Gold.




# Add a new athlete "Andre De Grasse" from "Canada" who won the Bronze medal in the "100m Sprint".



# Remove "Justin Gatlin" from the "100m Sprint" due to disqualification.







# Loop Through Each Sport





# Loop Through Each Event Within a Sport





# Loop Through Each Athlete Within an Event





