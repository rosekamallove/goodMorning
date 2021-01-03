
from apscheduler.schedulers.blocking import BlockingScheduler


from flowers import good_morning

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(good_morning, 'interval', hours=24)

sched.start()
