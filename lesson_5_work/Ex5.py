donuts = ["ягідні","вишневі","шоколадні","карамельні"]
is_present= False
for i in donuts:
    if i=="вишневі":
        is_present= True
        break
   
if  is_present== True:
    print("Є")
else:
    print("Немає")            
