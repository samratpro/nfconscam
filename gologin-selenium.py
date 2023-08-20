import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from gologin import GoLogin
from gologin import getRandomPort


gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGUyNzdlNGY1MWE0MzNlZDFhNDlmZjEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGUyN2M3N2E3YWQ0NzRiYjY0NTA1MGMifQ.rzws-YB2bh8zoSkU6ye_D00lByT4Gcae9O1GxviGPYo",
	"profile_id": "64e277e5f51a43189aa4a08a"
	})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"
	
service = Service(executable_path=chrome_driver_path)

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(service=service, options=chrome_options)



url = "https://www.facebook.com/hashtag/nfcon2023"
driver.get(url)
# Scroll down and wait for new content
SCROLL_WAIT_TIME = 20

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new content to load
    time.sleep(SCROLL_WAIT_TIME)

    # Extract and print the content (modify this part based on your needs)
    elements = driver.find_elements(By.XPATH, "//div[@data-ad-preview='message']")  # Replace with actual class name
    # print(elements)
    for element in elements:
        print(element.text)
        print('....\n........\n......\n')



# Close the browser
driver.quit()
time.sleep(3)
gl.stop()
