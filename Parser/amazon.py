import datetime
import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import pymongo

# MongoDB connection string
MONGO_URL = "mongodb+srv://mongoadmin:secretpass@cluster0.clh6g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "inventory"
COLLECTION_NAME ="items"

custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

visited_urls = set()

# Function to fetch the product information from URL
def get_product_info(url):
    response = requests.get(url, headers=custom_headers)
    if response.status_code != 200:
        print(f"Error in getting webpage: {url}")
        return None

    soup = BeautifulSoup(response.text, "lxml")

    name_element = soup.select_one("#productTitle")
    name = name_element.text.strip() if name_element else None

    price_element = soup.select_one('span.a-offscreen')
    price = price_element.text if price_element else None

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    return {
        "name": name, 
        "price": [price], 
        "timestamp": [timestamp],  # Array of price objects
        "url": url,
    }

# Function to scrape the product information for each URL
def parse_listing(product_urls, collection):
    global visited_urls
    page_data = []

    # Ensuring each URL is visited only once
    for url in product_urls:
        if url not in visited_urls:
            visited_urls.add(url)
            print(f"Scraping product from {url[:100]}", flush=True)
            product_info = get_product_info(url)
            if product_info:
                # Compare prices with previous prices
                previous_price = collection.find_one({"url": url}, {"price": 1})
                # if previous_price and previous_price.get("price") != product_info["price"]:
                #     print(f"Price changed for product {product_info['name']} at {url}. Previous price: {previous_price['price']}, New Price: {product_info['price']}")
                page_data.append(product_info)
            time.sleep(1)  # Introducing a delay between requests

    return page_data


def main():
    # Connect to MongoDB
    client = pymongo.MongoClient(MONGO_URL)
    db = client[DB_NAME]
    collection =  db[COLLECTION_NAME]

    MAX_ITERATIONS = 50


    data = []
    # List of the product URLs to scrape
    product_urls = [
        "https://www.amazon.com/Beats-Studio-Pro-Personalized-Compatibility/dp/B0C8PR4W22",
        "https://www.amazon.com/Logitech-Tenkeyless-Lightspeed-Mechanical-LIGHTSYNC/dp/B085RMD5TP",
        "https://www.amazon.com/Lenovo-IdeaPad-Display-Celeron-Graphics/dp/B0BLW25MB7"
    ]

    try:
        iteration = 0
        while True:
            
            global visited_urls
            visited_urls = set()
            
            data = parse_listing(product_urls, collection)
            df = pd.DataFrame(data)
            df.to_json("products.json") # Inserting data into a separate json file
            
            for item in data:
    # Check if price is a list and get the first element
                if isinstance(item["price"], list):
                    price_str = item["price"][0]  # Get the first element of the list
                else:
                    price_str = item["price"]  # If price is not a list, use it directly

    # Convert price from string to number
                price_as_number = float(price_str.replace("$", "").replace(",", ""))

    # Prepare the data to be inserted/updated
                formatted_data = {
                    "product": item["name"],
                    "prices": [{
                        "price": price_as_number,  # Converted price as a number
                        "date": item["timestamp"]
                    }]
                }

    # Update MongoDB
                collection.update_one(
                    {"product": item["name"]},  # Query to find the document
                    {
                        "$push": {"prices": {"$each": formatted_data["prices"]}}  # Append to the prices array
                    },
                    upsert=True  # Insert a new document if no match is found
                )



            
            print("Waiting before the next scraping...")

           # Generate a random delay between 2 and 6 hours
            delay_hours = random.uniform(2, 6)
            delay_seconds = delay_hours * 3600 # Convert hours to seconds
            # delay_seconds =30
            time.sleep(delay_seconds)

            iteration += 1

            if iteration >= MAX_ITERATIONS:
                print("Maximum iterations reached. Exiting...")
                break
    except KeyboardInterrupt:
        print("Scraping interrupted by user. Exiting...")
    except Exception as e:
        print(f"An error occurred: {str(e)}. Exiting...")

    finally:
        client.close() # Close MongoDB client connection
        
if __name__ == '__main__':
    main()
