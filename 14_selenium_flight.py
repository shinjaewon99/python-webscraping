import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))


browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"

browser.get(url)

begin_date = browser.find_element(By.XPATH , '//button[text() = "가는 날"]')

begin_date.click()

# time.sleep(1) # 1초 대기

wait_until('//b[text() = "27"]') # 나올때 까지 30초 대기
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')

day27[0].click()


wait_until('//b[text() = "31"]')
day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')

day31[0].click()


wait_until('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH , '//b[text() = "도착"]')

arrival.click()

wait_until('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH , '//button[text() = "국내"]')

domestic.click()

wait_until('//i[contains(text(),"제주국제공항")]')
jeju = browser.find_element(By.XPATH , '//i[contains(text(),"제주국제공항")]')

jeju.click()

wait_until('//span[contains(text(), "항공권 검색")]')
serch = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')

serch.click()
 
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight_sK0eA result"]')))

print(elem.text)

browser.quit()
