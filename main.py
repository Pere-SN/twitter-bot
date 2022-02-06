from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
CHROMIUM_PATH = Service("Chromium Path")
PROMISED_DOWN = '1000'
PROMISED_UP = '1000'
TWITTER_NAME = 'Your twitter name'
TWITTER_EMAIL = 'Your twitter email'
TWITTER_PASSWORD = 'Your twitter password'
PROVIDER_TWEETER_ACCOUNT = '@account'


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/es')
        self.driver.find_element(By.ID, '_evidon-banner-acceptbutton').click()
        self.driver.find_element(By.CLASS_NAME, 'start-text').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text

    def tweet_at_provider(self):
        message = f'Hey{PROVIDER_TWEETER_ACCOUNT}, why is my internet speed {self.down}down/{self.up}' \
                  f'up when I pay for 1000down/1000up?'
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        self.driver.find_element(By.NAME, 'text').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, "//*[text()='Next']").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, 'text').send_keys(f'{TWITTER_NAME}')
        self.driver.find_element(By.XPATH, "//*[text()='Next']").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, "//*[text()='Log in']").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block').send_keys(message)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "//div[@data-testid='tweetButtonInline']//span[contains(., 'Tweet')]").click()


tweet_bot = InternetSpeedTwitterBot(CHROMIUM_PATH)

tweet_bot.get_internet_speed()
tweet_bot.tweet_at_provider()
