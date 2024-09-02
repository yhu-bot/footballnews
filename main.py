import requests
from fantasy_agent.scrap import fetch_html

if __name__ == "__main__":
    url = 'https://www.fantasypros.com/nfl/injury-news.php'
    html_content = fetch_html(url)
    if html_content:
        with open('fetched_page.html', 'wb') as file:
            file.write(html_content)
        print("HTML content saved to 'fetched_page.html'")