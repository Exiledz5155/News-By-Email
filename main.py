import requests
from send_email import send_email


api_key = "d41f75527e9248a18e3e112a415d22cf"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-04-03&sortBy=publishedAt&apiKey=" \
      "d41f75527e9248a18e3e112a415d22cf"

# Make the request
request = requests.get(url)

# Get a dictionary with the data
content = request.json()

# Create a list to store titles and descriptions
message = ""

# Access the article titles and description
for index, article in enumerate(content["articles"]):
    if article["title"] is not None:
        message = message + f"Title: {article['title']} \nDesciption: {article['description']} \n\n"

message = message.encode("utf-8")
send_email(message)