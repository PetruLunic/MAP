from get_products_info import get_products_info
from parse_url import parse_url

# Product info type:
# {
#     brand: string,
#     name: string,
#     memory: string,
#     color: string
#     price: float
# }

params = {
    # "modelType": ["Tablete", "Telefoane"],
    # "minPrice": "1000",
    # "maxPrice": "2000",
    "brand": ["samsung"],
    # "color": ["Alb", "Mov"],
    # "storage": ["128+GB"]
}

baseUrl = "https://flip.ro/magazin/"

url = parse_url(baseUrl, params)
products_info = get_products_info(url)
print(url)
if products_info:
    for brand, name, memory, color, price in products_info:
        print("Brand: ", brand)
        print("Nume: ", name)
        print("Memorie: ", memory)
        print("Culoare: ", color)
        print("Pret: ", price)
        print("\n")
else:
    print("Nu exista nici un produs cu asa parametri")