# специально надо для того что бы подключиться к кошельку

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
import os

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
service = Service('./chromedriver_macos')
useragent = UserAgent(browsers=['chrome'])

options = Options()
options.add_extension('./metamask.crx')
options.add_argument(f"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")

# Директория для хранения профиля
profile_directory = os.path.join(os.getcwd(), "chrome_profile")
options.add_argument(f"user-data-dir={profile_directory}")

driver = webdriver.Chrome(service=service, options=options)

pause = 1

try:
    time.sleep(600)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()