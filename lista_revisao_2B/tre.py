import datetime 
data = datetime.date(2025,3,20)
agora = datetime.date.today()
anos = agora.year - data.year - ((data.month, data.day)>(agora.month, agora.day))
print(anos)