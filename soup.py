import csv
import sys
from bs4 import BeautifulSoup

def process_div(div):
    try:
        d = {
          'street': div.find(class_='thoroughfare').text.encode('utf8'),
          'name': div.find(class_='views-field-title').find(class_='field-content').text.encode('utf8'),
          'city': div.find(class_='locality').text.encode('utf8'),
          'state': div.find(class_='state').text.encode('utf8'),
          'country': div.find(class_='country').text.encode('utf8'),
          'zipcode': div.find(class_='postal-code').text.encode('utf8'),
        }

    except AttributeError:
        d = {}

    return d

with open('wholefoods.html') as f:
	soup = BeautifulSoup(f.read(),'html.parser')

divs = soup.find_all('div',class_='views_row')

fields = ['name','street','city','state','zipcode']

writer = csv.DictWriter(sys.stdout,fieldnames=fields)
writer.writeheader()

for div in divs:
	row = process_div(div)
	if row: 
		writer.writerow(row)





