#!/usr/bin/python3.5
from bs4 import BeautifulSoup
from urllib.request import urlopen


# user_input = input("Enter City: ")
# City = user_input;
# user_input = input("Enter Item name: ")
# Item = user_input;

City = "chico"
Item = "xbox"

url = "https://%s.craigslist.org/search/sss?query=%s" %(City, Item)
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

NumListings = int(soup.find('span', class_='totalcount').text)
file = open("pid.txt", "w")
counter = 0

while counter < NumListings:
    for listing in soup.find_all('p'):
        if counter > NumListings:
            break;
        a =listing.find('a', class_= 'result-title hdrlnk')
        posttitle= a.text.replace(',','')
        post_link = a['href']
        postprice = listing.find('span', class_='result-price')
        if postprice != None:
            postprice = postprice.text
        #city
        postcity = listing.find('span', class_='result-hood')
        if postcity != None:
            postcity = postcity.text[2:-1].upper().replace(',','')
        postdate = listing.find('time', class_='result-date')['datetime']
        print("%s,%s,%s,posted:%s,%s" % (posttitle, postprice,postcity, postdate, post_link))
        counter = counter + 1
        url = "https://%s.craigslist.org/search/sss?s=%s&query=%s" %(City, counter, Item)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
