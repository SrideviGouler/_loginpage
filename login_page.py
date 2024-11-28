import time

class DemoLogin:
    def __init__(self,driver):

        self.driver=driver
    def clk_login(self):
        self.driver.find_element("xpath","//a[@class='ico-login']").click()
        time.sleep(2)
    def email_log(self):
        self.driver.find_element("xpath","//input[@class='email']").send_keys("sridevi@gmail.com")
        time.sleep(1)
    def pwd_log(self):
        self.driver.find_element("xpath","//input[@class='password']").send_keys("sree@1234")
        time.sleep(1)
    def btn_log(self):
        self.driver.find_element("xpath","//input[@class='button-1 login-button']").click()


