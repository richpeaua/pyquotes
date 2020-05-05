#!/usr/local/bin/python3

from bs4 import BeautifulSoup as bs
import requests
import time
import re

# def get_page(url):
#     page = requests.get(url)

#     return page.content

# def parse_quotes(page):
#     soup = bs(page, 'html.parser')



BASE_URL = 'https://www.goodreads.com/quotes?page='

PAGE_COUNT = 1

page = requests.get(BASE_URL + str(PAGE_COUNT))
soup = bs(page.content, "html.parser")

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('div', class_='quoteText')
    author = quote.find('span', class_='authorOrTitle')

    print(f'{text.text.strip()}\n')

# while running:
#     page = requests.get(BASE_URL + str(PAGE_COUNT))
#     soup = bs(page.content, "html.parser")
#     next_page = soup.find('a', rel='next')
#     try:
#         print(next_page.text)
#         PAGE_COUNT += 1
#     except:
#         print("End of quotes")
#         running = False
#     time.sleep(0.2)
# print(page.content.decode())

# soup = bs(page.content, "html.parser")

# job_elems = soup.find_all('section', class_='card-content')

# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     title = title_elem.text.strip()
#     company = company_elem.text.strip()
#     location = location_elem.text.strip()
    
#     print(f'Title: {title}\nCompany: {company}\nLocation: {location}\n')