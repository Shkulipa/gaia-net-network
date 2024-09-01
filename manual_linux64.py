# метод в ручную: надо залогинться через метамаск и остаться на странице
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from questions import questions
import random
import time
import os

# Путь к Chrome и chromedriver
chrome_path = '/usr/bin/google-chrome'

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
service = Service('./chromedriver_linux64')
useragent = UserAgent(browsers=['chrome'])

options = Options()
options.binary_location = chrome_path  # Указываем путь к Chrome
options.add_extension('./metamask.crx')
options.add_argument(f"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
options.add_argument('--no-sandbox')

# Директория для хранения профиля
profile_directory = os.path.join(os.getcwd(), "chrome_profile")
options.add_argument(f"user-data-dir={profile_directory}")

driver = webdriver.Chrome(service=service, options=options)

def refresh_page():
    print("Обновление страницы...")
    driver.refresh()
    time.sleep(15)  # Дайте странице время для полной загрузки

try:
    driver.get('https://www.gaianet.ai/agents')

    time.sleep(40)

    driver.get('https://0x07f9258b97b128c12a34d49442582c4bc6858520.us.gaianet.network')
    time.sleep(10)

    # начать новый чат
    xpath = '//button[contains(text(), "New chat")]'
    new_chat_button = driver.find_element(By.XPATH, xpath)
    new_chat_button.click()
    time.sleep(15)

    # Бесконечный цикл для отправки вопросов по кругу
    while True:
        for question in questions:
           # Обязательно перезапрашиваем текстовое поле перед каждой отправкой вопроса
            textarea = driver.find_element(By.XPATH, '//textarea')
            textarea.send_keys(question + Keys.ENTER)
            time.sleep(10)

            try:
                WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, "//p[text()='Send']"))
                )
                time.sleep(15)
            except Exception as e:
                print(f"Ошибка при ожидании элемента: {e}")
                refresh_page()
                continue

        time.sleep(5)  # Ожидание перед началом нового круга вопросов
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()