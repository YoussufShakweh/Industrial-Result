from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

# Enter The Student Number
std_num = input("Enter Your Number: ")

url = "http://moed.gov.sy/12th/index.php"
driver = webdriver.Chrome()

while True:
  try: 
    driver.get(url)
    break
  except WebDriverException:
    driver.refresh()

# Select Branch
branch = driver.find_element(by=By.ID, value="branch")
select_branch = Select(branch)
select_branch.select_by_value("6") # To Chose Industrial select 6

# Select Sub - Branch
pro = driver.find_element(by=By.ID, value="sub-branch")
select_sub_branch = Select(pro)
# Auto Select Computer Technology
select_sub_branch.select_by_value("p06")

# Create City List
city = driver.find_element(by=By.ID, value="city")
select_city = Select(city)
# Auto Select Hama
select_city.select_by_value("7")

# Create Stdnum
stdnum = driver.find_element(by=By.ID, value="stdnum")
stdnum.send_keys(std_num)

# Create Submit Button
submit = driver.find_element(by=By.ID, value="submit")
submit.click()


input("Press to close ...")
