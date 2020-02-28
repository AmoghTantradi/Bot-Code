from selenium import webdriver
from time import sleep
from login_info import username,password
#this class provides a set of tools to spam other accounts on twitter or to tweet a lot
class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        sleep(2)
        self.login()

    def login(self):  # logs in
        self.driver.get('https://twitter.com/home')
        sleep(1)  # waits for the login page to load
        login_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/form/div/div[1]/label/div[2]/div/input')
        login_box.click()
        login_box.send_keys(username)
        password_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/form/div/div[2]/label/div[2]/div/input')
        password_box.click()
        password_box.send_keys(password)
        login_box = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/form/div/div[3]/div/div")
        login_box.click()

    def tweet(self, message):  # this sends the tweets but unfortunately, twitter does not allow repeated tweets for good reason
        tweet_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/header/div/div/div/div/div[3]/a/div/span/div/div/span')
        tweet_box.click()
        text_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')
        text_box.click()
        text_box.send_keys(message)
        send_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        send_box.click()

    def send_message(self, name, message):
        messages_tab = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[4]/div/div[2]/span')
        messages_tab.click()
        send_message_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/section[1]/div[1]/div/div/div/div/div[2]/a/div')
        send_message_box.click()
        search_bar_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[1]/div/div/div[2]/input')
        search_bar_box.click()
        search_bar_box.send_keys(name)
        sleep(2)
        first_result = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/span')

        try:
            first_result.click()
            sleep(2)
            next_box = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div/div/span')
            sleep(2)
            next_box.click()
            message_box = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div')
            # look for where 'white space' is mentioned to find the right xpath
            message_box.click()
            message_box.send_keys(message)
            sleep(2)
            button_box = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[3]/div')
            button_box.click()
            print('Message Sent Succesfully')
        except Exception:
            print('Cannot be messaged, will exit now')
            exit_tab = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div')
            exit_tab.click()
        home_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[1]/div')
        home_button.click()


