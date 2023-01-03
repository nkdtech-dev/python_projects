import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

MY_SEARCH = "business"
text = ["wow", "nice one", 'i love this', "cool"]
INSTAGRAM_URL = 'https://www.instagram.com/'
chrom_path = "/home/nkdtech/Desktop/python projects/chromedriver_linux64/chromedriver"

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrom_path), options=chrom_options)

driver.get(INSTAGRAM_URL)
main_login = driver.current_window_handle
sleep(2)
username = driver.find_element(By.NAME, "username").send_keys("python_nkd")
password = driver.find_element(By.NAME, "password").send_keys("qwertyuiop12,")
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button[1]').click()
sleep(5)
save_login = driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button').click()
sleep(3)
notification = driver.find_element(By.XPATH,
                                   '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
search_button = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]').click()
search_account = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys(
    MY_SEARCH)
sleep(3)
# acounts= driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]').click()
account_group = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div')
sleep(2)
account_list = account_group.find_elements(By.TAG_NAME, "div")
sleep(3)
for account in account_list:
    verified_account = account.find_elements(By.CSS_SELECTOR, "span[aria-label='Verified']")
    if len(verified_account) == 1:
        verified_account[0].click()
        sleep(5)
        follow = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button').click()
        sleep(3)
        # try:
        #     first_post = driver.find_element(By.CLASS_NAME, "_aagu").click()
        #     sleep(5)
        #     like_post = driver.find_element(By.XPATH,
        #                                     '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
        # except:
        #     continue
        # finally:
        #     sleep(5)


        followers_button = driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(3)
        followers_group = driver.find_element(By.XPATH,
                                              '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div')

        sleep(3)
        followers = followers_group.find_elements(by=By.CLASS_NAME, value="div")
        for acc in followers:
            acc.find_element(By.CSS_SELECTOR, "button[class='_acan _acap _acas _aj1-']").click()
            sleep(2)

    else:
        continue
print("clicked")
# follow= driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button').click()
# sleep(3)
# followers = driver.find_element(By.XPATH,
#                                 '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div').click()
# sleep(3)
# follow_button = driver.find_elements(by=By.CSS_SELECTOR, value="button _acan _acap _acas")
# i = 0
# for button in follow_button:
#     button.click()
#     sleep(5)
#     i += 1
# k = 0
# for handle in driver.window_handles:
#     k += 1
# print(i, k)
