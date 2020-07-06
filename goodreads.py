import bs4, requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://goodreads.com')

search = driver.find_element_by_css_selector('#sitesearch_field')
search.send_keys('sidney sheldon')
search.submit()
search.back()
search.forward()

boook = search.find_element_by_css_selector('body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > table > tbody > tr:nth-child(15) > td:nth-child(2) > a > span')
boook.click()

pagel = boook.find_element_by_css_selector('#details > div:nth-child(1) > span:nth-child(2)')

print('pagel.text[0].strip')
