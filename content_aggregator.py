import requests
from urllib.request import urlopen as uReq
import bs4
from bs4 import BeautifulSoup as soup
print("What you want to look at:")
print("makeup:1,books:2")
choice=input("choice:")
if choice=='1':
	page_url='https://www.walmart.com/search/?cat_id=1085666_1007040'
	client=uReq(page_url)
	html_page=client.read()
	client.close()
	page_soup=soup(html_page,"html.parser")#html parser
	containers_title=page_soup.findAll("div",{"class","search-result-product-title gridview"})
	containers_price_characteristic=page_soup.findAll("span",{"class","price-characteristic"})
	containers_mantissa=page_soup.findAll("span",{"class","price-mantissa"})
	filename="products.csv"
	headers="prodect,price\n"
	f=open(filename,"w")
	f.write(headers)
	print(len(containers_title))
	for i in range(len(containers_title)):
		title=containers_title[i].a["title"]
		container_charac=containers_price_characteristic[i].text
		container_mantissa=containers_mantissa[i].text
		print("product_name:"+str(title))
		print("price:"+"$"+str(container_charac)+"."+str(container_mantissa))
		f.write(title.replace(",","_")+","+"$"+container_charac+"."+container_mantissa+"\n")
	f.close()
                                        #By Miss.Robot
elif choice =='2':
	page_url='https://www.walmart.com/search/?cat_id=3920&query='
	client=uReq(page_url)
	html_page=client.read()
	client.close()
	page_soup=soup(html_page,"html.parser")#html parser
	containers_title=page_soup.findAll("div",{"class","search-result-product-title gridview"})
	containers_price_characteristic=page_soup.findAll("span",{"class","price-characteristic"})
	containers_mantissa=page_soup.findAll("span",{"class","price-mantissa"})
	filename="products.csv"
	headers="prodect,price\n"
	f=open(filename,"w")
	f.write(headers)
	print(len(containers_title))
	for i in range(len(containers_title)):
		title=containers_title[i].a["title"]
		container_charac=containers_price_characteristic[i].text
		container_mantissa=containers_mantissa[i].text
		print("product_name:"+str(title))
		print("price:"+"$"+str(container_charac)+"."+str(container_mantissa))
		f.write(title.replace(",","_")+","+"$"+container_charac+"."+container_mantissa+"\n")
	f.close()
else:
	print("Please choose 1 or 2 ")	
