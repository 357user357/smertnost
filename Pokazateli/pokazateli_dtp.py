
import smertnost_puti
import smertnost_begin_sql
import smertnost_variables

import re



#########################
# Расчет относит. показателя по смертности от ДТП на 100 тысяч населения предыдущего года

number_index_month = 0

current_row = 0

smertnost_variables.tekushee_kolichestvo_vsego = 0



for smertnost_variables.outer_month in smertnost_puti.months:
    
    # по строкам "всего ДТП" предыдущего года
    
    # 
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_prev + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                '"' + smertnost_variables.column_period_po_zags + '"' + " " + \
                                                "==" + \
                                                " " + '"' + smertnost_variables.outer_month + '"' + " " + \
                                                smertnost_variables.AND + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_DTP + '"' + " " + \
                                                ")" + " " + \
                                                ")" ):
        # учитываем по нарастающей
        if row[0] == "-":
            current_row = 0
        else:
            current_row = int(row[0])
        
        #print(current_row)

        #print("smertnost_variables.tekushee_kolichestvo_vsego" + str(smertnost_variables.tekushee_kolichestvo_vsego) )

        if smertnost_variables.tekushee_kolichestvo_vsego>current_row:
            smertnost_variables.tekushee_kolichestvo_vsego = smertnost_variables.tekushee_kolichestvo_vsego
        else:
            smertnost_variables.tekushee_kolichestvo_vsego += current_row
        # print(smertnost_variables.tekushee_kolichestvo_vsego)
        
        
        # обновляем подстроки если поступили сведения из ЗАГС и
        # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
        if current_row or smertnost_variables.tekushee_kolichestvo_vsego:
            #print("loop")
            smertnost_variables.for_update_only_current_month = int(smertnost_variables.tekushee_kolichestvo_vsego)
            
            smertnost_variables.calc_100000_DTP_human = round( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_prev_year) ) * 100000, 1 )
            #print(smertnost_variables.calc_100000_DTP_human)
            temp_for_sql = smertnost_variables.calc_100000_DTP_human
        else:
            # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
            temp_for_sql = 0
            # до конца года будут нули по оставшимся месяцам текущего года
            smertnost_variables.for_update_only_current_month = 0
        
        
        
        ######################################################################
        # UPDATE death_pokazateli SET "хххххх" = "0" WHERE "Наименование: месяц" = "Янв."
        
        if current_row or smertnost_variables.tekushee_kolichestvo_vsego:
            # внесение сведений за текущий год в свод "умерло всего от ДТП"
            smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_DTP_100_000_human_year_prev + '"' + " " + \
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
            
            # внесение сведений за такой-то год в свод "умерло всего от ДТП"
            smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_DTP_100_000_human_year_prev + '"' + " " + \
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
# Расчет относит. показателя по смертности от ДТП на 100 тысяч населения текущего года

number_index_month = 0

current_row = 0

smertnost_variables.tekushee_kolichestvo_vsego = 0



for smertnost_variables.outer_month in smertnost_puti.months:
    
    # по строкам "всего ДТП" текущего года
    
    # 
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                '"' + smertnost_variables.column_period_po_zags + '"' + " " + \
                                                "==" + \
                                                " " + '"' + smertnost_variables.outer_month + '"' + " " + \
                                                smertnost_variables.AND + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_DTP + '"' + " " + \
                                                ")" + " " + \
                                                ")" ):
        # учитываем по нарастающей
        if row[0] == "-":
            current_row = 0
        else:
            current_row = int(row[0])
        
        #print(current_row)

        #print("smertnost_variables.tekushee_kolichestvo_vsego" + str(smertnost_variables.tekushee_kolichestvo_vsego) )

        if smertnost_variables.tekushee_kolichestvo_vsego>current_row:
            smertnost_variables.tekushee_kolichestvo_vsego = smertnost_variables.tekushee_kolichestvo_vsego
        else:
            smertnost_variables.tekushee_kolichestvo_vsego += current_row
        # print(smertnost_variables.tekushee_kolichestvo_vsego)
        
        
        # обновляем подстроки если поступили сведения из ЗАГС и
        # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
        if current_row or smertnost_variables.tekushee_kolichestvo_vsego:
            #print("loop")
            smertnost_variables.for_update_only_current_month = int(smertnost_variables.tekushee_kolichestvo_vsego)
            
            smertnost_variables.calc_100000_DTP_human = round( (smertnost_variables.tekushee_kolichestvo_vsego / int(smertnost_puti.population_current_year) ) * 100000, 1 )
            #print(smertnost_variables.calc_100000_DTP_human)
            temp_for_sql = smertnost_variables.calc_100000_DTP_human
        else:
            # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
            temp_for_sql = 0
            # до конца года будут нули по оставшимся месяцам текущего года
            smertnost_variables.for_update_only_current_month = 0
        
        
        
        ######################################################################
        # UPDATE death_pokazateli SET "хххххх" = "0" WHERE "Наименование: месяц" = "Янв."
        
        if current_row or smertnost_variables.tekushee_kolichestvo_vsego:
            # внесение сведений за текущий год в свод "умерло всего от ДТП"
            smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_DTP_100_000_human_year_cur + '"' + " " + \
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
            
            # внесение сведений за текущий год в свод "умерло всего от ДТП"
            smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_pokazateli + " " + \
                                     smertnost_variables.SET + \
                                     " " + '"' + smertnost_variables.title_death_DTP_100_000_human_year_cur + '"' + " " + \
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



