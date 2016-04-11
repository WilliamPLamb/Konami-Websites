#! python3
# Opens up websites with the konami code

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# List of websites that use the konami code
websites = ["http://www.vogue.co.uk", "http://www.wired.co.uk"]

# only works if Firefox is installed
browser = webdriver.Firefox()

for website in websites:
    browser = webdriver.Firefox()
    # navigate to website
    browser.get(website)
    # select general website page to send key strokes to
    htmlElem = browser.find_element_by_tag_name("html")
    # send the konami key strokes
    htmlElem.send_keys(Keys.ARROW_UP)
    htmlElem.send_keys(Keys.ARROW_UP)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    htmlElem.send_keys(Keys.ARROW_LEFT)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    htmlElem.send_keys(Keys.ARROW_LEFT)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    htmlElem.send_keys("b")
    # these websites continue doing interesting things
    # when 'a' is repeatedly pressed
    for x in range(25):
        htmlElem.send_keys("a")
        sleep(.5)
