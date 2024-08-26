# метод где бот это всё делает в ручную, но к сожалению не может подтвердить конект к сайту, 
# силениум не видит верстку

# Проблема в том что когда на сайте надо залогиться под кошелком, то переходя в
# кошелек не селениум не видит верной верстки что бы нажать по кнопке
# в app-2 попробуем вручную один раз зайти, и сразу на сайт с ботом заходить

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
service = Service('./chromedriver')
useragent = UserAgent(browsers=['chrome'])

options = Options()
options.add_extension('./metamask.crx')
options.add_argument(f"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=service, options=options)

def wait_for_two_tabs_and_close_first(driver):
    """Ожидание появления двух вкладок и закрытие первой."""
    WebDriverWait(driver, 60).until(lambda d: len(driver.window_handles) >= 2)
    
    # Запоминаем идентификаторы вкладок
    all_windows = driver.window_handles
    if len(all_windows) >= 2:
        # Переключаемся на первую вкладку и закрываем её
        driver.switch_to.window(all_windows[0])
        driver.close()
        # Переключаемся на вторую вкладку
        driver.switch_to.window(all_windows[1])

pause = 1

try:
    # конектимся в метамаск
    # Ожидание появления двух вкладок и закрытие первой
    wait_for_two_tabs_and_close_first(driver)
    time.sleep(2)

    try:
        termsCheckElement = driver.find_element(By.XPATH, '//input[@data-testid="onboarding-terms-checkbox"]')

        if not termsCheckElement.is_selected():
            termsCheckElement.click()  # Клик по чекбоксу, чтобы отметить его

        # Перейти к следующему шагу
        importExistingWallet = driver.find_element(By.XPATH, '//*[@data-testid="onboarding-import-wallet"]')
        importExistingWallet.click()
        time.sleep(pause)

        # skip metrics
        metametricsNoThanks = driver.find_element(By.XPATH, '//*[@data-testid="metametrics-no-thanks"]')
        metametricsNoThanks.click()
        time.sleep(pause)

        secretPhrase = "secret phrase(12 words) from your wallet"
        secretPhraseArr = secretPhrase.split(" ")

        # заполняем сид фразу
        for index, value in enumerate(secretPhraseArr):
            try:
                xpath = f'//*[@data-testid="import-srp__srp-word-{index}"]'
                importSrpWord = driver.find_element(By.XPATH, xpath)
                importSrpWord.send_keys(value)
            except Exception as e:
                print(f"Not found element '{xpath}': {e}")
  

        # подтверждаем что заполнили сид фразу
        importSrpConfirm = driver.find_element(By.XPATH, '//*[@data-testid="import-srp-confirm"]')
        importSrpConfirm.click()
        time.sleep(pause)

        # создаем пароль
        password = 'selenium-metamask-password' 
        createPasswordNew = driver.find_element(By.XPATH, '//*[@data-testid="create-password-new"]')
        createPasswordNew.send_keys(password)

        createPasswordConfirm = driver.find_element(By.XPATH, '//*[@data-testid="create-password-confirm"]')
        createPasswordConfirm.send_keys(password)

        createPasswordTerms = driver.find_element(By.XPATH, '//*[@data-testid="create-password-terms"]')
        createPasswordTerms.click()

        createPasswordImport = driver.find_element(By.XPATH, '//*[@data-testid="create-password-import"]')
        createPasswordImport.click()
        time.sleep(pause)

        # пропускаем onboarding
        onboardingCompleteDone = driver.find_element(By.XPATH, '//*[@data-testid="onboarding-complete-done"]')
        onboardingCompleteDone.click()
        time.sleep(pause)

        # подтверждаем что ознакомились
        pinExtensionNext = driver.find_element(By.XPATH, '//*[@data-testid="pin-extension-next"]')
        pinExtensionNext.click()
        time.sleep(pause)

        pinExtensionDone = driver.find_element(By.XPATH, '//*[@data-testid="pin-extension-done"]')
        pinExtensionDone.click()
        time.sleep(pause)
    except Exception as e:
        print("Exception:", e)



    # идем на сайт
    driver.get('https://www.gaianet.ai/')
    xpath = '//span[contains(@class, "text-base") and contains(@class, "leading-none") and contains(text(), "Connect")]'
    connectBtn = driver.find_element(By.XPATH, xpath)
    connectBtn.click()

    # Ожидание появления вкладки MetaMask и переключение на неё
    WebDriverWait(driver, 60).until(lambda d: len(driver.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    try:
        # driver.get('chrome-extension://{}/notification.html'.format('nkbihfbeogaeaoehlefnkodbefgpgknn'))
        time.sleep(2)

        print('page_source', driver.page_source)
    except Exception as e:
        print("Exception when connect metamsk wallet on www.gaianet.ai:", e)
    time.sleep(2)

    time.sleep(60)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()