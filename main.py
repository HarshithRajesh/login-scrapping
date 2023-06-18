from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
from dotenv import load_dotenv
import time
load_dotenv()

USERNAME = os.getenv('USER')
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
    driver.get("https://www.freelancer.com/login")
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(By.ID,"emailOrUsernameInput").send_keys(USERNAME)
    time.sleep(2)
    driver.find_element(By.ID,"passwordInput").send_keys(PASSWORD+Keys.RETURN)
    time.sleep(5)
    return driver.current_url
    


print(main())


