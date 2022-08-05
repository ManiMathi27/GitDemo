from selenium import webdriver

ValidateText = "Manimegalai"

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://office-mfa.access-apj.sap.com/Citrix/OfficeMFAWeb/")
driver.find_element_by_css_selector("#name").send_keys(ValidateText)
driver.find_element_by_css_selector("#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert ValidateText in alertText
alert.accept()
driver.find_element_by_css_selector("#confirmbtn").click()
alert = driver.switch_to.alert
alert.dismiss()

