
from http.client import BAD_REQUEST
from socket import inet_ntoa
import time
import asyncio
from argparse import Action
import imp
from lib2to3.pgen2 import driver
from time import time
from tracemalloc import stop
import webbrowser 
import json
from json import JSONEncoder
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

 #open json file
f= open('member_cardnumber_2.json')

#load Json
card_numbers = json.load(f)
browser = webdriver.Chrome(options=chrome_options)

#openFile = open('memeber_details.json')


#For Searching Members
#cardnumberprefix = 'MD-'
# cardnumbersuffix = str(349)

 
#searchfield()

outer_list = card_numbers["card_numbers"]
n=300
final = [outer_list[i * n:(i + 1) * n] for i in range((len(outer_list) + n - 1) // n )]


for outer_list in final:
  browser.get("http://tclpstaff.bestbookbuddies.com")
  browser.find_element_by_id('userid').send_keys("kranti") 
  browser.find_element_by_id('password').send_keys("k1234")
  browser.find_element_by_id('submit-button').click()
  for idx, inner_dict in enumerate(card_numbers["card_numbers"]):
      
   old_id = inner_dict["Old Id"]
   new_id = inner_dict["New ID"]
   if idx ==0 :
     browser.find_element_by_id('ui-id-4').click()
   else:
     browser.find_element_by_id('ui-id-1').click()
   try : 
     browser.find_element_by_id('searchmember').send_keys(old_id)
   except:
     browser.find_element_by_id('ren_barcode').send_keys(old_id)
   try:
     browser.find_element_by_xpath("//*[@id='patron_search']/form/input[3]").click()
   except:
      browser.find_element_by_xpath("//*[@id='patron_search']/form/div[1]/input[3]").click()


    # Editing the fields 
      browser.find_element_by_xpath("//div[@id='patron-library-details']//a[@class='btn btn-default btn-xs'][normalize-space()='Edit']").click()

      cardnumber= browser.find_element_by_id('cardnumber')

      cardnumber.clear()
    
      cardnumber.send_keys(new_id)

      browser.find_element_by_xpath("//button[@id='saverecord']").click()

  #entredValue()

  # i = 1; 


  # print(editfield)

  # while cardnumbersuffix<str(425):
      #browser.find_element_by_id('ui-id-1').click()
    # browser.find_element_by_id('searchmember').send_keys("MD-"+cardnumbersuffix+1)
    # try: 
      #    browser.find_element_by_xpath("//*[@id='patron_search']/form/input[3]").click()
    # except: 
      #   browser.find_element_by_xpath("//*[@id='patron_search']/form/div[1]/input[3]").click()
    # browser.find_element_by_xpath("//div[@id='patron-library-details']//a[@class='btn btn-default btn-xs'][normalize-space()='Edit']").click()
      #cardnumber= browser.find_element_by_id('cardnumber')
  #
    # cardnumber.clear()
    # cardnumber.send_keys("MK-"+cardnumbersuffix+1)
    # browser.find_element_by_xpath("//button[@id='saverecord']").click() " "
      

      #For Loop


#to quit the window
browser.quit()
# browser.quit()