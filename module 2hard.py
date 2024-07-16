def password(n):
    kod_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                kod_ += str(i) + str(j)
    return kod_

print('Введите число от 3 до 20: ')
print(password(int(input())))
