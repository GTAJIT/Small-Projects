import requests
import json

qures = input("Topic: ")
url = f"https://newsapi.org/v2/everything?q={qures}&from=2024-11-20&sortBy=publishedAt&apiKey=9506c488976a4db6ab182fd9fd425e73"

r = requests.get(url)
news = json.loads(r.text)

# Check if the response contains the "articles" key
if "articles" in news:
    for article in news["articles"]:
        print("Title: ", article["title"])
        print("Description: ", article["description"])
        print("-------------------------------------")
else:
    print("Error in response:", news)