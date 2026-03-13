# 1 find_element(locator_name, locator value)
# single element
# returns single web element
#no such element exception
# 2. find_elements(locator_name, locator value)
# multiple elements
# returns list of web elements
#empty set
from time import sleep

#locator = address of an element

#types of locators
#direct locators
#ID
#NAME
#CLASSNAME
#TAG NAME
#text based
#LINK TEXT
#PARTIAL LINK TEXT
#expression based locators
#CSS SELECTORS
#XPATH

#click()-
#send_keys('text')- taking user input

# username=driver.find_element(By.ID,"userName")
# username.send_keys("Harshita")
# driver.find_element(By.ID,'userName').send.keys("Harshita")
# driver.find_element(By.ID,'userEmail-wrapper').send.keys("harshita@gmail.com")
# driver.find_element(By.ID,'currentAddress-wrapper').send.keys("gvjhvj")
# driver.find_element(By.ID,'permanentAddress-wrapper').send.keys("values")
# driver.find_element(By.ID,'submit').click()
# sleep(2)

#ID locator
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

#ID locator
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes")
sleep(2)
driver.find_element(By.ID,"nav-search-submit-button").click()

#NAME locator
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,'field-keywords').send_keys("shoes")
sleep(2)
driver.find_element(By.ID,'nav-search-submit-button').click()

#CLASS_NAME locator
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,'nav-input.nav-progressive-attribute').send_keys("shoes")
sleep(2)
driver.find_element(By.ID,'nav-search-submit-button').click()

#TAG_NAME locator
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
driver.find_element(By.TAG_NAME,'input').send_keys("Harshita")
driver.find_element(By.TAG_NAME,'input').send_keys("harshita@gmail.com")
driver.find_element(By.TAG_NAME,'textarea').send_keys("Rajasthan")
driver.find_element(By.TAG_NAME,'textarea').send_keys("Jaipur")
sleep(2)
driver.find_element(By.ID,'nav-search-submit-button').click()

#LINK_TEXT locator
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,"Today's Deals").click()

#PARTIAL_LINK_TEXT locator
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Game').click()

#CSS_SELECTOR
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"] ').send_keys('hoodies')



driver.close()
driver.quit()
sleep(5)





