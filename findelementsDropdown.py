import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("#autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "Ind":
        country.click()
        break
print(driver.find_element_by_css_selector("#autosuggest").text)
assert driver.find_element_by_css_selector("#autosuggest").get_attribute('value') == "Ind"



