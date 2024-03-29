from newsapi import NewsApiClient
from datetime import datetime

api_key = "9a2431be001148cdba4bd27b6696c2f0"

newsapi = NewsApiClient(api_key=api_key)

def general_news():
    top_headlines = newsapi.get_top_headlines(language="en", category="general", page_size=60)

    # Extract the articles from the response
    articles = top_headlines["articles"]

    # Create a list to hold the news items
    news_items = []

    for article in articles:
        author = article["author"]
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        image = article["urlToImage"]

        # Create a dictionary to hold the news item
        news_item = {
            "author": author,
            "title": title,
            "description": description,
            "date": datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ'),
            "url": url,
            "image": image
        }

        news_items.append(news_item)

    return news_items

def tech_news():
    top_headlines = newsapi.get_top_headlines(language="en", category="technology", page_size=30)

    # Extract the articles from the response
    articles = top_headlines["articles"]

    # Create a list to hold the news items
    news_items = []

    # Loop through the articles and extract the author, title, URL, and image
    for article in articles:
        author = article["author"]
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        image = article["urlToImage"]

        # Create a dictionary to hold the news item
        news_item = {
            "author": author,
            "title": title,
            "description": description,
            "date": date,
            "url": url,
            "image": image
        }

        news_items.append(news_item)

    return news_items

def sports_news():
    top_headlines = newsapi.get_top_headlines(language="en", category="sports", page_size=30)

    # Extract the articles from the response
    articles = top_headlines["articles"]

    # Create a list to hold the news items
    news_items = []

    # Loop through the articles and extract the author, title, URL, and image
    for article in articles:
        author = article["author"]
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        image = article["urlToImage"]

        # Create a dictionary to hold the news item
        news_item = {
            "author": author,
            "title": title,
            "description": description,
            "date": date,
            "url": url,
            "image": image
        }

        news_items.append(news_item)

    return news_items

def business_news():
    top_headlines = newsapi.get_top_headlines(language="en", category="business", page_size=30)

    # Extract the articles from the response
    articles = top_headlines["articles"]

    # Create a list to hold the news items
    news_items = []

    # Loop through the articles and extract the author, title, URL, and image
    for article in articles:
        author = article["author"]
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        image = article["urlToImage"]

        # Create a dictionary to hold the news item
        news_item = {
            "author": author,
            "title": title,
            "description": description,
            "date": date,
            "url": url,
            "image": image
        }

        news_items.append(news_item)

    return news_items

def science_news():
    top_headlines = newsapi.get_top_headlines(language="en", category="science", page_size=30)

    # Extract the articles from the response
    articles = top_headlines["articles"]

    # Create a list to hold the news items
    news_items = []

    # Loop through the articles and extract the author, title, URL, and image
    for article in articles:
        author = article["author"]
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        image = article["urlToImage"]

        # Create a dictionary to hold the news item
        news_item = {
            "author": author,
            "title": title,
            "description": description,
            "date": date,
            "url": url,
            "image": image
        }

        news_items.append(news_item)

    return news_items


def health_news():
    top_headlines = newsapi.get_top_headlines(language="en", category="health", page_size=30)

    # Extract the articles from the response
    articles = top_headlines["articles"]

    # Create a list to hold the news items
    news_items = []

    # Loop through the articles and extract the author, title, URL, and image
    for article in articles:
        author = article["author"]
        title = article["title"]
        description = article["description"]
        date = article["publishedAt"]
        url = article["url"]
        image = article["urlToImage"]

        # Create a dictionary to hold the news item
        news_item = {
            "author": author,
            "title": title,
            "description": description,
            "date": date,
            "url": url,
            "image": image
        }

        news_items.append(news_item)

    return news_items