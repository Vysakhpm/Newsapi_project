import requests
import pandas as pd
from textblob import TextBlob

# API Key and Endpoint
API_KEY = "a4cc5a1933184ec28d214d75a8f0025e"  
URL = f"https://newsapi.org/v2/everything?q=tesla&from=2024-12-17&sortBy=publishedAt&apiKey={API_KEY}"

def fetch_news_data():
    """
    Fetch news data from the News API and process it.
    """
    try:
        # Make a request to the News API
        response = requests.get(URL)
        if response.status_code != 200:
            print(f"Error fetching data: HTTP {response.status_code}")
            return None

        # Parse the response JSON
        news_data = response.json()
        articles = news_data.get("articles", [])
        if not articles:
            print("No articles found in the response.")
            return None

        # Process the articles and calculate sentiment
        table_data = []
        for article in articles:
            timestamp = article.get("publishedAt")
            author = article.get("author")
            description = article.get("description")
            sentiments_score = TextBlob(description).sentiment.polarity if description else 0.0

            table_data.append({
                "timestamp": timestamp,
                "author": author,
                "sentiments_score": sentiments_score,
                "description": description
            })

        # Convert to DataFrame
        return pd.DataFrame(table_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to fetch and display news data.
    """
    print("Fetching news data...")
    news_df = fetch_news_data()

    if news_df is not None and not news_df.empty:
        print("\nTop 5 News Articles:\n")
        print(news_df.head())  # Display the first 5 rows
        print("\nFull DataFrame saved to 'news_data.json'.")
        news_df.to_json("news_data.json", index=False)  # Save to a CSV file
    else:
        print("No data available.")
        


if __name__ == "__main__":
    main()