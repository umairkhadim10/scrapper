import requests
import bs4 as soup
import pandas as pd


# function to get data from url

def get_products_data(url):
    response = requests.get(url)
    beautiful_soup = soup.BeautifulSoup(response.content, 'lxml')
    products = beautiful_soup.findAll(
        'div',
        attrs={'class': 'col-sm-4 col-lg-4 col-md-4'}
    )
    return products


# function to parse the each product data

def parse_product_data(products,total_products):
    data = [[]]
    row_id = 0

    for items in products:
        # scrape the product based on total_prodcuts which user wants to see
        if row_id >= total_products:
            break   
        
        # scrape the detail of items
        price = items.find('h4', attrs={'class': 'pull-right price'})
        for pr in price:
            price_value = pr

        description = items.find('p', attrs={'class': 'description'})
        for des in description:
            description_value = des
            
        title = items.find('a')
        for tit in title:
            title_value = tit
        row_id += 1
        data.insert(row_id, [title_value, price_value, description_value])

    return data


# function to save product data in csv file

def save_to_csv(products_data):
    df = pd.DataFrame(
        products_data,
        columns=['title', 'price', 'description']
        )
    df.to_csv('productdata.csv')
    print("Congratulations!! your data is saved in CSV file Open CSV fiel to see the product data")


"""
funtion for get data from url then sendit to parser 
to parse the products and finally send parsed data to 
save function to save data in csv file

"""

def scrape_product_data(url, total_products):
    products = get_products_data(url)
    if len(products) < total_products:
        print("website have only {} products".format(len(products)))
    products_data = parse_product_data(products,total_products)
    save_to_csv(products_data)


# call main function to scrape our data

if __name__ == "__main__":
    # Check for Integer Input
    while True:
        try:
            total_products = int(input("Enter the total products you want to scrape :"))
            break
        except ValueError:
            print("you have Entered Wrong Value Please Enter an Integer number")

    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    scrape_product_data(url, total_products)
