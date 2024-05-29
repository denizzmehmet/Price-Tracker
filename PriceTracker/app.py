import smtplib
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Your User-Agent"}

def check_price(url,target):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="product-name").get_text().strip()[:18]
    price_span = soup.find("span", attrs={"data-bind": "markupText:'currentPriceBeforePoint'"})
    if price_span:
        price = price_span.get_text().strip()
        price = int(''.join(filter(str.isdigit, price)))
    else:
        print("Price not found.")

    if (price < target):
        return send_mail(url,title)

def send_mail(url,title):
    sender = "ENTER YOUR SENDER EMAIL HERE"
    receiver = "ENTER A RECEIVER EMAIL HERE"
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(sender,password="ENTER YOUR EMAIL PASSWORD OR GMAIL APP PASSWORD HERE")
        subject = title + " It's at the price you wanted!!"
        body = "you can go from this link => " + url
        mailContent = f"To: {receiver}\nFrom: {sender}\nSubject: {subject}\n\n{body}"
        server.sendmail(sender, receiver, mailContent)
        return True
    except smtplib.SMTPException as e:
        print("Error:")
    finally:
        server.quit()

