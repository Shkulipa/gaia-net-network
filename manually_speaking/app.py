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

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
service = Service('./chromedriver')
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
    driver.get('https://www.gaianet.ai/')

    time.sleep(60)

    driver.get('https://www.gaianet.ai/chat')
    time.sleep(1)

    # начать новый чат
    xpath = '//button[contains(text(), "New chat")]'
    new_chat_button = driver.find_element(By.XPATH, xpath)
    new_chat_button.click()
    time.sleep(7)

    textarea = driver.find_element(By.XPATH, '//textarea')

    # Выбираем случайный вопрос из списка
    random_question = random.choice(questions)

    # Отправляем случайный вопрос
    textarea.send_keys(random_question + Keys.ENTER)
    time.sleep(15)

    textarea = driver.find_element(By.XPATH, '//textarea')

    # Бесконечный цикл для отправки вопросов по кругу
    while True:
        for question in questions:
            textarea.send_keys(question + Keys.ENTER)
            time.sleep(5)

            # Ожидание появления тега <p> с текстом "Send"
            WebDriverWait(driver, 900).until(
                EC.presence_of_element_located((By.XPATH, "//p[text()='Send']"))
            )
            time.sleep(5)
            # Переход к следующей итерации сразу после появления тега "Send"
            continue

        time.sleep(5)  # Ожидание перед началом нового круга вопросов
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()