from bs4 import BeautifulSoup
import requests 
from csv import writer

url = "https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/showtype?gclid=Cj0KCQjworiXBhDJARIsAMuzAuzsjliytrKCQUWynjzo-Rv9rSdi9mHbWNTGynIs54NVbvxS2JODptwaAhn-EALw_wcB"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_= "wp-block property list")

with open('LagosApartment.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Description ', 'Location', 'Price_and_Duration']
    thewriter.writerow(header)
    for list in lists:
        title = list.find('h4', class_="content-title").text.replace('\n', '')
        address  = list.find('address', class_="voffset-bottom-10").text.replace('\n', '')
        price = list.find('span', class_="pull-sm-left").text.replace('\n', '')
        info = [title, address, price]
        thewriter.writerow(info)