# 1. Користувач хоче вибрати гру. Він вводить з клавітуари текст "2D" або "3D". 
# Якщо користувач ввів "2D" вивести на консоль "Terraria", якщо "3D" - "Minecraft".

print("To choose game you have to enter 2D or 3D: ")
game_chosen = input()
if game_chosen == "2D":
    print("Terraria")
elif game_chosen == "3D":
    print("Minecraft")
else:
    print("Start again and choose 2D or 3D: ")