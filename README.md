# EatIT CLI - What's on the menu today?

A python script that will tell you what is on the EatIT canteen's menu today.

The script will scrape the https://intranet.itu.dk/organisation/canteen, which it requires your ITU credentials to do.
After it has scraped the data, it will save it to a sqlite local database, found at ~/.eatit.db in your system, in order to quickly query for today's menu for the rest of the week.

After Monday 08:00, the script will prompt for ITU credentials again, to scrape for the new week's menu. The sqlite database is deleted and recreated so it won't store outdated data.

## Installation

You need the following packages to run the script: selenium, beautifulsoup, peewee. Run the following commands to install the libraries via pip.

`$ pip install selenium`

`$ pip install beautifulsoup4` 

`$ pip install peewee`

You will also need to install the chromedriver (and the browser Google Chrome, if you don't have it already).

See [here](https://pypi.python.org/pypi/chromedriver_installer) for installation of the chromedriver.

## Running the program
After you have installed the required packages, you are ready to run your EatIT cli.

`$ python eatit.py`

The first time the program is run (and at the start of each week), it will take some time to scrape. After that, running the program will be super quick as it will query the sqlite database.