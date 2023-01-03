from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22be" \
      "ds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
chrome_path = "/home/nkdtech/Desktop/python projects/chromedriver_linux64/chromedriver"
chrom_options = Options()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(executable_path=chrome_path), options=chrom_options)
driver.get(url)
try:
    k = 0
    captcha = driver.find_element(By.XPATH, "/html/body")
    for k in range(0, 400):
        captcha.click()
        sleep(0.001)
        k += 1
except:
    print("no captcha")
finally:
    print("successfully entered site")
houses = driver.find_elements(By.CSS_SELECTOR,
                              "li[class='ListItem-c11n-8-73-8__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation']")

sleep(10)
i = 0
house_details = []
for house in houses:
    try:
        details = {}
        details['house_price'] = house.find_element(By.XPATH,
                                                    f'/html/body/div[1]/div[5]/div/div/div/div[1]/ul/li[{houses.index(house)}]/article/div/div[1]/div[2]').text,
        details['house_url"'] = house.find_element(By.XPATH,
                                                   f'/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/li[{houses.index(house)}]/article/div/div[1]/a').get_attribute(
            "href"),
        details['house_address"'] = house.find_element(By.XPATH,
                                                       f'/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/li[{houses.index(house)}]/article/div/div[1]/a/address').text,
        house_details.append(details)
    except:
        continue
    finally:
        continue
print(house_details)
