"""
    Discord Dungeon Miner v1.2

    Collects and sells wood, minerals, lemons and XP
    points for a Discord chat server using the
    DiscordRPG bot text interface. 
    
    Runs with Python 3.6.0, Selenium 3.5.0
    and geckodriver v0.18.0 for x86_64 PCs

    Author: Sam Messick
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize browsing session
browser = webdriver.Firefox()
browser.get('https:discordapp.com/login')
time.sleep(1)
username = browser.find_element_by_id('register-email')
password = browser.find_element_by_id('register-password')
username.send_keys('EMAIL')                                            #Enter email and password between '' marks
password.send_keys('PASSWORD')                   
password.send_keys(Keys.ENTER)
time.sleep(1)
browser.get('SERVER ADDRESS') #Dungeon server link
time.sleep(10)

def bot_type(input_source, text, sleep_time):
    input_source.send_keys(text)
    input_source.send_keys(Keys.ENTER)
    time.sleep(sleep_time+.05)
def collect_items():
    bot_type(input, '#!forage', 0)
    bot_type(input, '#!chop', 0)
    bot_type(input, '#!mine', 0)
    bot_type(input, '#!fish', 0)
def heal_player():
    bot_type(input, '#!buy Health Potion 50', 0)
def sell():
    bot_type(input, '#!sell Log 30', 11)
    bot_type(input, '#!sell Iron Ore 18', 11)
    bot_type(input, '#!sell Iron Ore 18', 11)
    bot_type(input, '#!sell Coal 18', 11)
    bot_type(input, '#!sell Octopus 2', 11)
    bot_type(input, '#!sell Cherry 12', 11)
    bot_type(input, '#!sell Carrot 12', 11)
    bot_type(input, '#!sell Egg 12', 0)
def adventure(iterations):
    for i in range(iterations):
        if i%5 == 0:
            bot_type(input, '#!heal auto', 0)
            bot_type(input, '#!pheal auto', .1)
        bot_type(input, '#!adv 2', 12)

#Begin mining resources and adventuring; sell every 5th iteration
input = browser.find_element_by_class_name('textArea-20yzAH')
iter_count = 0

while(True):
    collect_items()
    if iter_count!=0 and iter_count%5==0:
        sell()
        heal_player()
        adventure(18)
        time.sleep(7)
    else:
        heal_player()
        adventure(25)
    iter_count += 1







