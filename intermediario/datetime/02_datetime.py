import datetime
import pytz

my_datetime = datetime.datetime(2023, 7, 19, 13, 45)
print(my_datetime)

datetime_add_one_week = my_datetime + datetime.timedelta(weeks=1)
print(datetime_add_one_week)
print(my_datetime + datetime.timedelta(days=5))
print(my_datetime - datetime.timedelta(weeks=2))

# trabalhando com data
data_atual = datetime.datetime.now()
print(data_atual)
# formatando a data e hora
print(data_atual.strftime("%d/%m/%Y %H:%M"))
# convertendo string para datetime
date_string = "28/09/2024 18:41"
nova_data = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(nova_data)
# trabalhando com timezone
timezone = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(timezone)

# obs.: devemos sempre priorizar trabalhar com a hora em uctnow() para então implementar o fuso
date_and_time = datetime.datetime.utcnow()
print(date_and_time)