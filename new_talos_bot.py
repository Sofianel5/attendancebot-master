from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
import urllib
import time
from twocaptcha import TwoCaptcha


BASE_URL = "https://talos.stuy.edu/auth/login/"
EMAIL = ""
PASSWORD = ""
SITE_KEY = "6LdeHOoUAAAAAHmiaqBcTvueEKOEeyGdP8KEnNdI"
API_KEY = "84f099a10f93eca92929d89b4239cd8e"

class Bot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def solve_recaptcha(self):
        two = TwoCaptcha(API_KEY)
        print(self.driver.current_url)
        res = two.resolve_captcha(SITE_KEY, self.driver.current_url)
        print(res)
        return res

    def take_attendance(self, email, password):
        driver = self.driver 
        driver.get(BASE_URL)
        driver.find_element_by_id('id_login').send_keys(email)
        driver.find_element_by_id('id_password').send_keys(password)
        driver.find_element_by_class_name('ml-auto').click()
        captcha_res = self.solve_recaptcha()
        driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='"+captcha_res+"'")
        driver.execute_script("document.querySelector('form').submit()")
        time.sleep(80)


def main():
    bot = Bot()
    while True:
        if datetime.now().hour == 7:
            print("trying")
            try:
                bot.take_attendance(EMAIL, PASSWORD)
                print(datetime.today().strftime("%H:%M:%S"))
                print("DONE")
                return
            except:
                bot.take_attendance(EMAIL, PASSWORD)

if __name__=="__main__":
    main()