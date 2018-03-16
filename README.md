# EatIT CLI - What's on the menu today?

A python script that will tell you what is on the EatIT canteen's menu today.

The script will scrape the https://intranet.itu.dk/organisation/canteen, which it requires your ITU credentials to do.
After it has scraped the data, it will save it to a sqlite local database, found at ~/.eatit.db in your system, in order to quickly query for today's menu for the rest of the week.

After Monday 08:00, the script will prompt for ITU credentials again, to scrape for the new week's menu. The sqlite database is deleted and recreated so it won't store outdated data.

## Installation

You need the following packages to run the script.