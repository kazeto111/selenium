from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pg
import time

driver = webdriver.Chrome()
url = 'https://colab.research.google.com/drive/1RqMlrV4xQekAnS4mBW3_tfl6f0hFQeM7'

login_id = ''
pas = ''

# ページを開く
driver.get(url)

time.sleep(5)
# ログイン画面:userid
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(login_id)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)

# ログイン画面:pwd
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(pas)
driver.find_element_by_xpath("//*[@id='passwordNext']").click()
time.sleep(10)


executor_url = driver.command_executor._url
session_id = driver.session_id

print(driver.current_url)
print(executor_url, session_id)

pg.hotkey("command", "fn", "F9")
