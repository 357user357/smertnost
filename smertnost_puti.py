
# загрузки программ
# для работы с эксель таблицами
import pandas as pd
import sqlite3 as sql
import os

# указываем года с которыми работаем

year_prev = 2020

year_current = 2021


# население на предыдущий год
population_prev_year = "28297"

# население на текущий год
population_current_year = "27494"


# население на 2020 год
#population_prev_year = "28297"

# население на 2021 год
#population_prev_year = "27494"

# ориентир. население на 2022 год
#population_current_year = "25962"

poliklinika = 0

title_organisation = "ГБУ «Курганская больница №2»"

# путь к папке смертности
path_death_all_years = "/home/user/Documents/Внутренние отчеты/Периодические/Смертность/Смертность по МО/"

output = os.popen("pwd")

line = output.readline()

output.close()

path_death_all_years = line[:-1] + "/"

#print(path_death_all_years)


#quit()


all_deaths_name_excel = "Журнал регистрации смерти для программы.xls"

poliklinika_deaths_name_excel = "Журнал регистрации поликлинической смерти для программы.xlsx"








# переменные для источника (журнал смертности) за текущий год
if not poliklinika:
  # финальный путь к файлу за текущий год с которым работаем
  from_excel_death_current = \
    path_death_all_years + str(year_current) + "/" + \
    all_deaths_name_excel
else:
  # временная переменная для поликлинической обработки за текущий год
  for_poliklinika_from_excel_death_current = \
    path_death_all_years + str(year_current) + "/" + \
    all_deaths_name_excel
  
  # убираем неполиклинических умерших из файла "for_poliklinika_from_excel_death_current" и 
  # сохраняем их в файле "from_excel_death_current" для текущего года
    
  # финальный путь к файлу за текущий год с которым работаем после поликлинической обработки
  from_excel_death_current = \
    path_death_all_years + str(year_current) + "/" + \
    poliklinika_deaths_name_excel

# финальный путь к файлу за предыдущий год с которым работаем
if not poliklinika:
  from_excel_death_prev = \
    path_death_all_years + str(year_prev) + "/" + \
    all_deaths_name_excel
else:
  #print("11199999999999999")
  # временная переменная для поликлинической обработки за предыдущий год
  for_poliklinika_from_excel_death_prev = \
    path_death_all_years + str(year_prev) + "/" + \
    all_deaths_name_excel
  #print(for_poliklinika_from_excel_death_prev)
  
  from_excel_death_prev = \
    path_death_all_years + str(year_prev) + "/" + \
    poliklinika_deaths_name_excel
  #print(from_excel_death_prev)

if not poliklinika:
  result_excel_dist = \
    path_death_all_years + str(year_current) + "/"+\
    "Свод по смертности за " + str(year_prev) + " и " + str(year_current) + " года.xlsx"
else:
  result_excel_dist = \
    path_death_all_years + str(year_current) + "/"+\
    "Свод по поликлинической смертности за " + str(year_prev) + " и " + str(year_current) + " года.xlsx"

  # убираем неполиклинических умерших из файла "for_poliklinika_from_excel_death_current" и 
  # сохраняем их в файле "from_excel_death_current" для текущего года
  
  # финальный путь к файлу за предыдущий год с которым работаем после поликлинической обработки


