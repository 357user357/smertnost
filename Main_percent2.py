
import smertnost_begin_sql
import smertnost_puti
import smertnost_variables

i=1

smertnost_variables.update_or_not = []
smertnost_variables.BSK_vsego = 0
smertnost_variables.percent_BSK_vsego = 0


# делаем отдельный прогон по месяцам чтобы определить месяц по которому будем сортировать: smertnost_puti.current_month_for_percent_sort
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года     
    # перебираем кол-во за каждый месяц по нарастающей умерших      
    
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        # данная переменная неинформативна так как создает массив добавляя за каждый месяц новый элемент
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        
        if smertnost_variables.select_cur_month_total[0] == '0':
            #print("smertnost_variables.outer_month : " + smertnost_variables.outer_month)
            # сохраняем месяц с которого у нас будут нули так как нет сведений за этот и последующие месяцы в данном году 
            if not smertnost_variables.before_this_month_do_sort :
                smertnost_variables.before_this_month_do_sort = smertnost_variables.outer_month
            #print("smertnost_variables.before_this_month_do_sort11 : " + smertnost_variables.before_this_month_do_sort)

        #print(smertnost_variables.before_this_month_do_sort)

        # перебираем месяцы и сохраняем тот месяц, который был перед нулевым месяцем: smertnost_variables.before_this_month_do_sort
        # так мы узнаем по которому месяцу будем делать сортировку по процентам
        ii=1
        for month in smertnost_puti.months:
            #print(ii)
            if month != smertnost_variables.before_this_month_do_sort:
                ii += 1
            else:
                ####print(smertnost_puti.new_array_month[ii])
                smertnost_puti.current_month_for_percent_sort = smertnost_puti.new_array_month[ii]
                #print("smertnost_puti.current_month_for_percent_sort = " + smertnost_puti.current_month_for_percent_sort)
        ii=1
        
        if smertnost_puti.current_month_for_percent_sort == "" :
            smertnost_puti.current_month_for_percent_sort = smertnost_puti.new_array_month[12]


