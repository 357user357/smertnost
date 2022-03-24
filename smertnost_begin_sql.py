
import smertnost_puti
import smertnost_variables
if smertnost_puti.poliklinika:
  from Poliklinika import check_polik_death

"""Раздел работы с базой данных"""
import sqlite3 as sql  # для сортировки, фильтрации и изменению информации

if not smertnost_puti.poliklinika:
  temp_sql_db = \
    smertnost_puti.path_death_all_years + \
    "death.db"
else:
  #print("ooooooooooooook")
  temp_sql_db = \
    smertnost_puti.path_death_all_years + \
    "death_poliklinika.db"  

# создаем временный файл для хранения информации из журнала смертности
conn = sql.connect(temp_sql_db)


# создаем так называемый "указатель" который будет обрабатывать запросы к базе данных
cur2 = conn.cursor()
# очищаем временную таблицу от ранее созданных временных сведений
cur2.execute("DROP TABLE IF EXISTS death")
cur2.execute("DROP TABLE IF EXISTS death_prev")
cur2.execute("DROP TABLE IF EXISTS death_svod")
cur2.execute("DROP TABLE IF EXISTS death_svod_percent")
cur2.execute("DROP TABLE IF EXISTS death_pokazateli")

#if not smertnost_puti.poliklinika:

# сохраняем во временный файл выгруженную информацию из эксель файлов за оба года для
# дальнейшей обработки
if not smertnost_puti.poliklinika:
  smertnost_puti.death_df.to_sql('death', conn, if_exists='replace')
  smertnost_puti.death_df_prev.to_sql('death_prev', conn, if_exists='replace')

#else:
#  check_polik_death.death_df_prev_poliklinika


### создание новой таблицы
CREATE_TABLE_death_svod = "CREATE TABLE death_svod ('Показатель' text, "

for month in smertnost_puti.months:
    CREATE_TABLE_death_svod += month
    if month != "Декабрь":
        CREATE_TABLE_death_svod += " text, "
    else:
        CREATE_TABLE_death_svod += " text"

CREATE_TABLE_death_svod += ")"
### завершения создания новой таблицы

cur2.execute(CREATE_TABLE_death_svod)



CREATE_TABLE_death_pokazateli = smertnost_variables.CREATE + ' ' + smertnost_variables.TABLE + ' ' +    \
    smertnost_variables.table_death_pokazateli + ' ' +      \
    "(" +     \
    "'" + smertnost_variables.column_name_month + "' text, " +    \
    "'" + smertnost_variables.column_name_pokazatel + "' text, " +   \
    "'" + smertnost_variables.title_death_all_cause_1000_human_dvoetotsie_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_all_cause_1000_human_dvoetotsie_year_prev + "' text, " +     \
    "'" + smertnost_variables.title_death_trud_100_000_human_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_trud_100_000_human_year_prev + "' text, " +     \
    "'" + smertnost_variables.title_death_BSK_100_000_human_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_BSK_100_000_human_year_prev + "' text, " +     \
    "'" + smertnost_variables.title_death_Onco_100_000_human_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_Onco_100_000_human_year_prev + "' text, " +     \
    "'" + smertnost_variables.title_death_DTP_100_000_human_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_DTP_100_000_human_year_prev + "' text, " +     \
    "'" + smertnost_variables.title_death_Tuber_100_000_human_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_Tuber_100_000_human_year_prev + "' text, " +     \
    "'" + smertnost_variables.title_death_Child_year_cur + "' text, " +     \
    "'" + smertnost_variables.title_death_Child_year_prev + "' text " +     \
     ")"


cur2.execute(CREATE_TABLE_death_pokazateli)
# pragma table_info('death_pokazateli');
# SELECT * FROM "death_pokazateli"


"""Завершения раздела работы с базой данных"""


# для начала создаю временную таблицу которая будет содержать строки по процентам:
### создание новой таблицы
CREATE_TABLE_death_svod_percent = "CREATE TABLE death_svod_percent (Old_id INT NOT NULL, New_id INT NULL, 'Показатель' text, "

for month in smertnost_puti.months:
    CREATE_TABLE_death_svod_percent += month
    if month != "Декабрь":
        CREATE_TABLE_death_svod_percent += " FLOAT(3,1), "
    else:
        CREATE_TABLE_death_svod_percent += " FLOAT(3,1) "

CREATE_TABLE_death_svod_percent += " )"
### завершения создания новой таблицы

#print(CREATE_TABLE_death_svod_percent)

cur2.execute(CREATE_TABLE_death_svod_percent)
"""Завершения раздела работы с базой данных"""