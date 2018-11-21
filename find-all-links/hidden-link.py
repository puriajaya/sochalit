from selenium import webdriver
import time 

driver = webdriver.Firefox()
opt=webdriver.FirefoxOptions()
driver.get ('https://stackoverflow.com/questions')
x_href='//*[@href]'   #searchs like div[] class[] input[]
link=driver.find_elements_by_xpath(x_href)
for lk in link:
    print(">> : ",lk.get_attribute('href'))

time.sleep(10) 
driver.close()
