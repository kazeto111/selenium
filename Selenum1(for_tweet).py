from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule

driver = webdriver.Chrome()
url = "https://colab.research.google.com/drive/1R3H-sGzhtFsf9KCBxf5yaz5i0xfZAIRG?usp=sharing"

login_id = ''
pas = ''

# ページを開く
def selenium1_for_tweet():
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

    # Google Colab
    print(driver.current_url)
    #driver.find_element_by_xpath('//*[@id="cell-99Q_nwYSY7WL"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click() #セルの実行

    #例外処理追加
    driver.find_element_by_xpath('//*[@id="cell-xMkekVF4yCxT"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
    #try:

    #except:
        #pass
    driver.find_element_by_xpath('//*[@id="cell-kRIeWv9iQa6y"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="cell-mETmBXj5X4qa"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="cell-xMkekVF4yCxT"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="cell-qQ47BZmCatg_"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="cell-Xo6BMMGpycnk"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()

schedule.clear()
schedule.every(12).hours.do(selenium1_for_tweet)
while True:
  schedule.run_pending()
  time.sleep(1)
#参考サイト
#selenium
# https://qiita.com/Fortinbras/items/4cfa9269af2ab8d1d4d5

#xpath
#https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics
