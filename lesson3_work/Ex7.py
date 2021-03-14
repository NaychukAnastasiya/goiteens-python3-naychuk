cars_senior = ["AudiR8Etron","MercedesBenzGle400","TeslaS"]
cars_junior = ["LadaKalyna","Zaporozhets"]
if len(cars_senior) > len(cars_junior):
    print("Senior developer Oleksij has got more cars than junior developer Oleh")
elif len(cars_senior) < len(cars_junior):
    print("Senior developer Oleksij has got less cars than junior developer Oleh") 
else:
    print ("Both developers have got the same amount of cars")       
