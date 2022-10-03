from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.rmit.edu.au/students/careers-opportunities/scholarships/coursework'

uClinet = uReq(url)
page_html = uClinet.read()
uClinet.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"cmp-list__item-content btn_Wrap_CTALink"})
filename = "scholarships.csv"
f = open(filename,"w")
headers = "Title, Description\n"

f.write(headers)

for container in containers:
	
	title = container.h3.text
	desc_container = container.findAll("p" , {"class":"short-desc-gen"})
	desc = desc_container[0].text

	print("title:" + title)
	print("description:" + desc)
	f.write(title + "," + desc.replace("," , " ") + "\n")
f.close()