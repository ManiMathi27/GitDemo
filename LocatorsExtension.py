from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Manimegalai.M\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=us")
driver.find_element_by_css_selector("#username").send_keys('Manimegalai M')
driver.find_element_by_css_selector(".password").send_keys("Mani")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//*[@name='cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)