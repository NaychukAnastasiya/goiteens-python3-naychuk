# Написати програму, яка буде рахувати, скільки пройшло хвилин 
# та секунд з початку доби до теперішнього моменту. 
# Наприклад якщо зараз 1 ночі, то пройшло 60 хв та 3600 секунд. 
# Програма повинна виводити час на даний момент, 
# кількість хвилин, які пройшли за добу та кількість секунд.
from datetime import datetime

now = datetime.now()
seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

minutes = seconds_since_midnight//60
seconds = seconds_since_midnight%60
print("Кількість хвилин, які пройшли за добу: ",minutes, " та кількість секунд, які пройшли за добу: ",seconds)