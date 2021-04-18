# y = f(X)
# y = 2*x -10 # x>0
# y = 0# x=0
# y = 2 * abs(x) -1 # x<0

print("Введіть число")
x = float(input())
y = 0
if x > 0:
    y = 2*x -10    
elif x == 0:
    y = 0
else: #x<0
    y = 2 * abs(x) -1

print ("y: ",y)

