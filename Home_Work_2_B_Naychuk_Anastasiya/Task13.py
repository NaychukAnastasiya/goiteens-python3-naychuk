# Створити змінну n (  Де n - кількість елементів ) і пустий массив arr = [ ] .
#  Ввести з клавіатури числа і добавити  в массив число в  квадраті  .
#  В кінці надрукувати сам массив тобто print( arr ) . 
# 5 ** 2, pow(3, 2), 4 * 4

print("Enter number of elements in array")
n = int(input())

arr = [0 for x in range(n)]

for x in range(n):
    print("Enter element ",x+1,": ")
    arr[x] = pow(float(input()),2)

print(arr)    

# arr = [0 for x in range(n)]
# print("Enter element 1")
# arr[0] = float(input())

# print("Enter element 2")
# arr[1] = float(input())

# print("Enter element 3")
# arr[2] = float(input())

# print("Enter element 4")
# arr[3] = float(input())

# print("Enter element 5")
# arr[4] = float(input())


# arr = []
# print("Enter element 1")
# x1 = float(input())
# arr.append(x1)

# print("Enter element 2")
# x2 = float(input())
# arr.append(x2)

# print("Enter element 3")
# x3 = float(input())
# arr.append(x3)

# print("Enter element 4")
# x4 = float(input())
# arr.append(x4)

# print("Enter element 5")
# x5 = float(input())
# arr.append(x5)

# print(arr)

    

