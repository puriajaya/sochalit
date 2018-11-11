from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
opt=webdriver.FirefoxOptions()

login_url='https://twitter.com/login'

def web_login():
    driver.get (login_url)
    driver.find_element_by_xpath('//div[@class="clearfix field"]/input[@name="session[username_or_email]"]').send_keys('$$$$$$')
    driver.find_element_by_xpath('//div[@class="clearfix field"]/input[@name="session[password]"]').send_keys('$$$$$$$')
    driver.find_element_by_xpath('//div[@class="clearfix"]/button[@class="submit EdgeButton EdgeButton--primary EdgeButtom--medium"]').click()
web_login()
driver.close()

