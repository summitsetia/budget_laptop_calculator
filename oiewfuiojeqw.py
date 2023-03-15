from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to pbtech.co.nz
driver.get("https://www.pbtech.co.nz")

# find the "Departments" menu and hover over it
departments_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle'][text()='Departments']"))
)
ActionChains(driver).move_to_element(departments_menu).perform()

# find the "Computers" category and click it
computers_category = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Computers']"))
)
computers_category.click()

# find the "Laptops" sub-category and click it
laptops_submenu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Laptops')]"))
)
laptops_submenu.click()

# wait for the laptops page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Laptops')]"))
)

# close the browser
driver.quit()
