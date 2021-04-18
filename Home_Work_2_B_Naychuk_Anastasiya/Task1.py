# Яке з 3 чисел найбільш наближене до середнього
print("Введіть перше число")
var1 = float(input())
print("Введіть друге число")
var2 = float(input())
print("Введіть третє число")
var3 = float(input())
# Avg = (var1+var2+var3)/3 # Варіант розв'язку з порівнянням чисел із середнім арифметичним:

if ((var1 > var2) and (var1 < var3)) or (var1 < var2) and (var1 > var3):
    print ("Найбільш наближеним числом до середнього є ",var1)
elif ((var2 > var1) and (var2 < var3)) or ((var2 < var1) and (var12 > var3)):
    print ("Найбільш наближеним числом до середнього є ",var2)
else:
    print ("Найбільш наближеним числом до середнього є ",var3)


# # Варіант розв'язку з порівнянням чисел із середнім арифметичним:
# if (abs(var1-Avg))>(abs(var2-Avg)):
#     if (abs(var2-Avg))>(abs(var3-Avg)):
#         print ("Найбільш наближеним числом до середнього є ",var3)
#     else: #(abs(var2-Avg))<(abs(var3-Avg))
#         print ("Найбільш наближеним числом до середнього є ",var2)
# else: #(abs(var1-Avg))<(abs(var2-Avg))
#     if (abs(var1-Avg))>(abs(var3-Avg)):
#         print ("Найбільш наближеним числом до середнього є ",var3)
#     else: #(abs(var1-Avg))<(abs(var3-Avg))
#         print ("Найбільш наближеним числом до середнього є ",var1)