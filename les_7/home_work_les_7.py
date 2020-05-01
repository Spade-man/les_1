import datetime
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm
import csv
import json

t_start = datetime.datetime.now()
def age_years(date_brth):
    z = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
     1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044,
     2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2100, 2104, 2108, 2112, 2116]
    scores_of_366 = 0
    date_b = datetime.datetime.strptime(date_brth.replace('/', ''), '%Y%m%d').date()
    b_year = date_b.year
    date_now = datetime.datetime.today().date()
    d_now_year = date_now.year
    while b_year <= d_now_year:
        if b_year in z:
            scores_of_366 += 1
        b_year += 1
    return ((date_now - date_b).days - scores_of_366) // 365

with open('hw_data.txt', 'r') as f:
    z = f.readlines()
    surname = z[0].strip()
    name = z[1].strip()
    date_brth = z[2].strip()
    place_brth =z[3].strip()
    sex = z[4].strip()
age = age_years(date_brth)

def get_context(surname, name, date_brth, age,  place_brth, sex):
    return {'surname': surname,
            'name': name,
            'date_brth': date_brth,
            'place_brth': place_brth,
            'sex': sex,
            'age': age}

def from_template(surname, name, date_brth, age, place_brth, sex, pic, template):
    template = DocxTemplate(template)
    context = get_context(surname, name, date_brth, age, place_brth, sex)

    img_size = Cm(12)
    picture = InlineImage(template, pic, img_size)
    context['pic'] = picture
    template.render(context)
    template.save(name + ' ' + surname + str(datetime.datetime.today().date()) + 'hw_template.docx')

def generate_report(surname, name, date_brth, age, place_brth, sex):
    template = 'hw_template.docx'
    pic = 'pic821.png'
    doc = from_template(surname, name, date_brth, age,  place_brth, sex, pic, template)

generate_report(surname, name, date_brth, age,  place_brth, sex)
t_finish = datetime.datetime.now()
t_func = t_finish - t_start
print('Время создания отчёта: ', t_func)


t_start = datetime.datetime.now()
dict_csv = [get_context(surname, name, date_brth, age,  place_brth, sex)]
fields = ['surname', 'name', 'date_brth', 'age',  'place_brth', 'sex']
with open('hw_data.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter='\\', fieldnames=fields)
    writer.writeheader()
    for i in range(len(dict_csv)):
        writer.writerow((dict_csv[i]))
t_finish = datetime.datetime.now()
t_func = t_finish - t_start
with open('hw_data.csv', 'a') as f:
    f.writelines('Time spent on report generation: ')
    f.writelines(str(t_func))

t_start = datetime.datetime.now()
dict_json = json.dumps(get_context(surname, name, date_brth, age,  place_brth, sex))
with open('hw_data.json', 'w') as f:
    json.dump(dict_json, f)
    f.write('\n')
t_finish = datetime.datetime.now()
t_func = t_finish - t_start
with open('hw_data.json', 'a') as f:
    f.writelines('Time spent on report generation: ')
    f.writelines(str(t_func))
