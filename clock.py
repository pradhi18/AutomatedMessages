from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from message import send_message


sched = BlockingScheduler()

sched.add_job(send_message, 'interval', hours=3)

sched.start()