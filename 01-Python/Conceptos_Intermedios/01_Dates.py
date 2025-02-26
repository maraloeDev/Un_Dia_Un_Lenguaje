## Dates

from _datetime import datetime

now = datetime.now()

timestamp = now.timestamp()
print(timestamp)


def print_date(date):
    print(f"AÑO {date.year}")
    print(f"MES {date.month}")
    print(f"DIA {date.day}")
    print(f"HORA {date.hour}")
    print(f"MINUTOS {date.minute}")
    print(f"SEGUNDOS {date.second}")
    print(date.timestamp())

print_date(now)

year_2026= datetime(2026,1,1)
print(year_2026)

from datetime import time

current_time = time(12,12,12)

print("HORA-MINUTO-SEGUNDO")
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2025,2,12)
current_date_actually = date.today()
print("DIA-MES-AÑO")
print(current_date.day)
print(current_date.month)
print(current_date.year)

print(f"Fecha actual {current_date_actually}")

## OPERACIONES CON FECHAS

current_date = date(current_date.year,current_date.month, current_date.day)

print(current_date.month)

diff = year_2026 - now
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)
print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)