import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    print(f"Fetching URL: {url}")
    # Send a GET request to the website
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful
    if response.status_code == 200:
        print("HTML content fetched successfully.")
        return response.content
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def parse_football_news(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all articles (assuming they are in <div> tags with class 'article')
    articles = soup.find_all('div', class_='article')
    
    # Extract relevant information from each article
    news = []
    for article in articles:
        title = article.find('h2').get_text() if article.find('h2') else 'No title'
        summary = article.find('p').get_text() if article.find('p') else 'No summary'
        link = article.find('a')['href'] if article.find('a') else 'No link'
        
        news.append({
            'title': title,
            'summary': summary,
            'link': link
        })
    
    return news