for smertnost_variables.outer_month in smertnost_puti.months:

    # пока что временно дублируем запрос чтобы быть в курсе loop текущее значение smertnost_variables.select_cur_month_total для
    # данного месяца
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.total + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):
        no_usage = ''

    

    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Б-нь сист. кровообр. 2021 г.') """        
    for smertnost_variables.BSK_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.BSK + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = smertnost_variables.BSK_vsego[0]                                                      
        # учитываем по нарастающей
        ######################3smertnost_variables.BSK_vsego += int(select_cur_BSK_total[0])

    ###print(smertnost_variables.select_cur_month_total[0])

    # обновляем подстроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0': 
        ##########################print("smertnost_variables.BSK_vsego : " + str(smertnost_variables.BSK_vsego) ) 

        smertnost_variables.temp_for_sql = round( ( int(smertnost_variables.BSK_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        #quit()
        temp_for_sql2 = smertnost_variables.temp_for_sql
        smertnost_variables.temp_for_sql2 = temp_for_sql2
        temp_for_sql = str(temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        temp_for_sql = "-"        
        temp_for_sql2 = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0
    
    ######print(temp_for_sql2)

    if smertnost_variables.outer_month == smertnost_puti.current_month_for_percent_sort:
        temp = {}
        temp[0] = smertnost_variables.BSK
        smertnost_variables.temp_for_sql2 = 0
        temp[1] = smertnost_variables.temp_for_sql2
        smertnost_variables.array_nosology_for_sort_month[i] = temp
        i += 1
        #print(smertnost_variables.array_nosology_for_sort_month)
    
    
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.percent_BSK + "'")
    


smertnost_variables.update_or_not = []
smertnost_variables.percent_Oncology_vsego = 0

# Онкология
for smertnost_variables.outer_month in smertnost_puti.months: 

    # пока что временно дублируем запрос чтобы быть в курсе loop текущее значение smertnost_variables.select_cur_month_total для
    # данного месяца
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.total + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):
        no_usage = ''       
        
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Злокач. новообр-я 2021 г.') """
        
    for smertnost_variables.ZNO_Oncology_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.ZNO + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):
        temp_no_usage = 0 

    for smertnost_variables.Benign_Oncology_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Benign_neoplasm + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):
        #print("smertnost_variables.Benign_Oncology_vsego[0] : " + smertnost_variables.Benign_Oncology_vsego[0]) 
        temp_no_usage = 0        
    
    # обновляем подстроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0':
        #print('11')
        #print("smertnost_variables.Oncology_vsego = " + str(smertnost_variables.Oncology_vsego) )
        #print("smertnost_variables.ZNO_Oncology_vsego = " + str(smertnost_variables.ZNO_Oncology_vsego) )
        
        if not smertnost_variables.Benign_Oncology_vsego:
            smertnost_variables.Benign_Oncology_vsego = {}
            smertnost_variables.Benign_Oncology_vsego[0] = 0
        smertnost_variables.Oncology_vsego = int(smertnost_variables.Benign_Oncology_vsego[0]) + int(smertnost_variables.ZNO_Oncology_vsego[0])
        #print("smertnost_variables.Oncology_vsego : " + str(smertnost_variables.Oncology_vsego) )
        #quit()

        smertnost_variables.temp_for_sql2 = round( ( int(smertnost_variables.Oncology_vsego) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        #print(smertnost_variables.temp_for_sql)
        #quit()
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"
        smertnost_variables.temp_for_sql2 = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    #print(smertnost_variables.temp_for_sql2)

    if smertnost_variables.outer_month == smertnost_puti.current_month_for_percent_sort:
        temp = {}
        temp[0] = smertnost_variables.title_percent_Oncology
        temp[1] = smertnost_variables.temp_for_sql2
        smertnost_variables.array_nosology_for_sort_month[i] = temp
        i += 1
        #print(smertnost_variables.array_nosology_for_sort_month)


    # внесение сведений за текущий год в свод "умерло всего"
    
    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Oncology + \
                                           "'" )




# ДС
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года                                            
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        no_usage = ''
        
        
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'ДС 2021 г.') """
        
    for smertnost_variables.Respiratory_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Respiratory + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = 0                                            

    # обновляем подстроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0': 
        smertnost_variables.temp_for_sql2 = round( ( int(smertnost_variables.Respiratory_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"        
        smertnost_variables.temp_for_sql2 = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    """
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                     smertnost_variables.title_percent_Respiratory_system + \
                                           "'")
    """

    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Respiratory_system + \
                                           "'" )
  



# Б-ни эндокрин. системы
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года                                            
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        temp_no_usage = 0
        
        
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Б-ни эндокрин. системы 2021 г.') """
        
    for smertnost_variables.Endocrine_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Endocrine + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = 0                                            

    # обновляем поБ-ни эндокрин. системы cтроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0': 
        smertnost_variables.temp_for_sql2 = round( ( int(smertnost_variables.Endocrine_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"        
        smertnost_variables.temp_for_sql2 = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    """
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.title_percent_Endocrine_system + "'")

    """

    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Endocrine_system + \
                                           "'" )  





# Старость
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года                                            
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        temp_no_usage = 0
        
        
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Старость 2021 г.') """
        
    for smertnost_variables.Senility_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Senility + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = 0                                            

    # обновляем поСтаростьтроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0': 
        smertnost_variables.temp_for_sql2 = round( ( int(smertnost_variables.Senility_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"        
        smertnost_variables.temp_for_sql2 = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    """
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.title_percent_Senility + "'")
    """

    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Senility + \
                                           "'" )  




# Психические заболевания
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        temp_no_usage = 0

    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Психические заболевания 2021 г.') """

    for smertnost_variables.Mental_disorders_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                                       ' ' + smertnost_variables.outer_month + ' ' + \
                                                                                       smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                                       smertnost_variables.WHERE + " " + \
                                                                                       "(" + \
                                                                                       '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                                       "=" + \
                                                                                       " " + "'" + smertnost_variables.Mental_disorders + " " + str(
        smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                                       ")"):
        temp_no_usage = 0

        # обновляем поПсихические заболеваниятроки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0':
        smertnost_variables.temp_for_sql2 = round(
            (int(smertnost_variables.Mental_disorders_vsego[0]) / int(smertnost_variables.select_cur_month_total[0])) * 100, 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"
        smertnost_variables.temp_for_sql2 = "-"
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0
    
    """
    print(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.title_percent_Mental_disorders + "'")
    """
    # UPDATE death_svod SET Январь = '0.0%' WHERE Показатель = 'псих. 3%'

    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.title_percent_Mental_disorders + "'")
    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Mental_disorders + \
                                           "'" ) 




# Заболевания ЖКТ
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        temp_no_usage = 0

    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Заболевания ЖКТ 2021 г.') """

    for smertnost_variables.Digestive_system_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                                       ' ' + smertnost_variables.outer_month + ' ' + \
                                                                                       smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                                       smertnost_variables.WHERE + " " + \
                                                                                       "(" + \
                                                                                       '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                                       "=" + \
                                                                                       " " + "'" + smertnost_variables.Digestive + " " + str(
                                                                                        smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                                       ")"):
        temp_no_usage = 0

        # обновляем по Заболевания ЖКТ строки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0':
        smertnost_variables.temp_for_sql2 = round(
            (int(smertnost_variables.Digestive_system_vsego[0]) / int(smertnost_variables.select_cur_month_total[0])) * 100, 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"
        smertnost_variables.temp_for_sql2 = "-"
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    """
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                     smertnost_variables.title_percent_Digestive_system + \
                                     "'")
    """

    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Digestive_system + \
                                           "'" )






# Болезни нервной системы
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        temp_no_usage = 0

    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Болезни нервной системы 2021 г.') """

    for smertnost_variables.Nervous_system_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                                     ' ' + smertnost_variables.outer_month + ' ' + \
                                                                                     smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                                     smertnost_variables.WHERE + " " + \
                                                                                     "(" + \
                                                                                     '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                                     "=" + \
                                                                                     " " + "'" + smertnost_variables.Nervous_system + " " + str(
                                                                                    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                                     ")"):
        temp_no_usage = 0

        # обновляем по Болезни нервной системы строки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0':
        smertnost_variables.temp_for_sql2 = round(
            (int(smertnost_variables.Nervous_system_vsego[0]) / int(smertnost_variables.select_cur_month_total[0])) * 100, 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"
        smertnost_variables.temp_for_sql2 = "-"
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    """
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                     smertnost_variables.title_percent_Nervous_system + \
                                     "'")
    """

    # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Nervous_system + \
                                           "'" )



