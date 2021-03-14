# 1. Користувач вводить з клавіатури кількість років президентства. 
# Порахувати скільки термінів цей президент управляв США.
#  Вивести на консоль повідомлення "Президент не може бути на посту президента більше 2 термінів", 
# якщо в результаті вийшло більше 2 термінів.

president_termin_max = 4 #years
print("Enter president termin in years: ")
president_termin = int(input())
if president_termin <= president_termin_max*2:
    print("President term0in ", president_termin, " years is valid")
else: print("President can't hold a position of a president if the total termin is more then 2 termins (8 years)")