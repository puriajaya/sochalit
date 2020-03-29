from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


browser = webdriver.Chrome(chrome_options=chrome_options)  
# Optional argument, if not specified will search path.



#placeing xpath
search_symbol_box='//*[@id="stock_symbol"]'
submit_go='//*[@id="search_symbol"]'
total_listed_share='//*[text()="Total Listed Shares"]/../td[2]'
xp_company_name='//*[text()="Name and Symbol"]/../td[2]'



#list out all Stock Symbols
browser.get('http://www.nepalstock.com/company/display/')
browser.find_element_by_xpath('//*[@name="StockSymbol_Select"]')

print("\nReading all Symbols...")
options = [x for x in browser.find_elements_by_tag_name("option")]

keys=[]

print("\nCollecting Keys...")
for each in options:
    if each.text!="":
        keys.append(each.text)
print("Total Symbols: ", len(keys)-1)
print(keys)

x=0
browser.get('http://www.nepalstock.com/company/display/')
print("Extracting all data from source... \n")
for x in range(len(keys)-1):
    browser.find_element_by_xpath(search_symbol_box).send_keys(keys[x+1])
    wait = WebDriverWait(browser, 100)
    go_link = wait.until(EC.visibility_of_element_located((By.XPATH, submit_go)))
    go_link.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, total_listed_share)))
    listed_share=browser.find_element_by_xpath(total_listed_share).text
    company_name=browser.find_element_by_xpath(xp_company_name).text
    print("%d:%s:%s"%(x+1,company_name,listed_share))


browser.quit()




