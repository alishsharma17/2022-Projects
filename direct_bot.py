from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

my_username = '_alishsharma'
my_password = 'alish17'

usernames = ['yumnaa.mahmood']

messages = ["ur a dumbass"]
between_messages = 2000

browser = webdriver.Chrome('chromedriver')

def auth (username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2,4))
        input_username = browser.find_element_by_name('username')
        input_password = browser.find_element_by_name('password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1,2))
        input_password.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()

def send_message(users, messages):
    try:
        browser.find_element_by_xpath('/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(random.randrange(3,5))
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.randrange(1,2))
        browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
        for user in users:
            time.sleep(random.randrange(1,2))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(random.randrange(2,3))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
            time.sleep(random.randrange(3,4))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div').click()
            time.sleep(random.randrange(3,4))
            text_area = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            text_area.send_keys(random.choice(messages))
            time.sleep(random.randrange(2,4))
            text_area.send_keys(Keys.ENTER)
            print(f'message has been sent to {user}')
            time.sleep(between_messages)
            browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()

    except Exception as err:
        print(err)
        browser.quit()


auth(my_username, my_password)
time.sleep(random.randrange(2,4))
send_message(usernames,messages)
