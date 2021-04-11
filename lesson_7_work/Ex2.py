# В батька сім'ї Неда Фландерса є заощадження на подарунки, але оскільки 
# він любить зберігати гроші в банках, то він має 4 банки з грошима. 
# 1 банка 100 доларів, 2 банка, 200 доларів, 3 банка 150 доларів, 4 банка 300 доларів. 
# Створити set з грошима, які є в банках Неда. Також в дружини Неда Мод є банка з 200 доларами. 
# Додати її в множину грошей Неда.
#  Порахувати суму грошей, яка вийшла в set

money_bottles_Ned = {"100", "200", "150", "300"}
money_bottles_Mod = {"201"}# 200 would not be added due to no duplicates in set
money_bottles_Ned.update(money_bottles_Mod)
money_bottles_family= money_bottles_Ned.union(money_bottles_Mod)
print(money_bottles_family)
print(money_bottles_Ned)

