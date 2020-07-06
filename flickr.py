from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Open chrome and go to Google
flick = webdriver.Chrome()
flick.get('https://google.com')
sleep(2)

#Seach for my flickr account
search = flick.find_element_by_css_selector('.gLFyf')
search.send_keys('iftekhar nibir flickr')
sleep(1)
search.submit()
sleep(2)

#Opening the first result
found = flick.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3')
found.click()
sleep(3)

#---------------------------------------------------------------------
#erpor theke r kaj kortese na for some reason!
photo = flick.find_element_by_css_selector('#yui_3_16_0_1_1587133864934_3878')
photo.click()
sleep(1)

dwnld = flick.find_element_by_xpath('//*[@id="yui_3_16_0_1_1587133004812_2388"]/div[3]/a/i')
dwnld.click()

size = flick.find_element_by_xpath('//*[@id="yui_3_16_0_1_1587133004812_4198"]/div[2]/div/ul/li/a')
size.click()

img = "https://live.staticflickr.com/65535/49514787856_e89459ce07_b.jpg"

newtab = flick.find_element_by_tag_name('body')
newtab.send_keys(Keys.CONTROL + 't')
flick.get(img)

#img = flick.find_element_by_class_name('spaceball')

