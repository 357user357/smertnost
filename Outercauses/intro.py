
import smertnost_puti
import smertnost_begin_sql
import smertnost_variables


INSERT_to_death_svod = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                         smertnost_variables.table_death_svod + ' ' + smertnost_variables.VALUES + ' ' + '(' + "'"
                         

insert_title = INSERT_to_death_svod + "Показатель', "

for month in smertnost_puti.months:
    insert_title += "'"
    insert_title += month
    insert_title += "'"
    if month != "Декабрь":
        insert_title += " , "

insert_title += ")"


#only_first_appearence = 0
#for smertnost_variables.outer_month in smertnost_puti.months:

check_death_for_outer_causes = 0

for smertnost_variables.outer_month in smertnost_puti.months:
    #if not smertnost_puti.poliklinika:

    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + " " + smertnost_variables.count_row + " " + \
                                         smertnost_variables.FROM + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.WHERE + " " + \
                                         "(" + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.Outer_causes + " " + str(
                                         smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + " " + \
                                         smertnost_variables.AND + " " + \
                                         "(" + \
                                         " " + '"' + smertnost_variables.outer_month + '"' + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.zero + "'" + " " + \
                                         ")" + \
                                         ")" ):
        if row[0]:
            check_death_for_outer_causes += 1
        #print(row[0])
        #print("check_death_for_outer_causes = " + str(check_death_for_outer_causes))
        #else:
        #temp=0
        #if row[0] and not only_first_appearence:
        #    print("row[0] and not only_first_appearence")
        ############################################################    smertnost_begin_sql.cur2.execute(insert_title)
        #if row[0]:
        #    only_first_appearence = 1
        #print("only_first_appearence = " + str(only_first_appearence) )



check_death_for_outer_causes_for_tire = 0

for smertnost_variables.outer_month in smertnost_puti.months:
    #if not smertnost_puti.poliklinika:

    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + " " + smertnost_variables.count_row + " " + \
                                         smertnost_variables.FROM + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.WHERE + " " + \
                                         "(" + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.Outer_causes + " " + str(
                                         smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + " " + \
                                         smertnost_variables.AND + " " + \
                                         "(" + \
                                         " " + '"' + smertnost_variables.outer_month + '"' + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.tire + "'" + " " + \
                                         ")" + \
                                         ")" ):
        if row[0]:
            check_death_for_outer_causes_for_tire += 1
        #print(row[0])
        #print("check_death_for_outer_causes_for_tire = " + str(check_death_for_outer_causes_for_tire))

check_death_for_outer_causes += check_death_for_outer_causes_for_tire

if not check_death_for_outer_causes or (check_death_for_outer_causes < 12 and check_death_for_outer_causes != 0) :
    if not smertnost_puti.poliklinika:
        smertnost_begin_sql.cur2.execute(insert_title)


## Раскомментировать если потребуется во внешних причинах указывать остальные неуказанные заболевания
"""
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
"""

smertnost_variables.update_or_not = []

for smertnost_variables.outer_month in smertnost_puti.months:

    # SELECT Январь FROM death_svod WHERE ("Показатель" = 'всего 2022 г.')
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


    # по строкам текущего года "всего "Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ""
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
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[10] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[11] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[12] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[13] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[14] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[15] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[16] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[17] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[18] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH[19] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ"
        smertnost_variables.Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ"
            temp_for_sql = smertnost_variables.tire
        
        
        # внесение сведений за текущий год в свод таблицы смертности ""Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH) + "'")




















