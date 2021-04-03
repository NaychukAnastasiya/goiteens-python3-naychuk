total_salary = 0
group_names = ["Гітарист", "Барабанщик", "Піаніст", "Вокаліст"]
group_salaries = [100, 100, 100, 100]
for i in range(len(group_names)):
    total_salary = total_salary + group_salaries[i]
print('total_salary = ',total_salary)