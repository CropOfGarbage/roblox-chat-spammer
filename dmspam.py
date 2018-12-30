from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('/home/meme/Desktop/py/roblox/chromedriver')
browser.get(('https://roblox.com/')) # Site to open

def login(username, password): # Login function
     browser.find_element_by_id('CookieLawAccept').click()
                          #AUTO COOKIE ACCEPT

     user = browser.find_element_by_id('horizontal-login-username')
     user.send_keys(username) # Get username box and fill it in

     passw = browser.find_element_by_id('horizontal-login-password')
     passw.send_keys(password) # Get password box and fill it in

     login = browser.find_element_by_id('horizontal-login-button')
     login.click() # Submit our login data

def SM2AF(message): #Send Message 2 All Friends :)
     chatwindow = browser.find_element_by_id('chat-main')
     chatwindow.click() # open our window
 
     time.sleep(1) # Safety pause 
 
     friendlist = browser.find_element_by_id('chat-friends')
     friends = friendlist.find_elements_by_tag_name('li')
     print('Grabbing friends/group chats...')
     fcount = 0
     tcount = 0
     for fwend in friends:
       text = fwend.text
       tcount = tcount + 1
       if text != '': # Without this check weird empty DMS appear.
          fcount = fcount + 1
          print('======='+  str(fcount) + '========')
          print(text)
          print('===============')
          fwend.click() # Open Chat Window
          chat_input = browser.find_element_by_id('dialog-input')
          chat_input.send_keys(message) # Type message
          chat_input.send_keys(Keys.ENTER) # Send message
          print('Sent a message')
          browser.find_elements_by_class_name('icon-chat-close-white')[0].click()
          time.sleep(1.5) # Increase/decrease this if needed, just here so we can load the chats in time.
     
username = str(raw_input('Username: '))
password = str(raw_input('Password: '))
msg = str(raw_input('Message to send: '))
login(username, password)
str(raw_input('Have you accepted the orange cookie warning AND done the verification challenge, if so press enter: '))
SM2AF(msg)
