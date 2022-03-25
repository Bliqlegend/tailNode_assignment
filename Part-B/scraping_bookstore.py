from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def ScrapeCurrpage(myurl):
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()
    aval = False
    page_soup = soup(page_html, "html.parser")

    bookshelf = page_soup.findAll(
        "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    filename = ("Al1000Books.csv")
    f = open(filename, "a")
    
    headers = "Title, Price , Availability, Rating \n"
    f.write(headers)
    
    # Printing the Titile,  Price, availability and Rating for Debug purposes
    for books in bookshelf:
    
        book_title = books.h3.a["title"]
        book_price = books.findAll("p", {"class": "price_color"})
        book_availability = books.find('p', {'class': 'instock availability'}).text.strip()
        book_Ratings = books.findAll("p", {"class": "star-rating One"})
        price = book_price[0].text.strip()
        if len(books.findAll("p", {"class": "star-rating One"}))!=0:
            book_rating = 1
        elif len(books.findAll("p", {"class": "star-rating Two"}))!=0:
            book_rating = 2
        elif len(books.findAll("p", {"class": "star-rating Three"}))!=0:
            book_rating = 3
        elif len(books.findAll("p", {"class": "star-rating Four"}))!=0:
            book_rating = 4
        elif len(books.findAll("p", {"class": "star-rating Five"}))!=0:
            book_rating = 5

        # print("Ratings")
        # print(book_Ratings)
     
        print("Title of the book : " + book_title)
        print("Price of the book : " + price)
        print("Availability of the book : " + book_availability)
        print("Rating of the book : " + str(book_rating))

    
        f.write(book_title + " , " + price +' , '+ book_availability +' , '+ str(book_rating) +"\n")
    
    f.close()

# Loop for fetching all 1000 books spread across all the pages, We know there are 50 pagesfr
for page_number in range(1,51): 
    myurl = f'https://books.toscrape.com/catalogue/page-{page_number}.html'
    print("__________________________________________________________\n")
    print(f"Page {page_number}")
    print("__________________________________________________________")
    ScrapeCurrpage(myurl)