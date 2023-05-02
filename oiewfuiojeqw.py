from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# navigate to Google
website = "https://www.pbtech.co.nz/category/computers/laptops/shop-all"
driver.get(website)

driver.maximize_window()
# find the element by its id

# Find the "maxFilters" element and click on it to show the filter dropdown
filters = driver.find_element(By.CLASS_NAME, "heading_wrapper--new")
filters.click()
