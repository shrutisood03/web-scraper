import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_static(url):
    print("Trying STATIC scraping...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Educational Scraper)"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        print("Static request failed")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # try to find some text
    text = soup.get_text(strip=True)

    if len(text) < 100:
        print("Very little content found")
        return None

    print("Static scraping SUCCESS")
    return soup


def scrape_dynamic(url):
    print("Trying BROWSER scraping...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(5)  # wait for JS

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    print("Browser scraping SUCCESS")
    return soup


def scrape(url):
    soup = scrape_static(url)

    if soup is None:
        soup = scrape_dynamic(url)

    return soup

import json

def extract_data(soup):
    data = {}

    # Page title
    data["title"] = soup.title.text if soup.title else "No title"

    # Headings
    data["headings"] = {
        "h1": [h.text.strip() for h in soup.find_all("h1")],
        "h2": [h.text.strip() for h in soup.find_all("h2")],
        "h3": [h.text.strip() for h in soup.find_all("h3")],
    }

    # Links
    data["links"] = []
    for link in soup.find_all("a", href=True):
        data["links"].append({
            "text": link.text.strip(),
            "url": link["href"]
        })

    return data

if __name__ == "__main__":
    url = input("Enter website URL: ")
    soup = scrape(url)

    if soup:
        extracted_data = extract_data(soup)

        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=2, ensure_ascii=False)

        print("\nScraping complete!")
        print("Data saved to output.json")

