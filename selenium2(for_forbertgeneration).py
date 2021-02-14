from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule

def selenium_for_bertgeneration():
    driver = webdriver.Chrome()
    url = "https://colab.research.google.com/drive/1RqMlrV4xQekAnS4mBW3_tfl6f0hFQeM7#scrollTo=44kd-Wz2UbfU"

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

    # Google Colab
    print(driver.current_url)
    #driver.find_element_by_xpath('//*[@id="cell-99Q_nwYSY7WL"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click() #セルの実行

    #マウント(後で例外処理追加)
    try:
        driver.find_element_by_xpath('//*[@id="cell-rZivOuBGUT-_"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
        driver.find_element_by_xpath('//*[@id="cell-rZivOuBGUT-_"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/colab-static-output-renderer/div[2]/pre/a').click()
        driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div').click()
        driver.find_element_by_xpath('//*[@id="submit_approve_access"]/div/button/div[2]').click()
        driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/span/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/span/'
                                     'div/textarea').send_keys(Keys.COMMAND, Keys.NUMPAD1)
        driver.find_element_by_xpath('//*[@id="cell-rZivOuBGUT-_"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/colab-static-output-renderer/'
                                     'div[2]/pre/input').send_keys(Keys.SHIFT, Keys.INSERT + Keys.ENTER)

    except:
        pass





    driver.find_element_by_xpath('//*[@id="cell-44kd-Wz2UbfU"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()

    #pip
    driver.find_element_by_xpath('//*[@id="cell-CXMWqhc4U0ZS"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()
    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="cell-oaBVCJYmW72P"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button').click()

schedule.clear()
schedule.every(60).minutes.do(selenium_for_bertgeneration)
while True:
  schedule.run_pending()
  time.sleep(1)

#参考サイト
#selenium
# https://qiita.com/Fortinbras/items/4cfa9269af2ab8d1d4d5

#xpath
#https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics
