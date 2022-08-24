#Made by Blocksrey
#P.S. Please abuse

from selenium.webdriver.common.by import By
from time import sleep

def find_button(driver,name):
	for button in driver.find_elements(By.CLASS_NAME,'artdeco-button__text') or {}:
		if button.text==name:
			return button

def start(driver,username,password,keywords):
	driver.get('https://www.linkedin.com/login')
	driver.find_element(By.ID,'username').send_keys(username)
	driver.find_element(By.ID,'password').send_keys(password)
	driver.find_element(By.XPATH,'//*[@type="submit"]').click()

	for page in range(1,1000000):#Should just be a while loop tbh
		driver.get('https://www.linkedin.com/search/results/people/?'+keywords+'&origin=GLOBAL_SEARCH_HEADER&page='+str(page))

		for result in driver.find_elements(By.CLASS_NAME,'reusable-search__result-container'):
			try:
				connect=find_button(result,'Connect')
				connect and connect.click()

				send=find_button(driver,'Send')
				send and send.click() or sleep(1)

			except:
				pass

#Driver
username='whatever@gaymail.com'
password='SECurePass!0721'
keywords='Game developer'

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

start(driver,username,password,keywords)

driver.quit()