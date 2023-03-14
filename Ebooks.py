import requests
from pprint import pprint
import pandas as pd

first_page = []
title = []
sub_title = []
authors = []
publication_year = []
publisher = []
price = []
description = []
book_url = []
image_url = []

base_link = 'https://www.ebooks.com/'
for i in range(1,2000):
    params = (
            ('pageNumber', str(i)),
            ('CountryCode', 'DE'),
            ('subjectId', '13'),
        )
    response = requests.get('https://www.ebooks.com/api/search/subject/', params=params)
    json_data = response.json()
    # print(json_data)
    keys = json_data.keys()
    # print(keys)
    books_data = json_data['books']
    # print(books_data)
    """
    title = books_data[0]['title']
    sub_title = books_data[0]['subtitle']
    authors = books_data[0]['authors'][0]['name']
    publication_year = books_data[0]['publication_year']
    publisher = books_data[0]['publisher']
    price = books_data[0]['price']
    description = books_data[0]['description']
    book_url = books_data[0]['book_url']
    image_url = books_data[0]['image_url']
    print(authors)
    
    print(image_url)
    
    """

    for data in books_data:
        title = data['title']
        sub_title = data['subtitle']
        authors = data['authors'][0]['name']
        publication_year = data['publication_year']
        publisher = data['publisher']
        price = data['price']
        description = data['description']
        book_url = data['book_url']
        image_url = data['image_url']



        first_page_data = {

            'title': title,
            'sub_title': sub_title,
            'authors': authors,
            'publication_year': publication_year,
            'publisher': publisher,
            'price': price,
            'description': description,
            'book_url': book_url,
            'image_url': image_url
        }
        first_page.append(first_page_data)

    data = pd.DataFrame(first_page)
    data.to_csv('ebook.csv', index=False)
