
# 2. Знайти на Wikipedia інформацію про те, коли були створені обидві ігри.
#  Роки їх створення записати в дві змінні. За допомогою оператора if порівняти яка гра є старішою.
#   Вивести на консоль свої результати.

year_of_creation_Minecraft =2009
year_of_creation_Terraria =2011
if year_of_creation_Minecraft < year_of_creation_Terraria:
    print ("Minecraft is older than Terraria")
elif year_of_creation_Minecraft > year_of_creation_Terraria:
    print ("Terraria is older than Minecraft")
else: print ("The year of creation Minecraft and Terraria is the same")