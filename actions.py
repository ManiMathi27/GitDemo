from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
childMenu = driver.find_element_by_link_text("Top")
action.move_to_element(childMenu).click().perform()