import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# target_product_url = "https://www.target.com/p/sony-wh-1000xm4-noise-canceling-overhead-bluetooth-wireless-headphones-black/-/A-79757327?ref=tgt_adv_XS000000&AFID=google_pla_df&fndsrc=tgtao&DFA=71700000014846099&CPNG=PLA_Electronics%2BShopping_Brand%7CElectronics_Ecomm_Hardlines&adgroup=SC_Electronics&LID=700000001170770pgs&LNM=PRODUCT_GROUP&network=g&device=c&location=9032493&targetid=pla-82462042369&ds_rl=1246978&ds_rl=1248099&gclid=CjwKCAjwtKmaBhBMEiwAyINuwKgPr2kaaazHNLcM_RJiMmb3TyeqlyoMI1BZQTGkbNPIxUmHq_GTdxoCDd0QAvD_BwE&gclsrc=aw.ds"
# walmart_product_url = "https://www.walmart.com/ip/Sony-WH-1000XM4-Wireless-Noise-Canceling-Over-the-Ear-Headphones-with-Google-Assistant-Black/310157752?wmlspartner=wlpa&selectedSellerId=0&wl13=2697&adid=22222222277310157752_117755028669_12420145346&wmlspartner=wmtlabs&wl0=&wl1=g&wl2=c&wl3=501107745824&wl4=pla-294505072980&wl5=9032493&wl6=&wl7=&wl8=&wl9=pla&wl10=8175035&wl11=local&wl12=310157752&wl13=2697&veh=sem_LIA&gclid=CjwKCAjwtKmaBhBMEiwAyINuwL_2qY0OX-8lRl1avU2qYn_QDkjO6liA0-8_HnPEaAua1aNI6Km0yBoC7uAQAvD_BwE&gclsrc=aw.ds"

test_url = "https://www.target.com/s?searchTerm=sony+wh+1000xm4"

page = requests.get(test_url)
soup = BeautifulSoup(page.content, "html.parser")

driver.get(test_url)
time.sleep(5)

results = driver.find_elements(By.XPATH, "//div[@data-test='product-details']")
for result in results:
    title_div = result.find_element(By.CLASS_NAME, "h-display-flex")
    title = title_div.find_element(By.TAG_NAME, "div").text
    price = result.find_element(By.CLASS_NAME, "h-padding-r-tiny").text
    print(title, price)
