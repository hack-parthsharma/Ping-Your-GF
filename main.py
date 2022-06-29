#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! ping-your-gf


"""
 [ping-your-gf] 
 Ping your GF is a python script that texts your gf or her uncle's ostrich a good morning text when ever you wish on instagram.
 This can also be used to tell someone that you are awake and going to the gym and take a nap, without even waking up.
"""

# importing module
from selenium import webdriver
import os
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


class bot:

    def __init__(self, username, password, user, message):
        self.username = "ruhendd"
        self.password = "sakura122"
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # first pop-up
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)

        # 2nd pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            
        time.sleep(4)

        # direct button
        self.bot.find_element_by_xpath(
            '//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Messenger"]').click()
        time.sleep(3)

        # clicks on pencil icon
    
        
        
        for i in self.user:
            self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)
            
            # enter the username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            # click on the username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[2]/div/div').click()
            time.sleep(2)

            # next button
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(2)

            # click on message area
            send = self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            # types message
            send.send_keys(self.message)
            time.sleep(1)

            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

def getInputs():
    user = ['nibbi']   # nibbi -> your girl
    message_list = ['Hi Babe! Good morning', 'Good morning sunshine!', 'I missed you while I was asleep :\(', 'Wake up my lovely pup...']
    message_ = random.choice(message_list)
    return user, message_

def init():
    user, message_ = getInputs()   
    bot('nibba', 'password_is_here', user, message_) # nibba -> you | password_is_here -> password
    input("DONE")


# calling the function
init()