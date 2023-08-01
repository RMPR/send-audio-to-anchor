import os
from time import sleep
import pyperclip
from pynput.keyboard import Key, Controller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

browser.get('https://podcasters.spotify.com/pod/login') 

username = browser.find_element(By.ID, 'email')
username.send_keys('email')

password = browser.find_element(By.ID, 'password')
password.send_keys('password')

cookie_button = browser.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_button.click()
# Find submit button with text "Login"
submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")

sleep(5)
submit_button.click()
sleep(5)

# Once logged in go to the upload page
sleep(7)
keyboard = Controller()
for file_path in [mp3_file for mp3_file in os.listdir() if mp3_file.endswith('.mp3')]:
	browser.get('https://podcasters.spotify.com/pod/dashboard/episode/wizard')
	sleep(5)
	file_input = browser.find_element(By.XPATH, "//button[@data-encore-id='buttonPrimary']")
	file_input.click()
	sleep(2)
	# Needs to copy-paste here because of some limitations of pyautogui/pynput
	pyperclip.copy(f"{file_path}")
	with keyboard.pressed(Key.ctrl):
		keyboard.press('v')
		keyboard.release('v')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(5)
	file_path_without_extension = file_path.replace(".mp3", "")
	title_input = browser.find_element(By.XPATH, "//input[@name='title']")
	title_input.send_keys(file_path_without_extension)
	episode_description = browser.find_element(By.XPATH, "//div[@role='textbox']")
	episode_description.send_keys(file_path_without_extension)
	publication_time = browser.find_element(By.XPATH, "//label[@for='publish-date-now']")
	publication_time.click()
	explicit_content = browser.find_element(By.XPATH, "//label[@for='no-explicit-content']")
	explicit_content.click()
	# Create a WebDriverWait to wait for the dialog
	wait = WebDriverWait(browser, 420)
	wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-encore-id='buttonSecondary' and text()='Replace']")))
	submit_button = browser.find_element(By.XPATH, "//button[@data-encore-id='buttonPrimary']")
	submit_button.click()
	sleep(2)
	submit_button = browser.find_element(By.XPATH, "//button[@data-encore-id='buttonPrimary']")
	submit_button.click()
	sleep(2)
	submit_button = browser.find_element(By.XPATH, "//button[@data-encore-id='buttonPrimary']")
	submit_button.click()
	os.remove(file_path)
	print(file_path, "deleted")
	sleep(8)