import datetime
date1 = datetime.date(int(input()),int(input()),int(input()))
date2 = datetime.date(int(input()),int(input()),int(input()))
differ = (date1 - date2)
print(abs(differ.days * 24 * 60))