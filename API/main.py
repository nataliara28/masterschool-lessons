import requests

# Request a random quote
response = requests.get("https://zenquotes.io/api/random")

print(response)  # This will show the response status - 200 if okay

print(response.json())  # convert the response to data in JSON

quote = response.json()[0]['q']  # Extract specific value, in this case the quote
print(quote)


# Request 50 random quotes
response = requests.get("https://zenquotes.io/api/quotes")
quotes = response.json()
for quote in quotes:
   print(quote['q'])


# Request the quote of today
response = requests.get("https://zenquotes.io/api/today")
quote = response.json()[0]
print(quote['q']) # Extract specific value, in this case the quote
print(quote['a']) # Extract specific value, in this case the author



