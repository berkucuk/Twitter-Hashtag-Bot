from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import sys


page="https://twitter.com/i/flow/login"
USER = "username"
PASSWORD = "password"

while True:
    try:
        driver = webdriver.Firefox()
        driver.get(page)
        time.sleep(15)

        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').click
        username_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_input.send_keys(USER)                 #"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
        time.sleep(4)
        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        login_button.click()


        time.sleep(5)

        password_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(PASSWORD)
        time.sleep(4)
        # find the element for login and click on it
        login_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()                         #"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"

        hastag = "elonmusk"
        hastag_url = f"https://twitter.com/search?q=%23{hastag}&src=typed_query&f=live"
        #print(hastag_url)
        time.sleep(5)
        driver.get(hastag_url)
        time.sleep(5)
        run_timer = 0
        temp_text = " "
        tweet = ""
        while True:
            run_timer += 1
            for scrool in range(3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            time.sleep(5)
            for i in range(10):
                try:
                    tweet = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[{i}]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span[1]').text            # "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[4]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span[1]"
                    print("- ",tweet)

                except:
                    pass
            if temp_text == tweet:
                break
            temp_text = tweet

    except KeyboardInterrupt:
        break
        sys.exit(0)
    except:
        pass
