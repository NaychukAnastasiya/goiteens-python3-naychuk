# Підрахувати, скільки разів серед символів заданого рядка зустрічається буква "а".
#  Рядок : "It is a long established fact that a reader."

#  Потрібно створити змінну count = 0 - де буде зберігатися кількість букви "а" .
#   Використати цикл for і  умовний оператор if .
#   Надрукувати через print("Кількість букв а : ", count)

string1 = "It is a long established fact that a reader."
count = 0
for i in range(len(string1)):
    if string1[i] =='a':
        count = count +1
print("Number of letter a in 'It is a long established fact that a reader.' is: ", count)        
