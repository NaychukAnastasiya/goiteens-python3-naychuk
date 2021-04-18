# Завдання 3: До програми з завдання номер 2 додати меню вибору арифметичної 
# дії та введення чисел з клавіатури
def functionCalculator(first_num,operator,second_num):
    if operator =='+':
         result =first_num+ second_num
    elif operator =='-':
         result =first_num- second_num
    elif operator =='/':
         result =first_num/second_num
    elif operator =='*':
         result =first_num*second_num
    print('first_num: ',first_num,'operator: ', operator,'second_num: ',second_num, 'result: ',result)

# викликаємо фукнцію, написавши її назву, та передавши в дужки числа
print("Введіть перше число")
val1 = float(input())

print("Введіть оператор")
oper = str(input())

print("Введіть друге число")
val2 = float(input())

functionCalculator(val1,oper,val2)

