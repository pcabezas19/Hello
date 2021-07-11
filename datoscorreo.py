from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= r"C:\dchrome\chromedriver.exe")
driver.get("http://compendiumdev.co.uk/selenium/testpages/calculate.php")

usuario = driver.find_element_by_id("number1")
usuario.send_keys("50")

usuario = driver.find_element_by_id("number2")
usuario.send_keys("50")
usuario.send_keys(Keys.ENTER)

time.sleep(3)


