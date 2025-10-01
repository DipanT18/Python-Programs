#This program is written to demonstrate thre use of News API to fetch and display news articles.

import requests
import json

API_KEY = "734439f6531842388d83b65653e8f676"
BASE_URL = "https://newsapi.org/v2/top-headlines"

query = input("Enter the topic you want to search news for: ")
url = f"{BASE_URL}?q={query}&apiKey={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])
    if articles:
        for idx, article in enumerate(articles, start=1):
            print(f"\nArticle {idx}:")
            print(f"Title: {article.get('title')}")
            print(f"Description: {article.get('description')}")
            print(f"URL: {article.get('url')}")
            print("= " * 65)
    print("\nEnd of news articles.")

else:
    print("Failed to retrieve news articles.")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

