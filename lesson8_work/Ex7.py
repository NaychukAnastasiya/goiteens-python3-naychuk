# Написати функцію, яка перевіряє чи в списку є ім'я "Євген"
def is_in_list(l, e):
    if e in l:
        return True
    else:
        return False
print(is_in_list(['Ярослав', 'Богдан', 'Катя', 'Євген'], "Євгенпше"))
