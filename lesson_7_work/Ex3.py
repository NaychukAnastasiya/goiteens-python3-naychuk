# Нед Фландерс та Гомер Сімпсон вже довгий час є сусідами.
#  На свої дні народження Нед отримав "Інструменти для лівшів", "Зелений чай", "Шоколад", 
#  а Гомер на своє "Піцу", "Премію на роботі", "Касети з всіма випусками Клоуна Красті", "Шоколад". 
# Записати їхні подарунки в 2 set та вивести на консоль подарунок,
#  який був однаковий в обох персонажів

gifts_Ned = {"Інструменти для лівшів", "Зелений чай", "Шоколад"}
gifts_Homer = {"Піцу", "Премію на роботі", "Касети з всіма випусками Клоуна Красті", "Шоколад"}
the_same_gift = gifts_Ned.intersection(gifts_Homer)

print("The same gift/s is/ are: ",the_same_gift)