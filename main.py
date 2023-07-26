from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

# Enter The Student Number
std_num = input("Enter Your Number: ")

url = "http://moed.gov.sy/12th/index.php"
driver = webdriver.Edge()

while True:
  try: 
    driver.get(url)
    break
  except WebDriverException:
    driver.refresh()

# Find Selection Webelement "Branch" and Select Industrial
Select(driver.find_element(By.ID, "branch")).select_by_value('6')

# Find Selection Webelement "Sub-Branch" and Select Computer Technology
Select(driver.find_element(By.ID, "sub-branch")).select_by_value("p06")

# Find Selection Webelement "City" and Select Hama
Select(driver.find_element(By.ID, "city")).select_by_value("7")

# Find Webelement "stdnum" and Fill It
driver.find_element(by=By.ID, value="stdnum").send_keys(std_num)

# Find Webelement "Submit" and Click It
driver.find_element(by=By.ID, value="submit").click()

input("Press to close ...")
