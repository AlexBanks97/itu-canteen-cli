# EatIT CLI - What's on the menu today?

A python script that scrapes the canteen's menu off their intranet website.

ITU login credentials are necessary in order to use this tool.

## Setup:
The script runs on Python 3.x and uses the following packages:

Selenium and bs4

They can be install through Pip as follows:

`$ pip install selenium`

`$ pip install bs4`

You will also need to install the chromedriver (and the browser Google Chrome, if you don't have it already).

See [here](https://pypi.python.org/pypi/chromedriver_installer) for installation of the chromedriver.

## Usage:

The script takes up to 3 arguments: Username and Password, which are required, and then "--headless" for headless mode.

Normal:
`$ python canteen-scraper.py username password`

Headless: 
`$ python canteen-scraper.py username password --headless`
