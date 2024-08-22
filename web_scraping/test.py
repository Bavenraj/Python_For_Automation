from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.instagram.com/reels/"

# Instantiate webdriver and open a Chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Maximize browser window
driver.maximize_window()

# Load the webpage 
driver.get(url)


reels_container = driver.find_element(By.XPATH,'//*[@id="mount_0_0_u5"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[3]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]')
# Scroll through the Reels horizontally every 10 seconds, stop after 60 seconds
scroll_time = 60  # Total time to scroll
interval = 10     # Interval between scrolls
scroll_amount = 300  # Amount to scroll each time, adjust as necessary

for i in range(0, scroll_time, interval):
    # Scroll horizontally within the reels container
    driver.execute_script(f"arguments[0].scrollBy({scroll_amount}, 0);", reels_container)
    # Wait for the defined interval
    sleep(interval)
