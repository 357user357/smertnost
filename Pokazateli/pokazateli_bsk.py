
import smertnost_puti
import smertnost_begin_sql
import smertnost_variables

import re



#########################
# Расчет относит. показателя по смертности от БСК на 100 тысяч населения за текущий год 


#print(insert_title)
#smertnost_begin_sql.cur2.execute(insert_title)
#smertnost_begin_sql.conn.commit()

number_index_month = 0

current_row = 0

smertnost_variables.tekushee_kolichestvo_vsego = 0

#############################################################################################################################

for smertnost_variables.outer_month in smertnost_puti.months:
    
    # по строкам "всего" текущего года
    
    # SELECT "Январь" FROM death_svod where "Показатель" = "БСК 2022 г."

    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + '"' + smertnost_variables.outer_month + '"' + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_svod + " " + \
                                                smertnost_variables.WHERE + \
                                                " " + smertnost_variables.column_pokazalel + " " + \
                                                "=" + \
                                                " " + '"' + smertnost_variables.BSK + " " + str(
                                                smertnost_puti.year_current) + " " + smertnost_variables.year_point + '"' ):
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
            smertnost_variables.calc_100000_bsk_human = round( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_current_year) ) * 100000, 1 )
            
            temp_for_sql = smertnost_variables.calc_100000_bsk_human
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
                                     " " + '"' + smertnost_variables.title_death_BSK_100_000_human_year_cur + '"' + " " + \
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
                                     " " + '"' + smertnost_variables.title_death_BSK_100_000_human_year_cur + '"' + " " + \
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





number_index_month = 0

current_row = 0

smertnost_variables.tekushee_kolichestvo_vsego = 0

#############################################################################################################################

for smertnost_variables.outer_month in smertnost_puti.months:
    
    # по строкам "всего" предыдущего года 

    # SELECT "Январь" FROM death_svod where "Показатель" = "БСК 2021 г."

    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + '"' + smertnost_variables.outer_month + '"' + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_svod + " " + \
                                                smertnost_variables.WHERE + \
                                                " " + smertnost_variables.column_pokazalel + " " + \
                                                "=" + \
                                                " " + '"' + smertnost_variables.BSK + " " + str(
                                                smertnost_puti.year_prev) + " " + smertnost_variables.year_point + '"' ):
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
            smertnost_variables.calc_100000_bsk_human = round( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_prev_year) ) * 100000, 1 )
            
            temp_for_sql = smertnost_variables.calc_100000_bsk_human
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
                                     " " + '"' + smertnost_variables.title_death_BSK_100_000_human_year_prev + '"' + " " + \
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
                                     " " + '"' + smertnost_variables.title_death_BSK_100_000_human_year_prev + '"' + " " + \
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



