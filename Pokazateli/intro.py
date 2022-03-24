
import smertnost_puti
import smertnost_begin_sql
import smertnost_variables

import re


import datetime

from datetime import timedelta

import time


INSERT_to_death_pokazateli = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                           smertnost_variables.table_death_pokazateli + ' ' + smertnost_variables.VALUES + ' ' +  \
                           '(' +  " " + \
                           '"' + smertnost_variables.period_month_name + '"' + " " + "," + " " +  \
                           '"' + smertnost_variables.pokazatel_short + '"' + " " + "," 



insert_title = INSERT_to_death_pokazateli

for loop_rubrika in range(1,15):
    #print( str(loop_rubrika) )
    #print( str(loop_rubrika%2) )
    if (loop_rubrika%2) == 1: 
        insert_title += '"'
        insert_title += str(smertnost_puti.year_current)
        insert_title += '"'
    else:
        insert_title += '"'
        insert_title += str(smertnost_puti.year_prev)
        insert_title += '"'        

    if loop_rubrika != 14:
        insert_title += " , "

insert_title += " " + ");"



for index_month in range(0,12):
    
    INSERT_to_death_pokazateli = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                           smertnost_variables.table_death_pokazateli + ' ' + smertnost_variables.VALUES + ' ' +  \
                           '(' + " " +  \
                           '"' + smertnost_puti.months_short[index_month] + '"' + " " + "," + " " +   \
                           '"' + smertnost_variables.pokazatel_short + '"' + " " + "," 
    insert_title = INSERT_to_death_pokazateli
    for loop_rubrika in range(1,15):
        insert_title += '"' 
        insert_title += "-"
        insert_title += '"'
        if loop_rubrika != 14:
            insert_title += " , "
    insert_title += " " + ")"
    smertnost_begin_sql.cur2.execute(insert_title)


    INSERT_to_death_pokazateli = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                           smertnost_variables.table_death_pokazateli + ' ' + smertnost_variables.VALUES + ' ' +  \
                           '(' +  \
                           '"' + smertnost_puti.months_short[index_month] + '"' + "," +   \
                           '"' + smertnost_variables.abs_human + '"' + "," 
    insert_title2 = INSERT_to_death_pokazateli
    for loop_rubrika in range(1,15):
        insert_title2 += '"' 
        insert_title2 += "-"
        insert_title2 += '"'
        if loop_rubrika != 14:
            insert_title2 += " , "
    insert_title2 += " " + ")"
    #print(insert_title2)
    smertnost_begin_sql.cur2.execute(insert_title2)
    
    
    smertnost_begin_sql.conn.commit()

## Завершения подготовки шаблона по абсолют. и относит. показ-лям
#######



#########################
# Расчет относит. показателя по общей смертности на тысячу населения за текущий год 


#print(insert_title)
#smertnost_begin_sql.cur2.execute(insert_title)
#smertnost_begin_sql.conn.commit()
#sql_query = 'SELECT Январь from "death_svod" where Показатель = "всего ' + smertnost_puti.year_current + ' г."'

number_index_month = 0

current_row = 0

smertnost_variables.tekushee_kolichestvo_vsego = 0



