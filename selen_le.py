from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com/')
elems = browser.find_elements(By.CSS_SELECTOR, 'p')
len(elems)

searchElem = browser.find_element_by_css_selector(
    'html')
searchElem.text
