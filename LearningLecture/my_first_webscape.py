from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/nz-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

# opening up connnection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class":"item-container "})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, price\n"

f.write(headers)

for container in containers:

	brand_container = container.findAll("a", {"class":"item-brand"})
	brand_name = brand_container[0].img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	price_container = container.findAll("li", {"class":"price-current"})
	product_price = price_container[0].strong.text

	print("brand_name: " + brand_name)
	print("product_name: " + product_name)
	print("product_price: " + product_price)

	f.write(brand_name.replace(",", "-") + "," + product_name.replace(",", "|") + "," + product_price.replace(",", " ") + "\n")

f.close()

