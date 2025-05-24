import re
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    )
}

def extract_links(text):
    # Extract all Amazon or Flipkart URLs from the given text
    url_pattern = r"(https?://[^\s]+)"
    links = re.findall(url_pattern, text)
    return [link for link in links if "amazon" in link or "flipkart" in link]

def scrape_product_data(url):
    try:
        if "amazon" in url:
            return scrape_amazon(url)
        elif "flipkart" in url:
            return scrape_flipkart(url)
        else:
            return "❌ Unsupported link (only Amazon & Flipkart supported)."
    except Exception as e:
        return f"⚠️ Failed to scrape: {str(e)}"

def scrape_amazon(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle")
    price = soup.find("span", class_="a-price-whole")

    if not title:
        return "❌ Could not find Amazon product title."

    title_text = title.get_text(strip=True)
    price_text = price.get_text(strip=True) if price else "Not found"

    return f"🛒 *{title_text}*\n💰 Price: ₹{price_text}"

def scrape_flipkart(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title_tag = soup.find("span", {"class": "B_NuCI"})
    price_tag = soup.find("div", {"class": "_30jeq3 _16Jk6d"})

    if not title_tag:
        return "❌ Could not find Flipkart product title."

    title_text = title_tag.get_text(strip=True)
    price_text = price_tag.get_text(strip=True) if price_tag else "Not found"

    return f"🛒 *{title_text}*\n💰 Price: {price_text}"
