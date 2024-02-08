import requests
from bs4 import BeautifulSoup
import json

def extract_urls(url, keyword):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            urls = [link['href'] for link in links]
            related_urls = [link for link in urls if keyword in link.lower()]
            absolute_urls = set()
            for link in related_urls:
                if link.startswith('http'):
                    absolute_urls.add(link)
                elif link.startswith('/'):
                    absolute_urls.add(url + link)
            return list(absolute_urls)
        else:
            print(f"Error: Unable to fetch URL ({response.status_code})")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    target_url = "https://coinmarketcap.com/currencies/polygon/"
    keyword = "polygon"
    extracted_urls = extract_urls(target_url, keyword)
    if extracted_urls:
        output_file = "extracted_polygon_urls.json"
        with open(output_file, "w") as file:
            json.dump(extracted_urls, file, indent=4)
        print(f"Extracted URLs related to Polygon have been saved to '{output_file}'.")
