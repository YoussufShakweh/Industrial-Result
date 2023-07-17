from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import selenium.common.exceptions as sel_ex


try:
  # Enter Year And The Student ID
  year = input("Enter The Year: ")
  std_id = input("Enter Your Number: ")
  driver = webdriver.Chrome()
  url = f"http://secondary{year}.moed.gov.sy/industrial/index.php"
  driver.get(url)

  # Create City List
  city = driver.find_element(by=By.ID, value="city")
  select_city = Select(city)
  # Auto Select Hama
  select_city.select_by_value("7")

  # Create Profession List
  pro = driver.find_element(by=By.ID, value="proname")
  select_pro = Select(pro)
  # Auto Select IT
  select_pro.select_by_value("p06")

  # Create Stdnum
  stdnum = driver.find_element(by=By.ID, value="stdnum")
  stdnum.send_keys(std_id)

  # Create Submit Button
  submit = driver.find_element(by=By.ID, value="Submit")
  submit.click()
except:
  print(sel_ex)

input("Press any key to close ...")
