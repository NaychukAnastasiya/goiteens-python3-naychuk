# В сім'ї Фландерсів кожного року святкують дні народження.

#  Цього року синам Тоду та Роду подарували
# скейтборд, футболку, рюкзак, цукерки (5 кг), мандарини. Створити множину/набір (set) з цих подарукнів. 
# Перевірити чи є скейтборд серед цих подарунків та вивести на консоль
#"Так, скейтборд є, якщо він є" та "Ні", якщо його немає
gifts = {"скейтборд", "футболку", "рюкзак", "цукерки", "мандарини"}
is_in_set = False
for x in gifts:
    if "скейтборд" in gifts:
        is_in_set = True
if is_in_set == True :
    print("Так, скейтборд є")
else:
    print("Ні, скейтборда немає")