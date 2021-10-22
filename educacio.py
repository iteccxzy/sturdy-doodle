import time
from selenium import webdriver
import conf

browser = webdriver.Firefox()
browser.get(conf.URL)

time.sleep(2)
name_use = "username" 
search_user = browser.find_element_by_name(name_use)
search_user.send_keys(conf.CAMPUS_USERNAME)

name_pass = "password" 
search_pass = browser.find_element_by_name(name_pass)
search_pass.send_keys(conf.CAMPUS_PASSWORD)

submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
time.sleep(1)
submit_btn_el.click()

time.sleep(2)

browser.close()
