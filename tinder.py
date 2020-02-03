#!/usr/bin/python
from selenium import webdriver

import re
import requests
driver = webdriver.Chrome()
driver.get("https://tinder.com/app/recs")
driver.find_element_by_xpath(""" //div*[@aria-label='Like'] """).click()