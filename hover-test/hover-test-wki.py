#weblink hover test

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

keys=['Nepal',]

driver = webdriver.Firefox()
opt=webdriver.FirefoxOptions()
action=ActionChains(driver)


driver.get ('https://www.wikipedia.org/')

x_search='//div[@class="search-input"]//input[@name="search"]'
x_submit='//button[@class="pure-button pure-button-primary-progressive"]'
x_hover_on='//p/a[@title="Nepali language"]' 

driver.find_element_by_xpath(x_search).send_keys(keys[0])
driver.find_element_by_xpath(x_submit).click()
hover_text="<<NA>>"
linked_data="<<NA>>"
try:
    element = driver.find_element_by_xpath(x_hover_on)
    hover_text=driver.find_element_by_xpath(x_hover_on).text
    linked_data=driver.find_element_by_xpath(x_hover_on).get_attribute('href')
    hov = ActionChains(driver).move_to_element(element)
    hov.perform()
    time.sleep(10) 
finally:
    print("Hovered on:",hover_text)
    print("Linked Data",linked_data)
    driver.close()



