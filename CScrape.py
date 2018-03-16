########## Imports ##########
import Login as lg
import os
from bs4 import BeautifulSoup

URL = "https://intranet.itu.dk/organisation/canteen"

# Acquire HTML from the URL.
HTML = lg.Login(URL, "username", "user_pass", "btnLogin")

# Set up soup
soup = BeautifulSoup(HTML, 'html.parser')

# Clear the terminal. Selenium prints some weird Devtools listening stuff.
os.system('cls' if os.name == 'nt' else 'clear')

def GetMenus():
    monday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day1Menu"})
    tuesday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day2Menu"})
    wednesday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day3Menu"})
    thursday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day4Menu"})
    friday = soup.find("div", {"id": "phmain_0_phmaincontent_4_Day5Menu"})

    menus = [monday.text, tuesday.text, wednesday.text, thursday.text, friday.text]
    return menus
