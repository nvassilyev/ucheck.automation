import time, random, datetime, sys
from selenium import webdriver

def delay():
   time.sleep(random.randint(1,2))
   
now = datetime.datetime.now()

username = '//*[@id="username"]'
password = '//*[@id="password"]'
login = '/html/body/div/div/div[1]/div[2]/form/button'
start = '//*[@id="root"]/div[2]/div/div/div[2]/button/span[1]'
q1 = '//*[@id="f5d87fa4-41c1-41bf-9307-2eb2e7862a28-noFocus"]/fieldset/label[2]'
q2 = '//*[@id="ebdd2acd-87ff-47aa-a7d2-059677987580-noFocus"]/fieldset/label[1]'
q3 = '//*[@id="5c2a5703-ce69-40aa-bf5a-5ddd81335aa9-noFocus"]/fieldset/label[1]'
q4 = '//*[@id="296a215c-8f44-4ca0-b2bc-6861ddabec3b-noFocus"]/fieldset/label[1]'
q5 = '//*[@id="c2a1ba3f-0113-49a6-95cc-aeede171963a-noFocus"]/fieldset/label[1]'
q6 = '//*[@id="11985099-8548-4dc6-944f-bb4ea9c9494b-noFocus"]/fieldset/label[1]'
q7 = '//*[@id="156f6b12-1f8a-491c-9261-2dd73aef9d6a-noFocus"]/fieldset/label[1]'
q8 = '//*[@id="801d8c6a-6523-437e-bb6d-fa4092dacab1-noFocus"]/fieldset/label[1]'
submit = '//*[@id="root"]/div/div/div/div[2]/main/div/div/div/div/div/button'

driver = webdriver.Chrome()
driver.get('https://ucheck.utoronto.ca')
driver.maximize_window()
u_id = 'username'
pw_id = 'passsword'

try:
    delay()
    driver.find_element_by_xpath(username).send_keys(u_id)
    driver.find_element_by_xpath(password).send_keys(pw_id)
    driver.find_element_by_xpath(login).click()
except:
    with open('log.txt', 'a') as f:
        print(f'{now}: Login error', file=f)
    driver.close()
    exit()
    
try:
    delay()
    driver.find_element_by_xpath(start).click()
    
    delay()
    driver.find_element_by_xpath(q1).click()
    delay()
    driver.find_element_by_xpath(q2).click()
    delay()
    driver.find_element_by_xpath(q3).click()
    delay()
    driver.find_element_by_xpath(q4).click()
    delay()
    driver.find_element_by_xpath(q5).click()
    delay()
    driver.find_element_by_xpath(q6).click()
    delay()
    driver.find_element_by_xpath(q7).click()
    delay()
    driver.find_element_by_xpath(q8).click()
    delay()
    driver.find_element_by_xpath(submit).click()
    
    with open('log.txt', 'a') as f:
        print(f'{now}: success', file=f)
    driver.close()

except:
    with open('log.txt', 'a') as f:
        print(f'{now}: bug', file=f)
    driver.close()

