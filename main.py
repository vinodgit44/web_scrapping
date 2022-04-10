from bs4 import BeautifulSoup
import requests
import lxml
#reading HTML file
with open('main.html','r') as page:
    content =page.read()


    #creating object of beautiful soup and pass the content of html file
    soup =BeautifulSoup(content,'lxml')

   # print(soup.prettify())   #printing html page  well structured
    tags_h5 = soup.find_all("h5")   #reading h5 tags
   # print(tags_h5)


    tags_h1=soup.find_all("h1") #reading h1 tags
   # print(tags_h1)


    course_card=soup.find_all('div', class_="card")

    for courses in course_card:
        course=courses.h5.text
        price=courses.a.text.split()[-1]  #grabbing only price word


        print(f"{course} costs {price}")
