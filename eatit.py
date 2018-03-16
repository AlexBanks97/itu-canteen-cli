import datetime
from dateutil.relativedelta import relativedelta, MO
import os
import sqlite3
from peewee import SqliteDatabase, IntegerField, CharField, DateTimeField, Model
from pathlib import Path
from os.path import expanduser

### CONSTANTS ###
HOME = expanduser("~")
DB_PATH = os.path.join(HOME, ".eatit.db")
DB = SqliteDatabase(DB_PATH)

### DATA MODELS ###

# day = 0-6, mon=0, sun=6
class Day(Model):
    day = IntegerField()
    menu = CharField()
    
    class Meta:
        database = DB

class LastScrape(Model):
    date = DateTimeField()

    class Meta:
        database = DB

# Connect to database. If it does not exist, create it.
DB.connect()
# Create tables if they do not exist.
DB.create_tables([Day, LastScrape])

def MenuToday():
    # Check if today is a weekend day.
    today = datetime.date.today()
    if today.weekday() > 4:
        print("It is weekend, so EatIT is closed :(")
        return

    # Query LastScrape for the last scrape
    last_scrape = LastScrape.select(LastScrape.date)

    # Get date at last monday at 8am
    last_monday = today + relativedelta(weekday=MO(-1))
    last_monday = datetime.datetime(last_monday.year, last_monday.month, last_monday.day, 8)

    # If LastScrape table is empty, or if it has been 7 days since last monday. 
    if len(last_scrape) < 1 or (datetime.datetime.now() - last_monday) > datetime.timedelta(days=7):
        # new up the database again
        DB.drop_tables([Day, LastScrape])
        DB.create_tables([Day, LastScrape])

        from util import CScrape as cs
        menus = cs.GetMenus()
        
        # Iterate menu items and insert into DB
        for idx, item in enumerate(menus):
            menu_to_save = Day(day=idx, menu=item)
            menu_to_save.save()

        # Save new scrape date to eatitdb
        newscrapedate = LastScrape(date=datetime.datetime.now())
        newscrapedate.save()

        # Call MenuToday again, this time querying the sqlite db
        MenuToday()

    # Query eatit.db
    else:
        query = Day.select(Day.day, Day.menu).where(Day.day == today.weekday())
        if len(query) == 1:
            import calendar
            print("Today is", calendar.day_name[today.weekday()])
            print("Menu:\n" + query[0].menu)
        else:
            print("Something went terribly wrong...")
            print("")

MenuToday()