for smertnost_variables.outer_month in smertnost_puti.months:
    
    # по строкам "всего" текущего года
    
    # SELECT "Январь" FROM death_svod WHERE "Показатель" = "всего 2022 г."
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + '"' + smertnost_variables.outer_month + '"' + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_svod + ' ' + \
                                                smertnost_variables.WHERE + \
                                                ' ' + '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                "=" + \
                                                " " + '"' + smertnost_variables.total + " " + \
                                                                str(smertnost_puti.year_current) + " " + \
                                                                smertnost_variables.year_point + \
                                                      '"' ):
        # учитываем по нарастающей
        if row[0] == "-":
            current_row = 0
        else:
            current_row = int(row[0])
        smertnost_variables.tekushee_kolichestvo_vsego = current_row
        # print(smertnost_variables.tekushee_kolichestvo_vsego)
        
        
        # обновляем подстроки если поступили сведения из ЗАГС и
        # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
        if current_row:
            smertnost_variables.for_update_only_current_month = int(smertnost_variables.tekushee_kolichestvo_vsego)
            #print(smertnost_variables.tekushee_kolichestvo_vsego)
            #print(int(smertnost_puti.population_current_year))
            #print(smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_current_year) )
            #print( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_current_year) ) * 1000)
            smertnost_variables.calc_1000_human = round( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_current_year) ) * 1000, 1 )
            
            temp_for_sql = smertnost_variables.calc_1000_human
        else:
            # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
            temp_for_sql = 0
            # до конца года будут нули по оставшимся месяцам текущего года
            smertnost_variables.for_update_only_current_month = 0
        


        ######################################################################
        # UPDATE death_pokazateli SET "Смертность от всех причин, на 1000 населения: 2022" = "0" WHERE "Наименование: месяц" = "Янв."
        
        if current_row:
            # внесение сведений за текущий год в свод "умерло всего"
            smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_all_cause_1000_human_dvoetotsie_year_cur + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(temp_for_sql) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.pokazatel_short + '"' + " " + \
                                     ")" )
        
            # внесение сведений за текущий год в свод "умерло всего"
            smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_all_cause_1000_human_dvoetotsie_year_cur + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(smertnost_variables.tekushee_kolichestvo_vsego) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.abs_human + '"' + " " + \
                                     ")" )
        current_row = 0
        
    number_index_month += 1


smertnost_begin_sql.conn.commit()




#########################
# Расчет относит. показателя по общей смертности на тысячу населения за предыдущий год 


number_index_month = 0

current_row = 0

smertnost_variables.tekushee_kolichestvo_vsego = 0


for smertnost_variables.outer_month in smertnost_puti.months:
    
    # по строкам "всего" текущего года
    
    # SELECT "Январь" FROM death_svod WHERE "Показатель" = "всего 2021 г."
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + '"' + smertnost_variables.outer_month + '"' + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_svod + ' ' + \
                                                smertnost_variables.WHERE + \
                                                ' ' + '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                "=" + \
                                                " " + '"' + smertnost_variables.total + " " + \
                                                                str(smertnost_puti.year_prev) + " " + \
                                                                smertnost_variables.year_point + \
                                                      '"' ):
        #print(row[0])        
        current_row = int(row[0])
        smertnost_variables.tekushee_kolichestvo_vsego = current_row
        # print(smertnost_variables.tekushee_kolichestvo_vsego)
        
        
        # обновляем подстроки если поступили сведения из ЗАГС и
        # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
        if current_row:
            smertnost_variables.for_update_only_current_month = int(smertnost_variables.tekushee_kolichestvo_vsego)
            
            smertnost_variables.calc_1000_human = round( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_prev_year) ) * 1000, 1 )
            
            temp_for_sql = smertnost_variables.calc_1000_human
        else:
            # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
            temp_for_sql = 0
            # до конца года будут нули по оставшимся месяцам текущего года
            smertnost_variables.for_update_only_current_month = 0
        
        current_row = 0
        
        # UPDATE death_pokazateli SET "Смертность от всех причин, на 1000 населения: 2021" = "0" WHERE "Наименование: месяц" = "Янв."
        
        # внесение сведений за предыдущий год в свод "умерло всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_all_cause_1000_human_dvoetotsie_year_prev + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(temp_for_sql) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + " " + \
                                     '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + " " + \
                                     '"' + smertnost_variables.pokazatel_short + '"' + " " + \
                                     ")" )
        
        #print(str(smertnost_variables.tekushee_kolichestvo_vsego))
        # внесение сведений за предыдущий год в свод "умерло всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_all_cause_1000_human_dvoetotsie_year_prev + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(smertnost_variables.tekushee_kolichestvo_vsego) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.abs_human + '"' + " " + \
                                     ")" )
    
    number_index_month += 1




smertnost_begin_sql.conn.commit()





number_index_month = 0
current_row = 0
smertnost_variables.tekushee_kolichestvo_vsego = 0



#################################################
# Формирование относительного показателя по трудоспособному населению за текущий год

number_index_month = 0

count_man_trud = 0
prev_count_man_trud = -1

count_woman_trud = 0
prev_count_woman_trud = -1

count_all_trud = 0



