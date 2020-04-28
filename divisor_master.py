#1 Простое ли число?
def is_simple(n):
    for i in range(1,n):
        if n % i == 0 and i != 1:
            return False
    return True


#2 Список всех делителей числа
def all_dividers(n):
    z = []
    for i in range(1, n+1):
        if n % i == 0:
            z.append(i)
    return z


#3 Самый большой простой делитель
def biggest_simp_divder(n):
    lst_smpl_dvdrs = []
    for i in all_dividers(n):
        if is_simple(i):
            lst_smpl_dvdrs.append(i)
    return (max(lst_smpl_dvdrs))


#4 Функция выводит каноническое разложение числа
def canon(n):
    ans = []
    i = 2
    while n > 1:
        if is_simple(i) and n % i == 0:
            ans.append(i)
            n //= i
        else: i += 1
    return ans


#5 Самый большой делитель не равный числу
def biggest_divder(n):
    return ((all_dividers(n)[-2] if n != 1 else 1))


print(biggest_divder(66432))
print(is_simple(8))
print(all_dividers(8))
print(biggest_simp_divder(8))
print(canon(8))

