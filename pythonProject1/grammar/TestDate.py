import time
import datetime

localtime1 = time.localtime()
print(localtime1)
format_localtime1 = time.strftime("%Y-%m-%d %H:%M:%S",localtime1)
print(format_localtime1)

datetime1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(datetime1)
datetime2 = datetime.timedelta(1)
print(datetime2)
datetime3 = datetime.datetime.now() + datetime.timedelta(hours=-1)
print(datetime3.strftime("%Y-%m-%d %H:%M:%S"))