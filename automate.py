from selenium import webdriver
import getpass

import time

from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://stackoverflow.com/')

time.sleep(2)

login = browser.find_element("xpath", '/html/body/header/div/nav/ol/li[3]/a')

login.click()

u_name = input("username: ")
p_word = getpass.getpass()

user = browser.find_element("xpath", '//*[@id="email"]')

user.send_keys(u_name)

passwd = browser.find_element("xpath", '//*[@id="password"]')

passwd.send_keys(p_word)

enter = browser.find_element("xpath", '//*[@id="submit-button"]')

enter.click()

time.sleep(2)

prof = browser.find_element("xpath", '/html/body/header/div/nav/ol/li[2]/a/div[1]/img')

prof.click()
