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
functionCalculator(2,'+',3)
functionCalculator(6,'-',5)
functionCalculator(6,'/',3)
functionCalculator(6,'*',3)