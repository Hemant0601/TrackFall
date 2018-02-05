#!/usr/bin/env python

username = "username"
password = "password"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.PhantomJS()
driver.get("http://insta.friendorfollow.com")
driver.find_elements_by_tag_name("a")[1].click()

print "Perimene file....".upper()
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_class_name("button-green").click()

try:
  driver.find_elements_by_name("allow")[1].click()
except:
  pass

f = open(username+".txt", 'w')
malakes = re.findall(ur'data-id=\"([0-9]*)\"', driver.page_source)[::-1]
for malakas in malakes:
  print >> f, malakas

f.close()
driver.quit()
