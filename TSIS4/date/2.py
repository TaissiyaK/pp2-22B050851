from datetime import date, timedelta
current = date.today()
yesterday = date.today() - timedelta(days=1)
tomorrow = date.today() + timedelta(days=1)
print(f'today is :{current}, yesterday is {yesterday}, tomorrow is {tomorrow}')