from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlretrieve
webdriver_options=webdriver.ChromeOptions()
driver=webdriver.Chrome('chromedriver')
webdriver_options.add_argument('--headless')
webdriver_options.add_argument('--no-sandbox')
webdriver_options.add_argument('--disable-dev-shm-usage')
webdriver_options.add_argument('window-size=1920x1080')
webdriver_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
driver=webdriver.Chrome('chromedriver',options=webdriver_options)

driver.get("https://www.google.com/")
a = '시바견'
name=driver.find_element_by_name("q")
name.clear()
name.send_keys(a)

bt1=driver.find_element_by_class_name("gNO89b")
time.sleep(5)
bt1.click()

bt2=driver.find_element_by_xpath("""//*[@id="hdtb-msb-vis"]/div[2]/a""")

time.sleep(5)

bt2.click()

links = []
for i in range(0,100):
   if i%40==0:
      img=driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

   time.sleep(5)
   try:
      img[i].click()
   except:
      img = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
      time.sleep(5)
      img[i].click()

   time.sleep(5)

   link=driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img""").get_attribute("src")
   # links.append(link)

   try:
      links.append(link)
      print(link)

   except Exception as e:
      print('Error raised at {}, {}'.format(link, e))

print("link download complete")
count=0
for link in links:
   count+=1

   try:
      urlretrieve(link,a+str(count)+".jpg")
      print(str(count)+"th file downloaded")
   except Exception as e:
      print(e)
            

