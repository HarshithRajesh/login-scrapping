from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


# service = Service('C:\\Development\\chromedriver.exe')
service = Service(service = Service(ChromeDriverManager().install()))
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("disable-popup-blocking")

    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3420079349&f_AL=true&geoId=105214831&keywords=python%20"
           "developer&location=Bengaluru%2C%20Karnataka%2C%20India&refresh=true")
    return driver

def main():
    driver = get_driver()
    sign_in = driver.find_element(By.LINK_TEXT,"Sign in")
    sign_in.click()
    time.sleep(1)
    username = driver.find_element(By.ID,"username")
    username.send_keys(USERNAME)
    password = driver.find_element(By.ID,"password")
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)
    return driver.current_url

print(main())


