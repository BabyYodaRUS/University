def get_password (number):
    password = ''
    for i in range (1,number):
        for j in range (2,number):
            if i >= j:
                continue
            if number % (i+j) == 0:
                password = password + str(i) + str(j)
    return password

n = int(input("Введите целое число от 3 до 20:"))
while 20 < n or n < 3:
    print("Число меньше 3 или больше 20")
    n = int(input("Введите целое число от 3 до 20:"))
else:
    print("Ваш пароль:",get_password(n))
