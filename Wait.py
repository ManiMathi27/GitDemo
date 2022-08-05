#implicit wait---Global wait(if we're giving 5 sec wait it shouldn't wait completey 5 secs to run next step, it will resume if the app takes to load 1.5 secs)
#Explicit wait--

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

list = []
list1 = []

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#time.sleep(20)
#driver.implicitly_wait(60)
#driver.maximize_window()
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
count = len(driver.find_elements_by_xpath("//div[@class='product']"))
assert count == 3
time.sleep(60)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4(child to parent) only possibe in Xpath not in CSS
for button in buttons:
    list.append((button.find_element_by_xpath("parent::div/parent::div/h4").text))
    button.click()
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoCode"))
time.sleep(50)
veggies = driver.find_elements_by_css_selector("p.product-name")
for Veg in veggies:
    list1.append(Veg.text)

print(list1)
assert list == list1
time.sleep(20)
originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
time.sleep(40)
driver.find_element_by_css_selector("button.promoBtn").click()
time.sleep(30)
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountAmount) < int(originalAmount)
time.sleep(30)
print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_element_by_xpath("//tr/td[5]/p")

sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

totalAmount = int(driver.find_element_by_css_selector("..totAmt").text)
assert sum == totalAmount