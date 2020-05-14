import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.nl/Samsung-Galaxy-Watch-Bluetooth-zilver/dp/B07G3S92WB/ref=sr_1_1?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3HI7Y8SFW0YMI&keywords=samsung%2Bgalaxy%2Bwatch%2B46mm&qid=1589482659&sprefix=samsu%2Caps%2C140&sr=8-1&th=1'

headers = {
    "User-Agent": '' # Paste your User agent between the '', search on google "My User Agent" to get yout user agent. ''
}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5].replace(',', '.'))

    if(converted_price < 200):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 200):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '') # First '' you're email, 2nd you're password

    subject = 'The product is Cheaper'
    body = 'Check your amazon link: https://www.amazon.nl/Samsung-Galaxy-Watch-Bluetooth-zilver/dp/B07G3S92WB/ref=sr_1_1?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3HI7Y8SFW0YMI&keywords=samsung%2Bgalaxy%2Bwatch%2B46mm&qid=1589482659&sprefix=samsu%2Caps%2C140&sr=8-1&th=1'

    msg = f"Subject: {subject}\n\n{body}";

    server.sendmail(
        '', # Email sender
        '',  # Email receiver
        msg
    )
    print('Email is send!')

    server.quit

while(True):
    check_price()
    time.sleep(1) # Set the time here that you want, this will make it check those seconds