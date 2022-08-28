import requests
import schedule
import time
from bs4 import BeautifulSoup
import smtplib
from playsound import playsound
#From selenium import webdriver



myList = []

def main():
    def myFunc():
        check_inventory()

    while True:
        myFunc()
        time.sleep(300)

def get_page_html(url):
    print("getting page")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print("Page status is ", page.status_code)
    return page.content


def check_item_in_stock(page_html):
    #soup = BeautifulSoup(page_html, 'html.parser')
    #out_of_stock_divs = soup.findAll("span", {"class": "justify-content-end"})
    #for a in out_of_stock_divs:
        #myList.append((a.text).lstrip().strip())
    soup = BeautifulSoup(page_html, 'html.parser')
    myButt = soup.find("button", class_="b-pdp-button_add btn m-primary m-shaking m-vertical-change m-icon")
    #print(myButt.contents)
    myList = str(myButt).split(" ")
    return myList

def check_inventory():
    #https://www.swatch.com/it-it/mission-to-the-moon-so33m100/SO33M100.html
    #https://www.swatch.com/it-it/clearly-gent-so28k100/SO28K100.html
    url = "https://www.swatch.com/it-it/mission-to-the-moon-so33m100/SO33M100.html"
    page_html = get_page_html(url)
    myList = check_item_in_stock(page_html)
    mySentence = 'disabled=""'
    if mySentence not in myList:
        send_email()
        print("Watch in stock!")
        playsound('C:/Users/Glennre92/PycharmProjects/pythonProject/venv/alarm.mp3')
    else:
        print("Out of stock")


def send_email():
    gmail_user = "test@gmail.com"
    gmail_password = "password"
    sent_from = gmail_user
    to = "test@yahoo.com"
    subject = "IN STOCK"
    body = "Watch in stock"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, body)
    server.close()

main()





