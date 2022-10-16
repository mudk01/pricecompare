import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def compare(search_term):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    target_url = "https://www.target.com/s?searchTerm="
    walmart_url = "https://www.walmart.com/search?q="
    target_url += search_term
    walmart_url += search_term
    # page = requests.get(test_url)
    # soup = BeautifulSoup(page.content, "html.parser")

    driver.get(target_url)
    time.sleep(5)

    results = driver.find_elements(By.XPATH, "//div[@data-test='product-details']")

    target_ls = {}
    for result in results:
        title_div = result.find_element(By.CLASS_NAME, "h-display-flex")
        title = title_div.find_element(By.TAG_NAME, "div").text
        price = result.find_element(By.CLASS_NAME, "h-padding-r-tiny").text
        target_ls[title] = price

    print(target_ls)

    driver.get(walmart_url)
    time.sleep(5)

    # results_walmart = driver.find_elements(By.XPATH, "//div[@data-testid='list-view']")

    price_div = driver.find_elements(
        By.XPATH, "//div[@data-automation-id='product-price']"
    )
    title_div = driver.find_elements(By.XPATH, "//span[@class='w_Bn']")

    title_arr = []
    for title in title_div:
        title_arr.append(title.text)

    separator = "\n"
    walmart_ls = {}
    for i in range(len(price_div)):
        walmart_ls[title_arr[i]] = price_div[i].text.split(separator, 1)[0]

    print(walmart_ls)
    return (target_ls, walmart_ls)
