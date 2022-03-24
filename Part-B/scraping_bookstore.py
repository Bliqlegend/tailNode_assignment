from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def ScrapeCurrpage(myurl):
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()
    
    page_soup = soup(page_html, "html.parser")
    
    # Finding the card and writing in the File
    bookshelf = page_soup.findAll(
        "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    filename = ("Al100Books.csv")
    f = open(filename, "w")
    
    headers = "Title, Price\n"
    f.write(headers)
    
    # Printing out Title and price in terminal (For debug purposes)
    for books in bookshelf:
    
        book_title = books.h3.a["title"]
        book_price = books.findAll("p", {"class": "price_color"})
        price = book_price[0].text.strip()
    
        print("Title of the book :" + book_title)
        print("Price of the book :" + price)
    
        f.write(book_title + "," + price+"\n")
    
    f.close()

# Loop for fetching all 1000 books spread across all the pages, We know there are 50 pages from observation
for page_number in range(1,51): 
    myurl = f'https://books.toscrape.com/catalogue/page-{page_number}.html'
    print("__________________________________________________________\n")
    print(f"Page {page_number}")
    print("__________________________________________________________")
    ScrapeCurrpage(myurl)