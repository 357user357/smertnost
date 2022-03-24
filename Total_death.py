
import smertnost_begin_sql
import smertnost_puti
import smertnost_variables

smertnost_variables.update_or_not = []
smertnost_variables.tekushee_kolichestvo_vsego_prev = 0
smertnost_variables.tekushee_kolichestvo_vsego = 0

for smertnost_variables.outer_month in smertnost_puti.months:
    # по строкам "всего" предыдущего года
    # ((( переменные для запросов не стал создавать динамически так как это не безопасно )))
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                            ' ' + smertnost_variables.count_row + ' ' + \
                                            smertnost_variables.FROM + \
                                            ' ' + smertnost_variables.table_death_prev + ' ' + \
                                            smertnost_variables.WHERE + \
                                            ' ' + '"' + smertnost_variables.column_period_po_zags + '"' + ' ' + \
                                            '==' + \
                                            ' ' + '"' + smertnost_variables.outer_month + '"'):
        # учитываем по нарастающей
        smertnost_variables.tekushee_kolichestvo_vsego_prev += row[0]
        # внесение сведений за предыдущий год в свод "умерло всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                     " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.tekushee_kolichestvo_vsego_prev) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.death_all_cause2 + " " + str(
                                        smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'")
    
    
    
    # по строкам "всего" текущего года
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                            ' ' + smertnost_variables.count_row + ' ' + \
                                            smertnost_variables.FROM + \
                                            ' ' + smertnost_variables.table_death_cur + ' ' + \
                                            smertnost_variables.WHERE + \
                                            ' ' + '"' + smertnost_variables.column_period_po_zags + '"' + ' ' + \
                                            '==' + \
                                            ' ' + '"' + smertnost_variables.outer_month + '"'):



                                            
        for select_cur_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.total + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):
            # проверяет есть ли смертность за данный месяц
            smertnost_variables.update_or_not.append(select_cur_total[0])
        
        
        
        
        
        # учитываем по нарастающей
        smertnost_variables.tekushee_kolichestvo_vsego += row[0]
        # обновляем подстроки если поступили сведения из ЗАГС и
        # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
        if row[0]:
            smertnost_variables.for_update_only_current_month = smertnost_variables.tekushee_kolichestvo_vsego
            temp_for_sql = smertnost_variables.tekushee_kolichestvo_vsego
        else:
            # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
            temp_for_sql = smertnost_variables.tire
            # до конца года будут нули по оставшимся месяцам текущего года
            smertnost_variables.for_update_only_current_month = 0

        # внесение сведений за текущий год в свод "умерло всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(temp_for_sql) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.death_all_cause2 + " " + str(
                                        smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'")
        
        
        
        # переменная по строкам "всего прирост/убыль" за текущий год
        smertnost_variables.Raznost_tekushee_kolichestvo_vsego = smertnost_variables.tekushee_kolichestvo_vsego - smertnost_variables.tekushee_kolichestvo_vsego_prev
        # проверяет есть ли смертность за данный месяц
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Raznost_tekushee_kolichestvo_vsego
        else:
            # либо оставляем нули по строкам "всего прирост/убыль" до конца текущего года
            temp_for_sql = smertnost_variables.tire

        # внесение разности между обоими годами в свод обзора смертности "всего прирост/убыль"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + " " + \
                                         "'" + \
                                         smertnost_variables.death_all_cause2 + " " + \
                                         smertnost_variables.prirost + " " + \
                                         str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                         smertnost_variables.slash + \
                                         str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + \
                                         "'")








