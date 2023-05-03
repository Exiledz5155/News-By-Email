import requests

api_key = "d41f75527e9248a18e3e112a415d22cf"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-04-03&sortBy=publishedAt&apiKey=" \
      "d41f75527e9248a18e3e112a415d22cf"

# Make the request
request = requests.get(url)

# Get a dictionary with the data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

