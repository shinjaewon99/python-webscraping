from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

url = "https://flight.naver.com/"

browser.get(url)

begin_date = browser.find_element(By.XPATH , '//button[text() = "가는 날"]')

begin_date.click()

day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')

day27[0].click()

day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')

day31[0].click()



arrival = browser.find_element(By.XPATH , '//b[text() = "도착"]')

arrival.click()

domestic = browser.find_element(By.XPATH , '//button[text() = "국내"]')

domestic.click()

jeju = browser.find_element(By.XPATH , '//i[contains(text(),"제주국제공항")]')

jeju.click()

serch = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')

serch.click()
 
