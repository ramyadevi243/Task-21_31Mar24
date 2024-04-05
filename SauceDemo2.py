import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SauceDemo:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)

    def before_login(self):
        print("Cookies Before Login:")
        for cookies in self.driver.get_cookies():
            print(cookies)

    def after_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        print("\nCookies After Login:")
        for cookies in self.driver.get_cookies():
            print(cookies)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    saucedemo = SauceDemo(url)
    saucedemo.start()
    saucedemo.before_login()
    saucedemo.after_login()
    saucedemo.close()