# ХПН (б-ни почек)
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2021 г.')"""
    # по строкам "всего" текущего года                                            
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        # smertnost_variables.update_or_not.append(select_cur_month_total[0])
        temp_no_usage = 0
        
        
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'ХПН (б-ни почек) 2021 г.') """
        
    for smertnost_variables.Genitourinary_system_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Genitourinary_system + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = 0                                            

    # обновляем по ХПН (б-ни почек) строки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0': 
        smertnost_variables.temp_for_sql2 = round( ( int(smertnost_variables.Genitourinary_system_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql2) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"        
        smertnost_variables.temp_for_sql2 = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    """
    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                     smertnost_variables.title_percent_Genitourinary_system + \
                                           "'" )
    """

      # пока что попробую продублировать процентную информацию с основной таблицей где "свод"                                       
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod_percent + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + str(smertnost_variables.temp_for_sql2) + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                         smertnost_variables.title_percent_Genitourinary_system + \
                                           "'" )



#print(smertnost_puti.current_month_for_percent_sort)


# " SELECT 
# death_svod.Показатель,
# death_svod.Январь, death_svod.Февраль, death_svod.Март, death_svod.Апрель, death_svod.Май, death_svod.Июнь,
# death_svod.Июль, death_svod.Август, death_svod.Сентябрь, death_svod.Октябрь, death_svod.Ноябрь, death_svod.Декабрь
# FROM death_svod WHERE (
# Показатель = 'Первое место: БСК 36%' 
# OR Показатель = 'Второе место: Онко. 15,6%'
# OR Показатель = 'Третье место: ДС 6%'
# OR Показатель = 'Четвертое место: энд 1,7%'
# OR Показатель = 'Пятое место: старость 3,5%'
# OR Показатель = 'Шестое место: псих 3,1%'
# OR Показатель = 'Седьмое место: пищ 6%'
# OR Показатель = 'Восьмое место: ЦНС 1,7%'
# OR Показатель = 'Девятое место: МПС 0,4%'
# ) 
# ORDER BY death_svod." + smertnost_puti.current_month_for_percent_sort

"""

