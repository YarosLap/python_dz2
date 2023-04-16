n = int(input('Введите количество элементов массива:'))
a = input('Введите элементы массива: ').split()
x = int(input('Введите количество элементов на которое надо сдвинуть: '))
for i in range(x):
    temp = a[i]
    a[i] = a[n - x + i]
    a[n - x + i] = temp
for i in range(x, n - 1):
    for j in range(x, n - i - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
print(*a)