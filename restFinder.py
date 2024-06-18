from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import json

driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome()

def doText(element):
    if element:
        element_text = element.text
    else:
        element_text = "None"
    return element_text


def parse(soup):
    restaurantsData = []
    restaurants = soup.find_all('div', class_='UaQhfb')
    for restaurant in restaurants:
        name = restaurant.find('div', class_='qBF1Pd')
        rating = restaurant.find('span', class_='MW4etd')
        type =restaurant.select_one('div:nth-child(4) > div:nth-child(1) > span:nth-child(1) > span')
        street = restaurant.select_one('div:nth-child(4) > div:nth-child(1) > span:nth-child(3) > span:nth-child(2)')
        if not street:
            street = restaurant.select_one('div:nth-child(4) > div:nth-child(1) > span:nth-child(2) > span:nth-child(2)')

        restDict = {"name": doText(name),
                    "rating": doText(rating),
                    "type": doText(type),
                    "street": doText(street)}
        restaurantsData.append(restDict)

    json_data = json.dumps(restaurantsData)
    return json_data
def run(name):
    try:
        driver.get(f'https://www.google.com/maps/search/{name}+Restaurant/')
        button = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button')
        button.click()
        scrollableElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'))
        )

        while True:
            try:
                driver.find_element(By.CLASS_NAME, 'HlvSq')
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                break
            except NoSuchElementException:
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollableElement)

        return parse(soup)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()