UPDATE 

SELECT death_svod_percent.id, death_svod_percent.Показатель,
death_svod_percent.Январь, death_svod_percent.Февраль, death_svod_percent.Март, 
death_svod_percent.Апрель, death_svod_percent.Май, death_svod_percent.Июнь,
death_svod_percent.Июль, death_svod_percent.Август, death_svod_percent.Сентябрь, 
death_svod_percent.Октябрь, death_svod_percent.Ноябрь, death_svod_percent.Декабрь
FROM death_svod_percent WHERE (
Показатель = 'БСК 36%' 
OR Показатель = 'Онко. 15,6%'
OR Показатель = 'ДС 6%'
OR Показатель = 'энд 1,7%'
OR Показатель = 'старость 3,5%'
OR Показатель = 'псих 3,1%'
OR Показатель = 'пищ 6%'
OR Показатель = 'ЦНС 1,7%'
OR Показатель = 'МПС 0,4%'
) ORDER BY death_svod_percent.Сентябрь DESC


РАБОЧИЙ:

SELECT * from death_svod_percent order by Сентябрь desc

Обновлять буду понятным способом: выгружу оба массива и буду перебирать каждый массив в поиске соответствия
по графе "Показатель" и после нахождения соответствия делать запрос по каждой строке в первоначальной таблице где
порядок уже известен. Также в обновлении таблицы актуализировать слова например "Первое место" и т.д.
. 

