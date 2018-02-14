from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

def Login(username, password, url, username_field_id, password_field_id, submit_button_id, headless):
    # Adds headless args to the options later parsed to the webdriver.
    options = Options()
    options.add_argument("log-level=3")
    if headless:
        options.add_argument("--headless")
        print("Headless mode enabled")

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


# CLI Support
import argparse
import getpass

parser = argparse.ArgumentParser()
parser.add_argument("--headless", help="Turns on headless mode", action="store_true")
args = parser.parse_args()

url = "https://intranet.itu.dk/organisation/canteen"

# Get the username and password as prompt
un = input("Username:")
try:
    pw = getpass.getpass()
except Exception as error:
    print("Error occured...")

# Check if headless or not
if args.headless:
    html = Login(un, pw, url, "username", "user_pass", "btnLogin", True)
else:
    html = Login(un, pw, url, "username", "user_pass", "btnLogin", False)

# Set up soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Clear the terminal.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Get today's weekday. 0 = monday, 6 = sunday
import datetime
today = datetime.datetime.today().weekday()


if today == 0:
    print("The Menu today (Monday):")
    monday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day1Menu"})
    print(monday.text)
elif today == 1:
    print("The Menu today (Tuesday):")
    monday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day2Menu"})
    print(monday.text)
elif today == 2:
    print("The Menu today (Wednesday):")
    monday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day3Menu"})
    print(monday.text)
elif today == 3:
    print("The Menu today (Thursday):")
    monday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day4Menu"})
    print(monday.text)
elif today == 4:
    print("The Menu today (Friday):")
    monday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day5Menu"})
    print(monday.text)
else:
    print("The canteen is closed in the weekend, sorry.")