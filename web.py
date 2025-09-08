import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}

def product_details(prod_url: str) -> dict:
    prod_details = {}
    try:
        page = requests.get(prod_url, headers=headers)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')

        title_element = soup.find('span', attrs={'id': 'productTitle'})
        prod_details['title'] = title_element.get_text().strip() if title_element else 'Title not found'

        price_element = soup.find('span', attrs={'class': 'a-price'})
        prod_details['price'] = price_element.find('span', attrs={'class': 'a-offscreen'}).get_text().strip() if price_element else 'Price not found'

        rating_element = soup.find('span', attrs={'id': 'acrCustomerReviewText'})
        prod_details['rating'] = rating_element.get_text().strip() if rating_element else 'Rating not found'

        availability_element = soup.find('div', attrs={'id': 'availability'})
        prod_details['availability'] = availability_element.get_text().strip() if availability_element else 'Availability not found'

    except requests.exceptions.RequestException as e:
        print(f"Error fetching product details: {e}")
        return {}
    except Exception as e:
        print(f"Could not parse product details: {e}")
        return {}

    return prod_details

prod_url = input("Enter product URL: ")
details = product_details(prod_url)

if details:
    print("\n--- Product Information ---")
    print(f"Title: {details.get('title', 'N/A')}")
    print(f"Price: {details.get('price', 'N/A')}")
    print(f"Rating: {details.get('rating', 'N/A')}")
    print(f"Availability: {details.get('availability', 'N/A')}")
else:
    print("\nCould not retrieve product details. Please check the URL and try again.")