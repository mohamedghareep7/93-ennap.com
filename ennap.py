from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

all_products = []

driver = webdriver.Chrome()
driver.get("https://ennap.com/collections/laptops-notebooks")

big_container = driver.find_element(By.XPATH , '//div[@id="ProductGridContainer"]')
# print(big_container.get_attribute("outerHTML"))

container = big_container.find_elements(By.XPATH , './/div[@class="f-column product-column"]')
for items in container:

    description = items.find_element(By.XPATH , './/span[@class="reversed-link__text"]').text
    print("description :" , description)

    price = items.find_element(By.XPATH , './/span[@class="f-price-item f-price-item--sale"]').text
    print("price :" , price)

    try:
        discount = items.find_element(By.XPATH , './/span[@class="f-price-item f-price-item--regular"]/s').text
        print("price befor discount :" , discount)
    except:
        discount = "no discount found"
        print("price befor discount :" , discount)

    product_image = items.find_element(By.XPATH , './/img').get_attribute("src")
    print("product_image :" , product_image)

    product_link = items.find_element(By.XPATH , './/a').get_attribute("href")
    print("product_link :" , product_link)

    dict_products = {
        "description" : description ,
        "price" : price ,
        "discount" : discount ,
        "product_image" : product_image ,
        "product_link" : product_link ,
    }
    all_products.append(dict_products)

    print("="*20)

header = all_products[0].keys()
path = "all products.csv"

with open (path , "w" , encoding="utf-8" , newline='') as file :
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)
    