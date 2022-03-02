from apscheduler.schedulers.background import BackgroundScheduler
from dailycandle import views
import sys, socket

def start():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 47200))
    except socket.error:
        print("!!!scheduler already started, DO NOTHING")
    else:
        scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
        #scheduler.add_job(views.format_save_data,"interval",minutes=30,id="stock_001",replace_existing=True)
        #scheduler.add_job(views.send_daily_email, "interval", minutes=2, id="stock_001", replace_existing=True)
        scheduler.add_job(views.format_save_data, 'cron', hour=17, minute=45, end_date='2030-12-31',id="stock_001",replace_existing=True)
        scheduler.start()
