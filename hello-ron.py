# test python script
import time
import datetime
today = []
now = datetime.date.today()
today.append(now)

while True:
    print ("Hello Ron, How is your day? Today is: " + str(today[0]))
    time.sleep(10)
