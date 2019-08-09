import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FacebookHomeBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Safari()

    def closebrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        # Stop here
        time.sleep(7)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        user_pw_elem = driver.find_element_by_xpath("//input[@name='password']")
        user_pw_elem.clear()
        user_pw_elem.send_keys(self.password)
        user_pw_elem.send_keys(Keys.RETURN)
        time.sleep(5)
        not_now_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]")
        not_now_button.click()
        time.sleep(2)

    def like_photo(self):
        driver = self.driver
        # driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(1)
        count = 0
        ercount = 0
        print('Start to scroll down!!')
        # will stop when there are all Likes
        for i in range(1, 100):
            like_buttons = driver.find_elements_by_xpath(
                "//button[@class='dCJp8 afkep coreSpriteHeartOpen _0mzm-' and ./span[@aria-label='Like']]")
            if like_buttons == []:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2000);")
            else:
                for button in like_buttons:
                    try:
                        button.click()
                        count += 1
                        print('Like times : ', count)
                        time.sleep(1)
                    except Exception as e:
                        ercount += 1
                        print('Somethings are wrong--times : ', ercount)
                        time.sleep(2)
                time.sleep(2)
        print('Finished scrolling!!')

        print('************************************')
        print('Finished program with : ', count, ' Likes')
        print('And end program with : ', ercount, ' Errors')


MichaelIns = InstagramBot("YOUR_USER_ID", "YOUR_PASSWORD")
MichaelIns.login()
MichaelIns.like_photo()





