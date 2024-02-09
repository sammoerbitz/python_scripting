# chat gpt
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.therandomscalemachine.com/")

# Find the element by XPath and click it
# buttons = {
#     "E": "/html/body/div[5]/div[2]/a",
#     "A": "/html/body/div[5]/div[2]/a",
#     "D": "",
#     "G": "",
#     "B": "",
#     "E": "",
# }

i = 0
start = 0
lap = False
key = 'y'
while key != 'q':
    key = keyboard.read_key()
    if (i == 0):
        end = time.time()
        print("Split Time: ", end - start)
        start = time.time()
    
    if (key == 'space'):
        i += 1
        if( i % 2 == 1):
            print(f"Key : {key}")
            print(i)
            driver.find_element(By.CSS_SELECTOR,"""body > div:nth-child(5) > div.middle > a""").click()
    i = 0 if i == 24 else i
    
    
# driver.find_element(By.XPATH,"(//div[5]//div[2]//a[@attribute='value'])[]").click()


# Close the browser
driver.close()
