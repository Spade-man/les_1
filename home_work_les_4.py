from random import choices

'''изначально решил задачу 2 как задачу 3 (я про z.count(i): i for i in z)
посмотрел как люди решают и узнал про функцию get() и код ускорился в 4-6 раз
оставил первоначальную конструкцию в задаче 3 - что бы неповадно было.'''
# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N
# cлучайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20,
# N = 100, рекомендуется использовать функцию random);
def F(names, N):
    return choices(names, k=N)


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
def most_common_name(z):
    v = {}
    for i in z:
        v[i] = v.get(i, 0) +1
    v = list(v.items())
    v.sort(key=lambda x: x[1], reverse=True)
    return (v[0][0])


# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def rarest_letter(z):
    letters = ''
    for i in z:
        letters += i[0]
    letters_count = sorted({letters.count(i): i for i in letters}.items())
    return (letters_count[0][1])


source = F(['уАбрам', 'бваз', 'Аввакум', 'бвгуст', 'Августин', 'фАвдей', 'Авраам', 'Автандил',
                      'Акгап', 'Агафон', 'бггей', 'Адам', 'фадис', 'фАдольф', 'Адриан'], 10000)
print(source)
print(most_common_name(source))
print(rarest_letter(source))


# # PRO:
# 4.  В файле с логами найти дату самого позднего лога (по метке времени):
# https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
dates = []
with open('\\log', 'r') as f:
    for i in f:
        dates.append(i[:23])
f.close()
print(max(dates))
"""Марат напишите, пожалуйста, код - как работать с этим файлом через URL

import request
with open(requests.get('https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8').text as f:...
"""




