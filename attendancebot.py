from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
import urllib
import time
from cnn import CNN


BASE_URL = "https://talos.stuy.edu/auth/login/"
EMAIL = "EMAIL"
PWORD = "PASSWORD"

class Bot():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.model = CNN()

    def take_attendance(self):
        driver = self.driver 
        driver.get(BASE_URL)
        emailelm = driver.find_element_by_id("id_username")
        emailelm.send_keys(EMAIL)
        passelm = driver.find_element_by_id("id_password")
        passelm.send_keys(PWORD)
        elem = driver.find_element_by_xpath("//input[@type='submit']")
        elem.click()
        elem = driver.find_element_by_link_text("Dashboard")
        elem.click()
        src = driver.find_element_by_class_name("captcha").get_attribute('src')
        driver.execute_script("window.scroll(0,900)") 
        urllib.request.urlretrieve(src, "captcha.png")
        ans = self.model.solve()
        elem = driver.find_element_by_id("id_captcha_1")
        elem.send_keys(ans)
        elem = driver.find_element_by_xpath("//input[@type='submit']")
        elem.click()
        elem = driver.find_element_by_class_name('alert')
        response = elem.text
        print(response)
        assert('Attendance taken' in response)
    

def main():
    bot = Bot()
    while True:
        if datetime.now().hour == 7:
            print("trying")
            try:
                bot.take_attendance()
                print(datetime.today().strftime("%h:%M:%S"))
                return
            except:
                bot.take_attendance()

if __name__=="__main__":
    main()