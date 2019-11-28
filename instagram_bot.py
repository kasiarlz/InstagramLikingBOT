from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


class InstagramBot:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox(executable_path=r'geckodriver.exe')
    def closeBrowser(self):
        self.driver.close()

    def login(self): 
        #driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
        driver=self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        login_button=driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem=driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem=driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        
    def like_photo(self, hashtag):
        driver=self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)
        
        for _ in range (1,3):
  
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            hrefs=driver.find_elements_by_tag_name('a')      #teraz to szuka zdjęcia  
            hrefs= [elem.get_attribute('href') for elem in hrefs if '.com/p/' in elem.get_attribute('href')]
            #pic_hrefs=[elem.get_attribute('href')for elem in hrefs]
            [hrefs.append(href) for href in hrefs if href not in hrefs]
            #print("Check: pic href length " + str(len(hrefs)))  -------TO JEST DOBRE
            
     
# Liking the picture
        unique_photos = len(hrefs)
        for pic_href in hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button=driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                like_button.click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


        
                
        
YourIg=InstagramBot('YOUR LOGIN','YOUR PASSWORD')
YourIg.login()
YourIg.like_photo('HASHTAGS')






