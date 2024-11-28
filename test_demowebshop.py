from POM.login_page import DemoLogin

def test_login(launching_driver):     #launching_driver = driver
    d=DemoLogin(launching_driver)                 #driver=webdriver.Chrome()
    d.clk_login()
    d.email_log()
    d.pwd_log()
    d.btn_log()



















