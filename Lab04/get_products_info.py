from bs4 import BeautifulSoup
import requests

def get_products_info(url, limit=5):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        products_characteristic = soup.find_all("a", class_="font-bold d-block mt-md-2 mb-1")
        products_price = soup.find_all("div", class_="real-price font-bold")

        products_info = []

        index = 0

        for characteristic, price in zip(products_characteristic, products_price):
            characteristic = characteristic.get_text(strip=True)
            price = price.find("span").get_text(strip=True)
            price = price.replace(".", "")
            price = float(price[:-2] + "." + price[-2:])

            brand, name, memory, color = characteristic.split(",")

            products_info.append({brand: brand.strip(), name: name.strip(), memory: memory.strip(), color: color.strip(), price: price})

            index += 1

            if index >= limit:
                return products_info

        return products_info

    else:
        print("HTTP request failed. Error code: ", response.status_code)
        return None