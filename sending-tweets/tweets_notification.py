from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.message import EmailMessage

subscriber='$$$$$@gmail.com'
smtp_adress='$$$$$@gmail.com'
smtp_auth='$$$$$'
tweet_user='$$$$$'
tweet_pass='$$$$$'

def send_email(e_subject,e_receiver,e_meassage):
    msg = EmailMessage()
    msg['Subject'] = e_subject
    msg['From'] =smtp_adress
    msg['To'] = e_receiver
    msg.set_content(e_meassage)
    mail_conf = smtplib.SMTP('smtp.gmail.com' , 587)
    mail_conf.starttls()
    mail_conf.login( smtp_adress, smtp_auth)
    try:
        mail_conf.send_message(msg)
        mail_conf.quit()
    except Exception as e:
	    print("Unable to send, error:",e)



driver = webdriver.Firefox()
opt=webdriver.FirefoxOptions()

def web_login(usr_url):
    driver.get (usr_url)
    driver.find_element_by_xpath('//div[@class="clearfix field"]/input[@name="session[username_or_email]"]').send_keys(tweet_user)
    driver.find_element_by_xpath('//div[@class="clearfix field"]/input[@name="session[password]"]').send_keys(tweet_pass)
    driver.find_element_by_xpath('//div[@class="clearfix"]/button[@class="submit EdgeButton EdgeButton--primary EdgeButtom--medium"]').click()


web_login('https://twitter.com/login')
driver.get ('https://twitter.com/i/notifications')
link=driver.find_element_by_xpath('//div[@class="QuoteTweet-container"]/a').get_attribute('href')
driver.get(link)
note_content=driver.find_element_by_xpath('//div[@class="js-tweet-text-container"]/p').text
noticeof=driver.find_element_by_xpath('//span[@class="FullNameGroup"]/strong').text    
print(noticeof,note_content)

send_email("New notification from "+noticeof,subscriber,note_content)

driver.close()
