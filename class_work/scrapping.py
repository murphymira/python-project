from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.goodreads.com/quotes/tag/life"

response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('div', {"class": "quoteText"})

with open("loveQuote.csv", mode='w') as quote_csv:
    csv_write = writer(quote_csv)
    csv_write.writerow("Quote")
    for quote in quotes:
        q1 = quote.getText()
        csv_write.writerow([q1])

