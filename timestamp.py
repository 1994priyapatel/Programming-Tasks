import time
import datetime
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%B %d,%Y')
print "unix:",ts,", natural:",st