for smertnost_variables.outer_month in smertnost_puti.months:
    
    # SELECT "Дата рождения" , "Дата смерти" , "Пол" FROM death WHERE "Период по ЗАГС" = "Январь"
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + ' ' + \
                                                '"' + smertnost_variables.column_date_birth + '"' + ' ' + "," + ' '     + \
                                                '"' + smertnost_variables.column_date_death + '"' + ' ' + "," + ' '     + \
                                                '"' + smertnost_variables.column_gender + '"' + ' '     + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' '     + \
                                                smertnost_variables.WHERE + ' '     + \
                                                '"' + smertnost_variables.column_period_po_zags + '"' + ' '     + \
                                                '=' + ' '       + \
                                                '"' + smertnost_variables.outer_month + '"'):        
        #print(row)
        # сначала обрабатываем дату рождения
        # 1981-10-14 00:00:00
        
        p = re.compile(r'(\d+)-(\d+)-(\d+)\s.*')
        m = p.findall(row[0])
        # печать буквенного начала ячейки
        person_year_birth = int(m[0][0])
        person_month_birth = int(m[0][1])
        person_day_birth = int(m[0][2])
        #print('year: ' + person_year_birth)
        #print('month: ' + person_month_birth)
        #print('day: ' + person_day_birth)
        #quit()
        
        
        person_birth_datetime = datetime.datetime(person_year_birth, person_month_birth, person_day_birth)
        
        #print(person_birth_datetime)
        
        # далее обрабатываем дату смерти
        p = re.compile(r'(\d+)-(\d+)-(\d+)\s.*')
        m = p.findall(row[1])
        # печать буквенного начала ячейки
        person_year_death = int(m[0][0])
        person_month_death = int(m[0][1])
        person_day_death = int(m[0][2])
        #print('year: ' + str(person_year_death))
        #print('month: ' + str(person_month_death))
        #print('day: ' + str(person_day_death))        
        #print(row[1])
        #quit()
        
        person_death_datetime = datetime.datetime(person_year_death, person_month_death, person_day_death)
        
        #print("---")
        #print(person_death_datetime)
        #quit()     
        #unix_raznost_for_death_date = (person_death_datetime - smertnost_variables.century_before_unix_begin_datetime).total_seconds()        
        #print("unix_raznost_for_death_date = " + str(unix_raznost_for_death_date))        
        #quit()
        
        check_trud_vozrast = 0
        
        if row[2]=='м':
            man_edge_trud_datetime = datetime.datetime(person_year_birth + smertnost_variables.edge_of_man_age, person_month_birth, person_day_birth)
            #print("man_edge_trud_datetime = " + str(man_edge_trud_datetime))
            
            check_trud_man_vozrast = (person_death_datetime - man_edge_trud_datetime).total_seconds()
            if check_trud_man_vozrast<0:
                check_trud_vozrast = 1
            #print("check_trud_man_vozrast = " + str(check_trud_man_vozrast))
        elif row[2]=='ж':
            woman_edge_trud_datetime = datetime.datetime(person_year_birth + smertnost_variables.edge_of_woman_age, person_month_birth, person_day_birth)
            #print("woman_edge_trud_datetime = " + str(woman_edge_trud_datetime))
            
            check_trud_woman_vozrast = (person_death_datetime - woman_edge_trud_datetime).total_seconds()
            if check_trud_woman_vozrast<0:
                check_trud_vozrast = 1
        
        #(person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds()        
        #unix_raznost_for_birth_date = (person_birth_datetime - smertnost_variables.century_before_unix_begin_datetime).total_seconds()                
        #print("unix_raznost_for_birth_date = " + str(unix_raznost_for_birth_date))
        ##### (person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds()        
        
        if row[2]=='м' and check_trud_vozrast:
            #print("man: ")
            #print(person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds())
            ######### if (person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds()>0:
            smertnost_variables.lists_man_birth_death.append( (person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds() )
        
        
        if row[2]=='ж' and check_trud_vozrast:
            #print("woman: ")
            #print(person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds())
            ######### if (person_birth_datetime-smertnost_variables.datetime_for_woman_edge_trud).total_seconds()>0:
            smertnost_variables.lists_woman_birth_death.append( (person_birth_datetime-smertnost_variables.datetime_for_woman_edge_trud).total_seconds() )
    
    # Завершения цикла по выборке дат рождений, смерти и пола 
    # (и дополнения списка трудоспособных в случае наличия) за текущий месяц
    #print("begin: count_all_trud = " + str(count_all_trud))
    if prev_count_man_trud<0:
        prev_count_man_trud = 0
    elif prev_count_man_trud==0:
        prev_count_man_trud = len(smertnost_variables.lists_man_birth_death)
        #print(prev_count_man_trud)
    if prev_count_woman_trud<0:
        prev_count_woman_trud = 0
    elif prev_count_woman_trud==0:
        prev_count_woman_trud = len(smertnost_variables.lists_woman_birth_death)
        #print(prev_count_woman_trud)
    
    count_man_trud = len(smertnost_variables.lists_man_birth_death)
    
    #print("count_man_trud = " + str(count_man_trud))
    
    count_woman_trud = len(smertnost_variables.lists_woman_birth_death)
    
    #print("count_woman_trud = " + str(count_woman_trud))
    
    count_all_trud = 0
    count_all_trud += len(smertnost_variables.lists_man_birth_death)
    count_all_trud += len(smertnost_variables.lists_woman_birth_death)
    
    #print("smertnost_puti.months_short[number_index_month] = " + smertnost_puti.months_short[number_index_month])        
    #print("count_all_trud = " + str(count_all_trud))
    
    smertnost_variables.count_all_trud = count_all_trud
    
    # учитываем по нарастающей
    if count_all_trud == 0:
        current_row = 0
    else:
        current_row = int(count_all_trud)
    smertnost_variables.tekushee_kolichestvo_vsego = current_row
    # print(smertnost_variables.tekushee_kolichestvo_vsego)
    
    
    # обновляем подстроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if current_row:
        smertnost_variables.for_update_only_current_month = int(smertnost_variables.tekushee_kolichestvo_vsego)
        #print(smertnost_variables.count_all_trud)
        #print(int(smertnost_puti.population_current_year))
        #print(smertnost_variables.count_all_trud / int(smertnost_puti.population_current_year) )
        #print( (smertnost_variables.count_all_trud / int(smertnost_puti.population_current_year) ) * 100000)
        smertnost_variables.calc_100000_trud_human = round( (smertnost_variables.count_all_trud / int(smertnost_puti.population_current_year) ) * 100000, 1 )
            
        temp_for_sql = smertnost_variables.calc_100000_trud_human
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        temp_for_sql = 0
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0
        
    current_row = 0        
    
    # UPDATE death_pokazateli SET "Смертность в трудоспособном возрасте, на 100000 населения: 2022" = "3.6" 
    # WHERE ( "Наименование: месяц" = "Янв." AND "Наименование: показатель" = "Пок-тель" )        
    # внесение сведений за текущий год в свод "умерло всего"
    
    if (count_man_trud != prev_count_man_trud) or (count_woman_trud != prev_count_woman_trud):
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.column_name_trud_dvoetotsie_year_cur + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(temp_for_sql) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.pokazatel_short + '"' + " " + \
                                     ")" )
    

    if (count_man_trud != prev_count_man_trud) or (count_woman_trud != prev_count_woman_trud):
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.column_name_trud_dvoetotsie_year_cur + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(smertnost_variables.count_all_trud) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.abs_human + '"' + " " + \
                                     ")" )    


    prev_count_man_trud = len(smertnost_variables.lists_man_birth_death)
    prev_count_woman_trud = len(smertnost_variables.lists_woman_birth_death)
    number_index_month += 1

