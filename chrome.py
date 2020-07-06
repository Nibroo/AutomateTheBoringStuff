from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep


oogle = webdriver.Chrome()
oogle.get('https://google.com')
sleep(2)

images = oogle.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[2]/a')
images.click()
sleep(1)

search = oogle.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search.send_keys('iftekhar nibir')
sleep(1)
search.submit()

photo = oogle.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img')
photo.click()

actionChains = ActionChains(oogle)
actionChains.context_click('https://live.staticflickr.com/4580/24612331658_7471e8453c_b.jpg').perform()