if poliklinika:   
  
  temp_sql_db_polik = \
    path_death_all_years + \
    "death_poliklinika.db"

  # создаем временный файл для хранения информации из журнала смертности
  conn_polik = sql.connect(temp_sql_db_polik)


  # создаем так называемый "указатель" который будет обрабатывать запросы к базе данных
  cur2_polik = conn_polik.cursor()
  # очищаем временную таблицу от ранее созданных временных сведений
  cur2_polik.execute("DROP TABLE IF EXISTS death_for_polik")
  cur2_polik.execute("DROP TABLE IF EXISTS death_prev_for_polik")
  
  
  # загружаем из эксель файлов имеющуюся информацию за оба года
  death_df_for_polik = pd.read_excel(for_poliklinika_from_excel_death_current)
  death_df_prev_for_polik = pd.read_excel(for_poliklinika_from_excel_death_prev)
  
  # сохраняем во временный файл выгруженную информацию из эксель файлов за оба года для
  # дальнейшей обработки
  death_df_for_polik.to_sql('death_for_polik', conn_polik, if_exists='replace')
  death_df_prev_for_polik.to_sql('death_prev_for_polik', conn_polik, if_exists='replace')
  
  conn_polik.commit()


  # пока что не создали уже отфильстрованную поликлиническую смертность и поэтому
  # ставим временную заглушку (при отсутствии созданного поликлинического экселя - возвращаемся
  # к переменной, которая создавалась без поликлинической смертности)
  ###########################################################################################################
  
  #from_excel_death_current = for_poliklinika_from_excel_death_current
  #from_excel_death_prev = for_poliklinika_from_excel_death_prev
  
  #print("for polik: from_excel_death_current= " + from_excel_death_current)
  ###########################################################################################################

#print("from_excel_death_current= " + from_excel_death_current)

if not poliklinika:
  death_df = pd.read_excel(from_excel_death_current)
  death_df_prev = pd.read_excel(from_excel_death_prev)


months = ("Январь" , "Февраль" , "Март" , "Апрель" , "Май" , "Июнь" , \
         "Июль" , "Август" , "Сентябрь" , "Октябрь" , "Ноябрь" , "Декабрь")
months_list = {}
months_short = {}
months_short_list = ("Янв." , "Фев." , "Мар." , "Апр." , "Май" , "Июнь" , \
         "Июль" , "Авг." , "Сен." , "Окт." , "Ноя." , "Дек.")
i = 0
for item_month in months_short_list:
    months_short[i] = item_month
    i += 1
#print(months_short)
# {0: 'Янв.', 1: 'Фев.', 2: 'Мар.', 3: 'Апр.', 4: 'Май', 5: 'Июнь', 6: 'Июль', 7: 'Авг.', 8: 'Сен.', 9: 'Окт.', 10: 'Ноя.', 11: 'Дек.'}

i = 0
item_month = ""
for item_month in months:
    months_list[i] = item_month
    i += 1

#print(months_list)
# {0: 'Январь', 1: 'Февраль', 2: 'Март', 3: 'Апрель', 4: 'Май', 5: 'Июнь', 6: 'Июль', 7: 'Август', 8: 'Сентябрь', 9: 'Октябрь', 10: 'Ноябрь', 11: 'Декабрь'}
#quit()

months_reverse_list = {v: k for k, v in months_list.items()}

#print(months_list)
#quit()

i=0
for month in months_short_list:
    months_short[i] = month
    i += 1

new_array_month = {}
i=1
for month in months:
    new_array_month[i] = month
    i += 1
i=0
current_month_for_percent_sort = ""

# подготавливаем шаблоны для заполнения ячеек с нулями и прочерками когда нет или 
# не должно быть сведений
i=12
tire_12, nuli_12 = "", ""
while i:
    i -= 1
    if i:
        tire_12 += " '-', "
        nuli_12 += " '0', "
    else:
        tire_12 += " '-' "
        nuli_12 += " '0' "



# теперь из файлов соответствующих годов с началом названия "for_poliklinika_" оставляем
# лишь поликлинические строки, содержащие в соответствующей графе "дом" или "другое место смерти дом",
# а потом из этого поликлинического файла будем осуществлять дальнейшую обработку таким образом, чтобы
# сохранить название переменной "path_death_all_years" для соответствующего года, тем самым 
# последующая обработка программой останется неизменной.

# пока что не удалось выделить поликлинический код в отдельный файл, так как происходит
# бесконечная рекурсия к путям файлов смертности - если я собираюсь делать включение кода во
# внутрь файла - то это надо делать в самом верху файла.

#if poliklinika:
#  from Poliklinika import check_polik_death




