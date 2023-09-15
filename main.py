from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time


URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

pokedex = []


def scrape_data():
    global pokedex
    driver = webdriver.Chrome()

    driver.get(url=URL)

    table_data = driver.find_elements(By.CSS_SELECTOR, ".roundy tr")
    time.sleep(3)
    table_data.pop(0)

    for i in range(0, len(table_data)):
        row = table_data[i].text.split()
        if "#" in row[0]:
            pokedex.append(row)


def export_data():
    with open("pokedex.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(pokedex)


def read_data():
    file_data = []
    keep_going = True

    with open("pokedex.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            file_data.append(row)

    while keep_going:
        try:
            entry = input("Enter a number for search or q to quit: ")

            if entry == "q":
                keep_going = False
            else:
                num = int(entry) - 1
                print("Entry: " + file_data[num][0])
                print("Name: " + file_data[num][1])
                if len(file_data[int(entry) - 1]) <= 3:
                    print("Type: " + file_data[num][2])
                else:
                    print("Type: " + file_data[num][2] + " " + file_data[num][3])
        except ValueError:
            print("Value error!")


# scrape_data()
# export_data()
read_data()
