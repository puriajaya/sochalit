from selenium import webdriver
import xlsxwriter as xl
from datetime import date

workbook = xl.Workbook('/home/ajpuri/Desktop/Deal_Of_the_Day.xlsx')
worksheet = workbook.add_worksheet()

browser = webdriver.Firefox()
fox_opt=webdriver.FirefoxOptions()
fox_opt.add_argument('--headless')

query_url = "https://www.amazon.com/gp/goldbox"
browser.get(query_url)
print('Run Date:',date.today())
for x in range(25):
    x_deal_name='//div[@id="100_dealView_'+str(x)+'"]//a[@id="dealTitle"]/span'
    x_deal_price='//div[@id="100_dealView_'+str(x)+'"]//div[@class="a-row dealDetailContainer"]//div[@class="a-row priceBlock unitLineHeight"]/span'
    deal_name = browser.find_elements_by_xpath(x_deal_name)
    deal_price=browser.find_elements_by_xpath(x_deal_price)
    try:
        print('Item %d: %s & price %s' %(x+1,deal_name[0].text,deal_price[0].text))
        worksheet.write(x, 0, deal_name[0].text)
        worksheet.write(x, 1, deal_price[0].text)
    except IndexError:
        print('Item %d: %s & No Price Listed.'%(x,deal_name[0].text))
        worksheet.write(x, 0, deal_name[0].text)
        worksheet.write(x, 1, 'No Price Listed.')

browser.close()
workbook.close()


