import requests
from bs4 import BeautifulSoup
url="https://www.nike.com/fr/"

response=requests.get(url)
#print(response)
content=response.content
#print(content)
soup=BeautifulSoup(content,'html.parser')
img_1=soup.find_all('img')
#print(img_1)
image_urls=[img["src"] for img in img_1]
for url in image_urls:
    print("url of images :",url)
results=soup.find(id="VisualSearchInput")
print(results.prettify())


ripple_elements = results.find("span", class_="ripple")
print(ripple_elements)

id_element=soup.find(id="hf_header_find_a_store")
print(id_element)

id_element_1=soup.find(id="hf_header_label_help")
print(id_element_1)
id_element_2=soup.find(id="hf_title_signin_membership")
print(id_element_2)
id_element_3=soup.find(id="hf_title_joinus_membership")
print(id_element_3)
menu_elements=soup.find_all(role="menuitem")
print(menu_elements)
panier_element =soup.find("a", title="Articles du panier")
print(panier_element)
video_element=soup.find("playsinline",class_="vjs-tech")
print(video_element)
div_elements=soup.find_all()



