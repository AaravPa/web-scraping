#Selenium is used to interact with the webpage. It is famously used for automation testing such as testing the functionality of a website
#(login/logout, etc) but can also be used to interact with the page such as clicking a button.
from selenium import webdriver
#bs4(BeautifulSoup) is a python module that is famously used for parsing text as html and then performing actions in it such as find specific html tags with a particular class/id,
#or listing out all the li tags inside the ul tags
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/Kartik/Web Scraping/venv/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class", "wikitable sortable jquery-tablesorter"}):
            th_tags = tr_tag.find_all("th")
            temp_list = []
            for index, th_tag in enumerate(th_tags):
                if index == 0:
                    temp_list.append(th_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
