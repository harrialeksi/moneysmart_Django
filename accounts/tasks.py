import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

ORIGINAL_DOMAIN = os.getenv(
    'ORIGINAL_DOMAIN')


def job():
    from .views import scrape_account
    url = ORIGINAL_DOMAIN + 'savings-account'
    scrape_account(url)
    print("I'm working...")


def task():

    while True:
        schedule.run_pending()
        time.sleep(1)


# schedule.every(10).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
