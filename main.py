import requests
from send_email import send_email


topic = "tesla"

api_key = "d41f75527e9248a18e3e112a415d22cf"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=d41f75527e9248a18e3e112a415d22cf" \
      "language=en"

# Make the request
request = requests.get(url)

# Get a dictionary with the data
content = request.json()

# Create a list to store titles and descriptions
message = ""

# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = f"Subject: Today's News \n" + message + \
                            f"Title: {article['title']} \nDesciption: " \
                            f"{article['description']}\n" \
                            f"{article['url']}\n\n"

message = message.encode("utf-8")
send_email(message)