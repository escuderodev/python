from datetime import date, datetime, time, timedelta

data_nascimento = date(1984, 4, 26)
print(data_nascimento)

data_atual = date.today()
print(data_atual)

date_and_time = datetime(1984, 4, 26, 12, 30, 27)
print(date_and_time)

date_and_time_current = datetime.today()
print(date_and_time_current)

hour = time(10, 30, 28)
print(hour)

date_and_time += timedelta(weeks=1)
print(date_and_time)
date_and_time += timedelta(days=10)
print(date_and_time)
date_and_time += timedelta(minutes=15)
print(date_and_time)
date_and_time += timedelta(hours=1)
print(date_and_time)
date_and_time += timedelta(seconds=10)
print(date_and_time)

idade = data_atual - data_nascimento
print(idade)