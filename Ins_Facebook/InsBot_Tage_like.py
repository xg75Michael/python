from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Safari()

    def CloseBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
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
        # not_now_button = driver.find_element_by_xpath("//button[@class='aOOlW HoLwm ']")
        not_now_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]")
        not_now_button.click()
        time.sleep(2)
        # alert = driver.switch_to_alert()
        # alert.dismiss()

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        hrefs = []
        for i in range(1, 30):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            hrefs_ele = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs_ele]
            # print(pic_hrefs)
            hrefs = hrefs + pic_hrefs
            # print(hrefs)
            hrefs = list(set(hrefs))
            # print(hrefs)

        # searching for pictures link
        # hrefs = driver.find_elements_by_tag_name('a')
        # pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        # print(pic_hrefs)
        pic_links = [href for href in hrefs if '/p/' in href]
        print(hashtag + ' photos: ' + str(len(pic_links)))
        print(pic_links)
        i = 1
        for pic_href in pic_links:
            print('已点赞数量：', i, '----', pic_href)
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            try:
                # driver.find_element_by_link_text("Like").click()
                like_click = driver.find_element_by_xpath("//main[@role='main']/div/div/article/div[2]/section[1]/span[1]/button")
                like_click.click()
                i += 1
                time.sleep(2)
            except Exception as e:
                time.sleep(1)

        # login continue as mic.hunter
        # "//div[class=' Igw0E IwRSH eGOV_ _4EzTm XfCBB ']"
        # log in: "//a[@href='/accounts/login/?source=auth_switcher']"
        # username input: "//input[@name='username']"
        # password input: "//input[@name='password']"


MichaelIns = InstagramBot("YOUR_USER_ID", "YOUR_PASSWORD")
MichaelIns.login()
MichaelIns.like_photo('TAG_NAME')

# SelinaIns = InstagramBot("karroy_yumberry", "Apolar0426")
# SelinaIns.login()
# SelinaIns.like_photo('poodle')





