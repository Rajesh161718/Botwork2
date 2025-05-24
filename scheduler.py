# scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler

def scheduled_task():
    print("📅 Scheduled task executed!")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, 'interval', seconds=30)
    scheduler.start()

def start_scheduler():
    print("Scheduler started")
