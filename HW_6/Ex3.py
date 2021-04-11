# Кожен трансформер має свою вагу, запишемо її у словник

# transformersWeight = { "Оптімус": 5000, "Бамблбі": 2500, "Джаз": 3000 }
# Яка вага всіх трансформерів у словнику?

transformersWeight = { "Оптімус": 5000, "Бамблбі": 2500, "Джаз": 3000 }
total_weight = 0
for value in transformersWeight.values():
    total_weight+=value
print("Total weight: ",total_weight)
