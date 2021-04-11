# Перевірити чи сьогодні "Sunday" з допомогою datetime. Якщо так, то вивести 
# "Привіт субота", якщо ні то "НІІІІІІІІІІІІ, хочу суботу"
import datetime

x = datetime.datetime.now()
if x.strftime("%A")=="Saturday":
    print("Привіт субота")
else:
    print("НІІІІІІІІІІІІ, хочу суботу")