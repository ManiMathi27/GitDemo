from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))


for i in checkboxes:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_xpath("//input[@id='hide-textbox']").click()

assert not driver.find_element_by_id("displayed-text").is_displayed()

