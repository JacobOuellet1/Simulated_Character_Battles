# AI Project (Superhero fight simulator)
# Author: Jacob Ouellet
# 4/1/2021
# Purpose: Scrape data from the website, superherodb.com and put it into an organized excel sheet to be used
# by our AI agent.
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import openpyxl

def main():
    get_links("https://www.superherodb.com/characters/male/superheroes/?page_nr=", 8)
    get_links("https://www.superherodb.com/characters/male/villains/?page_nr=", 6)
    get_links("https://www.superherodb.com/characters/female/superheroes/?page_nr=", 4)
    get_links("https://www.superherodb.com/characters/female/villains/?page_nr=", 2)

    get_data_from_links()


def get_links(path, max_page_num):

    i = 1
    while i <= max_page_num: # for each of the pages in male superheros
        binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        options = Options()
        options.binary = binary
        browser = webdriver.Firefox(firefox_options=options, executable_path="C:\\Users\\jacob\\PycharmProjects\\SuperHero_DB_Data_Scraper\\geckodriver.exe")
        browser.get(path + str(i))

        element = browser.find_element_by_xpath("/html/body/main/div/div[4]")
        links = element.find_elements_by_tag_name("li")
        f = open("links.txt", "a")
        for link in links:
            a_elm = link.find_element_by_css_selector("a")
            href = a_elm.get_attribute("href")
            f.write(href + "\n")
        i += 1
        browser.close()


def get_data_from_links():
    binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    options = Options()
    options.binary = binary

    f = open("links.txt", "r")
    line = f.readline()
    row = 0
    while line != '':
        browser = webdriver.Firefox(firefox_options=options, executable_path="C:\\Users\\jacob\\PycharmProjects\\SuperHero_DB_Data_Scraper\\geckodriver.exe")
        browser.get(line)
        data = []
        
        try:
            data.append(browser.find_element_by_css_selector(".col-10 > h1:nth-child(1)").text)                     # heroic_name
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append((browser.find_element_by_css_selector(".col-10 > h2:nth-child(2)")).text)                     # real_name
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector(".col-10 > h3:nth-child(3)").text)                        # universe
        except NoSuchElementException:
            data.append("N/A")
        try:
            x = browser.find_element_by_xpath("//*[contains(text(), 'Gender')]/parent::*")
            r = x.find_element_by_xpath("td[2]")
            data.append(r.text)     # gender
        except NoSuchElementException:
            data.append("N/A")
        try:
            x = browser.find_element_by_xpath("//*[contains(text(), 'Species')]/parent::*")
            r = x.find_element_by_xpath("td[2]")
            data.append(r.text)  # species
        except NoSuchElementException:
            data.append("N/A")
        try:
            x = browser.find_element_by_xpath("//*[contains(text(), 'Height')]/parent::*")
            r = x.find_element_by_xpath("td[2]")
            data.append(r.text)  # Height
        except NoSuchElementException:
            data.append("N/A")
        try:
            x = browser.find_element_by_xpath("//*[contains(text(), 'Weight')]/parent::*")
            r = x.find_element_by_xpath("td[2]")
            data.append(r.text)  # Weight
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(2) > div:nth-child(2)").text)  # intelligence
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(3) > div:nth-child(2)").text)      # strength
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(4) > div:nth-child(2)").text)         # speed
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(5) > div:nth-child(2)").text)    # durability
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(6) > div:nth-child(2)").text)         # power
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(7) > div:nth-child(2)").text)        # combat
        except NoSuchElementException:
            data.append("N/A")
        try:
            data.append(browser.find_element_by_css_selector("div.stat-bar:nth-child(8) > div:nth-child(2)").text)          # tier
        except NoSuchElementException:
            data.append("N/A")
        col = 0
        index = 7
        character_with_no_stats = True
        while index < 12:
            if data[index] != '∞':
                if int(data[index]) != 0:
                    character_with_no_stats = False
            index += 1

        if not character_with_no_stats:
            workbook = openpyxl.load_workbook("Character_Database.xlsx")
            worksheet = workbook.active
            worksheet.append(data)
            workbook.save("Character_Database.xlsx")
            workbook.close()
        browser.close()
        line = f.readline()

main()
