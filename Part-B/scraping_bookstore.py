from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def ScrapeCurrpage(myurl):
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    bookshelf = page_soup.findAll(
        "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    filename = ("Al1000Books.csv")
    f = open(filename, "a")
    
    headers = "Title, Price\n"
    f.write(headers)
    
    # Printing the Titile and Price for Debug purposes
    for books in bookshelf:
    
        book_title = books.h3.a["title"]
        book_price = books.findAll("p", {"class": "price_color"})
        price = book_price[0].text.strip()
    
        print("Title of the book :" + book_title)
        print("Price of the book :" + price)
    
        f.write(book_title + "," + price+"\n")
    
    f.close()

# Loop for fetching all 1000 books spread across all the pages, We know there are 50 pagesfr
for page_number in range(1,51): 
    myurl = f'https://books.toscrape.com/catalogue/page-{page_number}.html'
    print("__________________________________________________________\n")
    print(f"Page {page_number}")
    print("__________________________________________________________")
    ScrapeCurrpage(myurl)