smertnost_begin_sql.conn.commit()



"""
print("smertnost_variables.lists_man_birth_death")
print(len(smertnost_variables.lists_man_birth_death) )
print("smertnost_variables.lists_woman_birth_death")
print(len(smertnost_variables.lists_woman_birth_death) )
"""
#quit()
 
















#################################################
# Формирование относительного показателя по трудоспособному населению за предыдущий год

number_index_month = 0

count_man_trud = 0

count_woman_trud = 0

count_all_trud = 0

smertnost_variables.lists_man_birth_death = []

smertnost_variables.lists_woman_birth_death = []


for smertnost_variables.outer_month in smertnost_puti.months:
    
    
    # ?????? SELECT "Дата рождения" , "Дата смерти" , "Пол" FROM death_prev WHERE "Период по ЗАГС" = "Январь"
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + ' ' + \
                                                '"' + smertnost_variables.column_date_birth + '"' + ' ' + "," + ' '     + \
                                                '"' + smertnost_variables.column_date_death + '"' + ' ' + "," + ' '     + \
                                                '"' + smertnost_variables.column_gender + '"' + ' ' + "," + ' '     + \
                                                '"Фамилия"' + ' '     + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_prev + ' '     + \
                                                smertnost_variables.WHERE + ' '     + \
                                                '"' + smertnost_variables.column_period_po_zags + '"' + ' '     + \
                                                '=' + ' '       + \
                                                '"' + smertnost_variables.outer_month + '"'):        
        #print(row)
        # сначала обрабатываем дату рождения
        # 1981-10-14 00:00:00
        
        p = re.compile(r'(\d+)-(\d+)-(\d+)\s.*')
        m = p.findall(row[0])
        # печать буквенного начала ячейки
        person_year_birth = int(m[0][0])
        person_month_birth = int(m[0][1])
        person_day_birth = int(m[0][2])
        #print('year: ' + person_year_birth)
        #print('month: ' + person_month_birth)
        #print('day: ' + person_day_birth)
        #quit()
        
        person_birth_datetime = datetime.datetime(person_year_birth, person_month_birth, person_day_birth)
        
        #print(person_birth_datetime)
        
        # далее обрабатываем дату смерти
        p = re.compile(r'(\d+)-(\d+)-(\d+)\s.*')
        m = p.findall(row[1])
        # печать буквенного начала ячейки
        person_year_death = int(m[0][0])
        person_month_death = int(m[0][1])
        person_day_death = int(m[0][2])
        #print('year: ' + str(person_year_death))
        #print('month: ' + str(person_month_death))
        #print('day: ' + str(person_day_death))        
        #print(row[1])
        #quit()
        
        person_death_datetime = datetime.datetime(person_year_death, person_month_death, person_day_death)
        
        #print("---")
        #print(person_death_datetime)
        #quit()
        #unix_raznost_for_death_date = (person_death_datetime - smertnost_variables.century_before_unix_begin_datetime).total_seconds()        
        #print("unix_raznost_for_death_date = " + str(unix_raznost_for_death_date))        
        #quit()
        
        check_trud_vozrast = 0
        
        if row[2]=='м':
            man_edge_trud_datetime = datetime.datetime(person_year_birth + smertnost_variables.edge_of_man_age, person_month_birth, person_day_birth)
            #print("man_edge_trud_datetime = " + str(man_edge_trud_datetime))            
            check_trud_man_vozrast = (man_edge_trud_datetime - person_death_datetime).total_seconds()
            if check_trud_man_vozrast>0:
                check_trud_vozrast = 1
            #print("check_trud_man_vozrast = " + str(check_trud_man_vozrast))
        elif row[2]=='ж':
            woman_edge_trud_datetime = datetime.datetime(person_year_birth + smertnost_variables.edge_of_woman_age, person_month_birth, person_day_birth)
            #print("woman_edge_trud_datetime = " + str(woman_edge_trud_datetime))            
            check_trud_woman_vozrast = (woman_edge_trud_datetime - person_death_datetime).total_seconds()
            if check_trud_woman_vozrast>0:
                check_trud_vozrast = 1
        
        #(person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds()        
        #unix_raznost_for_birth_date = (person_birth_datetime - smertnost_variables.century_before_unix_begin_datetime).total_seconds()                
        #print("unix_raznost_for_birth_date = " + str(unix_raznost_for_birth_date))
        ##### (person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds()        
        
        if row[2]=='м' and check_trud_vozrast:
            #print(row)
            #print((person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds())
            ######### if (person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds()>0:
            smertnost_variables.lists_man_birth_death.append( (person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds() ) 
            # print("len(smertnost_variables.lists_man_birth_death) = " + str(len(smertnost_variables.lists_man_birth_death)) )   
        
        if row[2]=='ж' and check_trud_vozrast:
            #print(row)
            #print(person_birth_datetime-smertnost_variables.datetime_for_man_edge_trud).total_seconds())
            ######### if (person_birth_datetime-smertnost_variables.datetime_for_woman_edge_trud).total_seconds()>0:
            smertnost_variables.lists_woman_birth_death.append( (person_birth_datetime-smertnost_variables.datetime_for_woman_edge_trud).total_seconds() )
            #print("len(smertnost_variables.lists_woman_birth_death) = " + str(len(smertnost_variables.lists_woman_birth_death)) ) 
    
    # Завершения цикла по выборке дат рождений, смерти и пола 
    # (и дополнения списка трудоспособных в случае наличия) за текущий месяц
    #print("begin: count_all_trud = " + str(count_all_trud))
    
    count_man_trud = len(smertnost_variables.lists_man_birth_death)
    
    #print("prev year: count_man_trud = " + str(count_man_trud))
    
    count_woman_trud = len(smertnost_variables.lists_woman_birth_death)
    
    #print("prev year: count_woman_trud = " + str(count_woman_trud))
    
    count_all_trud = 0
    count_all_trud += len(smertnost_variables.lists_man_birth_death)
    count_all_trud += len(smertnost_variables.lists_woman_birth_death)
    
    #print("smertnost_puti.months_short[number_index_month] = " + smertnost_puti.months_short[number_index_month])        
    #print("count_all_trud = " + str(count_all_trud))
    
    smertnost_variables.count_all_trud = count_all_trud
    
    # учитываем по нарастающей
    if count_all_trud == 0:
        current_row = 0
    else:
        current_row = int(count_all_trud)
    smertnost_variables.tekushee_kolichestvo_vsego += current_row
    # print(smertnost_variables.tekushee_kolichestvo_vsego)        
    
    # обновляем подстроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if current_row:
        smertnost_variables.for_update_only_current_month = int(smertnost_variables.tekushee_kolichestvo_vsego)

        #print(smertnost_variables.outer_month)
        #print("smertnost_variables.count_all_trud = " + str(smertnost_variables.count_all_trud) )


        #print("int(smertnost_puti.population_prev_year) = " + smertnost_puti.population_prev_year)
        #print("smertnost_variables.count_all_trud / int(smertnost_puti.population_prev_year) = " +  \
        #    str( smertnost_variables.count_all_trud / int(smertnost_puti.population_prev_year) ) )
        #print( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_prev_year) ) * 1000)
        smertnost_variables.calc_100000_trud_human = round( (smertnost_variables.count_all_trud / int(smertnost_puti.population_prev_year) ) * 100000, 1 )
        
        #print(smertnost_variables.calc_100000_trud_human)
        
        temp_for_sql = smertnost_variables.calc_100000_trud_human
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        temp_for_sql = 0
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0
    
    current_row = 0        
    
    # UPDATE death_pokazateli SET "Смертность в трудоспособном возрасте, на 100000 населения: 2022" = "3.6" 
    # WHERE ( "Наименование: месяц" = "Янв." AND "Наименование: показатель" = "Пок-тель" )
    
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.column_name_trud_dvoetotsie_year_prev + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(temp_for_sql) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.pokazatel_short + '"' + " " + \
                                     ")" )
    
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.column_name_trud_dvoetotsie_year_prev + '"' + " " + \
                                     "=" + \
                                     " " + '"' + str(smertnost_variables.count_all_trud) + '"' + " " + \
                                     smertnost_variables.WHERE + " " + \
                                     "(" + 
                                     " " + '"' + smertnost_variables.column_name_pokazatal_month + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_puti.months_short[number_index_month] + '"' + " " + \
                                     smertnost_variables.AND + " " + \
                                     '"' + smertnost_variables.column_name_pokazatel + '"' + " " + \
                                     "=" + \
                                     " " + '"' + smertnost_variables.abs_human + '"' + " " + \
                                     ")" )


    number_index_month += 1




"""
print("smertnost_variables.lists_man_birth_death")
print(len(smertnost_variables.lists_man_birth_death) )

print("smertnost_variables.lists_woman_birth_death")
print(len(smertnost_variables.lists_woman_birth_death) )
"""
#quit()


smertnost_begin_sql.conn.commit()






