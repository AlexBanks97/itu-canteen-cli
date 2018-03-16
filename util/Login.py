from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import getpass

# Get the username and password as prompt
username = input("Username:")
try:
    password = getpass.getpass()
except Exception as error:
    print("Error occured...")


def Login(url, username_field_id, password_field_id, submit_button_id):
    # Adds headless args to the options later parsed to the webdriver.
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")

    # Specify what browser to use, and navigate to the desired website. 
    # You may need to modify this if you wish to use chrome instead.
    browser = webdriver.Chrome(chrome_options=options) 
    browser.get(url)

    # Wait for the page to load. 10 Seconds for timeout.
    # If/when loaded, acquire the username and password field.
    try:
        username_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,username_field_id)))
        password_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,password_field_id)))
        submit_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,submit_button_id)))
        print(username_field)
    except TimeoutException:
        print("Loading took too long. Timeout Exception")  

    # Enter login-information and submit.
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.submit()

    # return source code
    return browser.page_source