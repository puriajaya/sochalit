from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


keys={
'firstname':'TestUser',
'lastname':'SurnameUser',
'mobile_number':'9800010001',
'password':'Testpassword@$101',
'birthdate':['Dec',17,1971],
'gender':'Female'
}

driver = webdriver.Firefox()
opt=webdriver.FirefoxOptions()
driver.get ('https://www.facebook.com/')

x_firstname='//div[@class="uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput"]/input[@name="firstname"]'
x_lastname='//div[@class="uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput"]/input[@name="lastname"]'
x_mn='//div[@class="uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput"]/input[@name="reg_email__"]'
x_paswd='//div[@class="uiStickyPlaceholderInput uiStickyPlaceholderEmptyInput"]/input[@name="reg_passwd__"]'
x_month='//select[@name="birthday_month"]/option[text()="'+str(keys['birthdate'][0])+'"]'
x_day='//select[@name="birthday_day"]/option[text()="'+str(keys['birthdate'][1])+'"]'
x_year='//select[@name="birthday_year"]/option[text()="'+str(keys['birthdate'][2])+'"]'
x_gender_male='//span[@class="_5k_2 _5dba"]/input[@id="u_0_a"]'
x_gender_female='//span[@class="_5k_2 _5dba"]/input[@id="u_0_9"]'

if keys['gender'].lower() =='female' or 'f':
    x_gender=x_gender_female
elif keys['gender'].lower()=="male" or 'm':
    x_gender=x_gender_male



driver.find_element_by_xpath(x_firstname).send_keys(keys['firstname'])
driver.find_element_by_xpath(x_lastname).send_keys(keys['lastname'])
driver.find_element_by_xpath(x_mn).send_keys(keys['mobile_number'])
driver.find_element_by_xpath(x_paswd).send_keys(keys['password'])
driver.find_element_by_xpath(x_month).click()
driver.find_element_by_xpath(x_day).click()
driver.find_element_by_xpath(x_year).click()
driver.find_element_by_xpath(x_gender).click()

time.sleep(10) 

driver.close()
