# IMPORTING THE REQUIRED MODULES FOR SCRAPING
import requests
from bs4 import BeautifulSoup
import csv
import pandas as p

# Scraping
url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracke"

r=requests.get(url)
soup=BeautifulSoup(r.content, "html.parser")

# titles Scraping  of mobile phones
titles=soup.find_all("div", class_="_4rR01T")

# Rating Scraping of mobile phones
ratings=soup.find_all("div", class_="_3LWZlK")

# reviews Scraping of mobile phones
reviews=soup.find_all("span", class_="_2_R_DZ")

# prices Scraping of mobile phones
# price=soup.find_all("div", class_="_30jeq3 _1_WHN1")
prices=soup.find_all("div", class_="_25b18c")
# print(price)


# Storing scraped data into a list so that we can read easily

titles_list=[]
ratings_list=[]
reviews_list=[]
prices_list=[]

# iterating and appending into the lists

for titles_s, ratings_s, reviews_s, prices_s in zip(titles, ratings, reviews, prices):
    titles_list.append(titles_s.text)
    ratings_list.append(ratings_s.text)
    reviews_list.append(reviews_s.text)
    prices_list.append(prices_s.text)

# print(titles_list)


# store data into the csv files

# STEP1: STORING DATA FROM LIST FORMAT TO DICTIONARY FORMAT AS KEY AND VALUE PAIR
d={"titles_list":titles_list, "ratings_list": ratings_list, "reviews_list":reviews_list, "prices_list":prices_list}

# STEP2: USING PANDAS MODULE WE ARE CREATING DATAFRAME AND STORING DICTIONARY DATA OF variable "d"
model=p.DataFrame(data=d)


# STEP3: to_csv is a function in pandas used to store data in csv files
model.to_csv("Flipkart_Mobiles_Data.csv")
