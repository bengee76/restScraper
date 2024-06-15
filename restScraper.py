import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup



driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome()

name = ("Gdansk")

def parse(soup):
    restaurants = soup.find_all('div', class_='UaQhfb')
    counter = 0
    for restaurant in restaurants:
        name = restaurant.find('div', class_='qBF1Pd').text
        print(name)
        counter += 1

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
            time.sleep(7)
            break
        except NoSuchElementException:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollableElement)

    parse(soup)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()