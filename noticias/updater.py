from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scrape_economia, scrape_ciencias, scrape_meio_ambiente, scrape_tecnologia

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_economia, 'interval', minutes=15)
    scheduler.add_job(scrape_tecnologia, 'interval', minutes=18)
    scheduler.add_job(scrape_meio_ambiente, 'interval', minutes=21)
    scheduler.add_job(scrape_ciencias, 'interval', minutes=24)
    scheduler.start()