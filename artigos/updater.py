from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scrape_physical_sciences_and_engineering, scrape_meio_tec, scrape_saude, scrape_cultura

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_physical_sciences_and_engineering, 'interval', hours=23)
    scheduler.add_job(scrape_cultura, 'interval', hours=23)
    scheduler.add_job(scrape_saude, 'interval', hours=23)
    scheduler.add_job(scrape_meio_tec, 'interval', hours=23)
    scheduler.start()