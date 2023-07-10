from selenium import webdriver
import time
import os



options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])

website = 'https://twitter.com/'
path = '/Users/koichirosuzuki/Desktop/Wab_Scraping/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(path, chrome_options=options)
driver.get(website)
driver.maximize_window()

# login = driver.find_element_by_xpath('//a[@href="/login"]')
# login.click()
time.sleep(2)

username = driver.find_element_by_xpath('//input[@autocomplete="username"]')
username.send_keys("@Sukima_English_")

next_button = driver.find_element_by_xpath('//div[@role="button"]//span[text()="次へ"]')
next_button.click()

# wait of 2 seconds after clicking button
time.sleep(2)

# password
password = driver.find_element_by_xpath('//input[@autocomplete ="current-password"]')
password.send_keys("Suzuki65")  # Write Password Here
# password.send_keys(os.environ.get("TWITTER_PASS"))

# locating login button and then clicking on it
login_button = driver.find_element_by_xpath('//div[@role="button"]//span[text()="ログイン"]')
login_button.click()

# closing driver
# driver.quit()