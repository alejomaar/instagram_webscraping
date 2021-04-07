from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

path = r'D:\Descargas\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get('https://www.instagram.com/')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("alejo_ingeniero")
password.clear()
password.send_keys("roquero2")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

#Second Page
#Make the search
keyword = "#ivanduque"
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.XTCLo")))
searchbox.clear()
searchbox.send_keys(keyword)

time.sleep(4) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/"+keyword[1:]+"/')]")))
my_link.click()

#Third Page

#scroll down 2 times
#increase the range to sroll more
n_scrolls = 1
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

anchors = driver.execute_script("return [...document.querySelectorAll('a')].map(a=> a.href)")
#target all the link elements on the page
anchors = [a for a in anchors if a.startswith("https://www.instagram.com/p/")]
anchors= anchors[0:4]
ListUsername = [];
ListComment = [];
#document.querySelector(".C4VMK>span").textContent
#document.querySelector("._1o9PC").innerText
for page in anchors:
    driver.get(page)
    time.sleep(5)
    username = driver.execute_script("return document.querySelector('.C4VMK').querySelector('span').innerText");
    comment = driver.execute_script("return document.querySelector('.C4VMK>span').textContent");
    date = driver.execute_script("return document.querySelector('._1o9PC').innerText");
    ListUsername.append(username)
    ListComment.append(comment)

print(ListUsername)
print(ListComment)