"""

"""
print("SELECT death_svod_percent.Old_id, death_svod_percent.New_id, death_svod_percent.Показатель,"
"death_svod_percent.Январь, death_svod_percent.Февраль, death_svod_percent.Март, "
"death_svod_percent.Апрель, death_svod_percent.Май, death_svod_percent.Июнь, "
"death_svod_percent.Июль, death_svod_percent.Август, death_svod_percent.Сентябрь, "
"death_svod_percent.Октябрь, death_svod_percent.Ноябрь, death_svod_percent.Декабрь "
"FROM death_svod_percent WHERE ("
"Показатель = 'БСК 36%' "
"OR Показатель = 'Онко. 15,6%' "
"OR Показатель = 'ДС 6%' "
"OR Показатель = 'энд 1,7%' "
"OR Показатель = 'старость 3,5%' "
"OR Показатель = 'псих 3,1%' "
"OR Показатель = 'пищ 6%' "
"OR Показатель = 'ЦНС 1,7%' "
"OR Показатель = 'МПС 0,4%' "
") ORDER BY death_svod_percent." + smertnost_puti.current_month_for_percent_sort + " DESC ")
"""

temp_sql_list_months = ""

i=1

for smertnost_variables.outer_month in smertnost_puti.months:
    temp_sql_list_months += smertnost_variables.table_death_svod_percent + smertnost_variables.point + smertnost_variables.outer_month
    if not i==12:
        temp_sql_list_months += ", "
    i += 1

#print(temp_sql_list_months)


select_svod_percent_desc = smertnost_begin_sql.cur2.execute (smertnost_variables.SELECT + " " +     \
    smertnost_variables.table_death_svod_percent + smertnost_variables.point + "Old_id" + " " + "," + " " +     \
    smertnost_variables.table_death_svod_percent + smertnost_variables.point + "New_id" + " " + "," + " " +     \
    smertnost_variables.table_death_svod_percent + smertnost_variables.point + smertnost_variables.column_pokazalel + " " + "," + " " +     \
temp_sql_list_months + " " +    \
smertnost_variables.FROM + " " + smertnost_variables.table_death_svod_percent + " " + smertnost_variables.WHERE + " " + "(" +     \
smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.percent_BSK + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Oncology + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Respiratory_system + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Endocrine_system + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Senility + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Mental_disorders + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Digestive_system + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Nervous_system + '"' + " " +     \
smertnost_variables.OR + " " + smertnost_variables.column_pokazalel + " " + "=" + " " '"' + smertnost_variables.title_percent_Genitourinary_system + '"' + " " +     \
") ORDER BY " + smertnost_variables.table_death_svod_percent + smertnost_variables.point + smertnost_puti.current_month_for_percent_sort + " DESC ") 


#print(smertnost_puti.current_month_for_percent_sort)


#print(select_svod_percent_desc.fetchall() )
    
select_rows_percent_desc = select_svod_percent_desc.fetchall()

#print(select_rows_percent_desc)


New_id = 1

for row_without_New_id in select_rows_percent_desc :
    #print(New_id)
    # первые три столбца это старый и новый айди плюс Показатель
    number_month = 3
    for smertnost_variables.outer_month in smertnost_puti.months :
        #print(row_without_New_id[2])
        #print ("UPDATE death_svod_percent SET " + \
        #                    smertnost_variables.outer_month + " = '" + str(row_without_New_id[number_month]) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ")
        #print("UPDATE death_svod_percent SET " + \
        #                        smertnost_variables.outer_month + " = '" + str(row_without_New_id[number_month]) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ")
        # UPDATE death_svod_percent SET Январь = '61.5' WHERE Показатель = 'БСК 36%'
        smertnost_begin_sql.cur2.execute ("UPDATE death_svod_percent SET " + \
                                smertnost_variables.outer_month + " = '" + str(row_without_New_id[number_month]) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ")
        number_month += 1

    #print("UPDATE death_svod_percent SET Old_id = '" + str(row_without_New_id[0]) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ")
    smertnost_begin_sql.cur2.execute ("UPDATE death_svod_percent SET Old_id = '" + str(row_without_New_id[0]) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ")
    #print("UPDATE death_svod_percent SET New_id = '" + str(New_id) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ") 
    smertnost_begin_sql.cur2.execute ("UPDATE death_svod_percent SET New_id = '" + str(New_id) + "' WHERE Показатель = '" + row_without_New_id[2] + "' ")    
    New_id += 1    


# результат брать из РАБОЧЕГО ВАРИАНТА:

# SELECT * from "death_svod_percent" order by New_id asc

select_svod_percent_desc = smertnost_begin_sql.cur2.execute ("SELECT * from death_svod_percent order by New_id asc")


INSERT_to_death_svod = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                         smertnost_variables.table_death_svod + ' ' + smertnost_variables.VALUES + ' ' + '(' + "'"

#print(select_rows_percent_desc)

i = 1
for row_with_New_id in select_rows_percent_desc :
    insert = INSERT_to_death_svod + str(i) + " место: "
    insert += str(row_with_New_id[2]) + "', '"
    for ii in range(3,14) :
        #print(ii)
        if row_with_New_id[ii] != '-' :
            insert += str(row_with_New_id[ii]) + "%', '"
        else :
           insert += str(row_with_New_id[ii]) + "', '"
    if row_with_New_id[14] != '-' :
        insert += str(row_with_New_id[14]) + "%')"
    else :
        insert += str(row_with_New_id[14]) + "')"
    #print(insert)
    smertnost_begin_sql.cur2.execute(insert)
    
    """
    smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + str(i) + " место: " + \
                                    str(row_with_New_id[2]) + "%', '" + str(row_with_New_id[3]) + "%', '" + str(row_with_New_id[4]) + "%', '" + \
                                    str(row_with_New_id[5]) + "%', '" + str(row_with_New_id[6]) + "%', '" + str(row_with_New_id[7]) + "%', '" + \
                                    str(row_with_New_id[8]) + "%', '" + str(row_with_New_id[9]) + "%', '" + str(row_with_New_id[10]) + "%', '" + \
                                    str(row_with_New_id[11]) + "%', '" + str(row_with_New_id[12]) + "%', '" + str(row_with_New_id[13]) + "%', '" + \
                                    str(row_with_New_id[14]) + "%')")
    """
    i += 1


#smertnost_begin_sql.conn.commit()


#quit()







# INSERT INTO death_svod VALUES ('ВИЧ',  '-',  '-',  '-',  '-',  '-',  '-',  '-',  '-',  '-',  '-',  '-',  '-' )


# Если нужно указывать строку ВИЧ без сортировки - то снять комментирование этих строк:
"""
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 smertnost_variables.VICH + "'" + ", " + smertnost_puti.tire_12 + ")")
"""







# ВИЧ
for smertnost_variables.outer_month in smertnost_puti.months:

    """ SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2022 г.') """    
    # по строкам "всего" текущего года                                            
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        no_usage = ''
    
    
    
        
    """ SELECT Январь FROM death_svod WHERE ("Показатель" = 'ВИЧ 2022 г.') """        
    for smertnost_variables.VICH_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.VICH + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = 0                                            
    
        

    
    # обновляем по ВИЧ строки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0':
        #print("smertnost_variables.VICH_vsego = " + str(smertnost_variables.VICH_vsego) )
        #print("smertnost_variables.select_cur_month_total = " + str(smertnost_variables.select_cur_month_total) )
        
        if not smertnost_variables.VICH_vsego:
            smertnost_variables.VICH_vsego = {}
            smertnost_variables.VICH_vsego[0] = 0

        smertnost_variables.temp_for_sql = round( ( int(smertnost_variables.VICH_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                     smertnost_variables.VICH + \
                                           "'" )
  





if not smertnost_puti.poliklinika:
    smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 smertnost_variables.title_percent_Outer_causes + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")

smertnost_variables.Outer_causes_vsego = 0

# Внешние причины
for smertnost_variables.outer_month in smertnost_puti.months:
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2022 г.')"""
    # по строкам "всего" текущего года                                            
    for smertnost_variables.select_cur_month_total in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
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
        #smertnost_variables.update_or_not.append(select_cur_month_total[0])
        no_usage = ''
    
            
    """SELECT Январь FROM death_svod WHERE ("Показатель" = 'Внешние причины 2021 г.') """
    
    """
    print(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Outer_causes + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")")
    """
    
    for smertnost_variables.Outer_causes_vsego in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                                 ' ' + smertnost_variables.outer_month + ' ' + \
                                                                 smertnost_variables.FROM + ' ' + smertnost_variables.table_death_svod + " " + \
                                                                 smertnost_variables.WHERE + " " + \
                                                                 "(" + \
                                                                 '"' + smertnost_variables.column_pokazalel + '"' + " " + \
                                                                 "=" + \
                                                                 " " + "'" + smertnost_variables.Outer_causes + " " + str(
                                                                 smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + \
                                                                 ")"):     
        temp_no_usage = 0                                            
    
    #smertnost_begin_sql.conn.commit()
    
    #print(smertnost_variables.Outer_causes_vsego)

    #quit()    

    # обновляем по Внешние причины строки если поступили сведения из ЗАГС и
    # переменная smertnost_variables.for_update_only_current_month тогда не равна нулю
    if smertnost_variables.select_cur_month_total[0] != '0': 
        
        #print(smertnost_variables.Outer_causes_vsego)
        #print(smertnost_variables.select_cur_month_total)
        
        if not smertnost_variables.Outer_causes_vsego:
            smertnost_variables.Outer_causes_vsego = {}
            smertnost_variables.Outer_causes_vsego[0] = 0
        
        smertnost_variables.temp_for_sql = round( ( int(smertnost_variables.Outer_causes_vsego[0]) / int(smertnost_variables.select_cur_month_total[0]) ) * 100 , 1)
        smertnost_variables.temp_for_sql = str(smertnost_variables.temp_for_sql) + "%"
    else:
        # в любом случае изменяем значения temp_for_sql из предыдущих строк свода
        smertnost_variables.temp_for_sql = "-"        
        # до конца года будут нули по оставшимся месяцам текущего года
        smertnost_variables.for_update_only_current_month = 0

    # внесение сведений за текущий год в свод "умерло всего"
    smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + " " + smertnost_variables.table_death_svod + " " + \
                                     smertnost_variables.SET + \
                                     " " + smertnost_variables.outer_month + " " + \
                                     "=" + \
                                     " " + "'" + smertnost_variables.temp_for_sql + "'" + " " + \
                                     smertnost_variables.WHERE + \
                                     " " + smertnost_variables.column_pokazalel + " " + \
                                     "=" + \
                                     " " + "'" + \
                                     smertnost_variables.title_percent_Outer_causes + \
                                           "'" )
  





smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 "*Анализ показателей проводить по нарастающей" + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 "" + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 "" + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")

