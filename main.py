from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
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
    driver.get("https://www.linkedin.com/authwall?trk=qf&original_referer=https://www.linkedin.com/feed/&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fhome")
    return driver

def main():
    driver = get_driver()
    driver.find_element(By.ID,"session_key").send_keys(USERNAME)
    driver.find_element(By.ID,"session_password").send_keys(PASSWORD + Keys.RETURN)
    return driver.current_url

print(main())


