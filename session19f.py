import requests
import json

url = "https://newsapi.org/v2/everything?q=tesla&from=2021-05-23&sortBy=publishedAt&apiKey=e3b47176c4de496985d4f116bf34a16c"
response = requests.get(url)
news = json.loads(response.text)


print(news["articles"])
for i in range(0, len(news["articles"])):
    print(news["articles"][i]["author"])
