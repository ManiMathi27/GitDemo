from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

#driver.find_element_by_name("name").send_keys('Manimegalai M')
#CSS Selector syntax : tagname[attribute='value'], scanning starts from top left
driver.find_element_by_css_selector("input[name='name']").send_keys('Mani')
driver. find_element_by_name("email").send_keys('Mani')
driver.find_element_by_id("exampleCheck1").click()
#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_css_selector("#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)

#Assert
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message
#//*[contains(@class,'alert-success')]--Xpath
#[class*='alert-success'] --CSS