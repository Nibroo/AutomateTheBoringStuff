from selenium import webdriver
from time import sleep

her = webdriver.Chrome()
her.get('https://google.com')
sleep(2)

img = her.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[2]/a')
img.click()

want = her.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
want.send_keys('alizeh shah')
want.submit()
sleep(2)

need = her.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[7]/a[1]/div[1]/img')
need.click()

wow = her.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/a/img')
wow.click()

see = her.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[1]/a/div[2]')
see.click()                                
