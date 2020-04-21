from datetime import datetime as dt
t = '07:05:45PM'

t = dt.strptime(t, '%I:%M:%S%p')
print(t.strftime('%H:%M:%S'))
