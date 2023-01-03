from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import sys
from time import sleep

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeoZH-6UI7SWxkqixkcPGnUYySSCR7vip6cxJ-gW2q_LAS0Lg/viewform?usp=sf_link"
zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.97677392568409%2C%22east%22%3A-121.46340722646534%2C%22south%22%3A37.783700516400216%2C%22north%22%3A38.61575831419846%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
captcha = "https://www.zillow.com/captchaPerimeterX/?url=%2fb%2falta-waverly-oakland-ca-9NV4t5%2f&uuid=2c8bbdb7-7a15-11ed-8e3a-6d706b717465&vid="
# html_file = requests.get(url=zillow_url)
# html_file.raise_for_status()
# soup = BeautifulSoup(html_file.text, "lxml")
# print(soup.prettify())
# # print(soup.title.string)
# desired_data = soup.find("dive", id='search-page-react-content')
# print(desired_data)

driver_path = "/home/nkdtech/Desktop/python projects/chromedriver_linux64/chromedriver"
chrom_options = Options()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(driver_path), options=chrom_options)
driver.get(zillow_url)
# desired_data=driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/div/div/div[1]/ul")
try:
    print("dealing with captcha")
    element = driver.find_element(By.XPATH, '/html/body')
    action = ActionChains(driver)
    click = ActionChains(driver)
    frame_x = element.location['x']
    frame_y = element.location['y']
    x_move = frame_x + element.size['width']*0.5
    y_move = frame_y + element.size['height']*0.5
    action.move_to_element_with_offset(element, x_move, y_move).click_and_hold().perform()
    sleep(10)
    action.release(element)
    action.perform()
    sleep(0.2)
    action.release(element)
except:
    print("")
finally:
    houses = []
for i in range(1, 50):
    try:
        houses.append(driver.find_element(By.XPATH, f'//*[@id="grid-search-results"]/ul/li[{i}]'))
    except:
        continue
    finally:
        i += 1
house_data = []

house_link = houses[0].find_element(By.TAG_NAME, "a"),
# "house_location": house.find_element(By.),
house_price = houses[0].find_element(By.TAG_NAME, "span")
print(house_link)
print(house_price.text)
