# Перевірити чи в створеному словнику серед ключів є ім'я "Оптімус". 
# Якщо так то вивести на консоль "Оптімус Прайм прибув"

carsdict = {
  "Оптімус Прайм" : "Грузовик Peterbilt 379",
  "Бамблбі" : "Chevrolet Camaro",
  "Джаз" : "Porsche 935 Turbo"
}
if 'Оптімус' in carsdict.keys():
    print("Оптімус прибув")
elif 'Оптімус Прайм' in carsdict.keys():
    print("Оптімус Прайм прибув")