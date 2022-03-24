
import smertnost_begin_sql
import smertnost_puti
import smertnost_variables

smertnost_variables.update_or_not = []

for smertnost_variables.outer_month in smertnost_puti.months:
    
    ### по строкам из журнала смертности "всего Внешние причины" предыдущего года
    """
    # Старая версия:
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
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[0] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[1] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[2] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[3] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[4] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[5] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[6] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[7] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[8] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[9] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[10] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[11] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[12] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[13] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[14] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[15] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[16] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[17] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[18] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[19] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[20] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        """
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
                                                " " + '"' + smertnost_variables.sql_Outer_causes[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[6] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):

        # переменная по строкам "всего Внешние причины" предыдущего года
        smertnost_variables.Outer_causes_vsego_prev += row[0]
        # внесение сведений за предыдущий год в свод "Внешние причины всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Outer_causes_vsego_prev) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.Outer_causes + " " + str(
            smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'")
    
    
    """

    SELECT count(*) FROM death WHERE 
    ("Период по ЗАГС" == "Январь" 
    AND 
    ( 
    "Причина смерти" NOT LIKE "A15%" AND "Причина смерти" NOT LIKE "A16%" AND "Причина смерти" NOT LIKE "A17%" AND "Причина смерти" NOT LIKE "A18%" 
    AND "Причина смерти" NOT LIKE "A19%" AND "Причина смерти" NOT LIKE "B20%" AND "Причина смерти" NOT LIKE "B21%" AND "Причина смерти" NOT LIKE "B22%" 
    AND "Причина смерти" NOT LIKE "B23%" AND "Причина смерти" NOT LIKE "B24%" AND "Причина смерти" NOT LIKE "C%" AND "Причина смерти" NOT LIKE "D%" 
    AND "Причина смерти" NOT LIKE "E%" AND "Причина смерти" NOT LIKE "F%" AND "Причина смерти" NOT LIKE "G%" AND "Причина смерти" NOT LIKE "I%" 
    AND "Причина смерти" NOT LIKE "J%" AND "Причина смерти" NOT LIKE "K%" AND "Причина смерти" NOT LIKE "M%" AND "Причина смерти" NOT LIKE "N%" 
    AND "Причина смерти" NOT LIKE "R54%" 
    ) 
    )

    "A15%" "A16%" "A17%" "A18%" "A19%" "B20%" "B21%" "B22%" "B23%" "B24%" "C%" "D%" "E%" "F%" "G%" "I%" "J%" "K%" "M%" "N%" "R54%"
    
    """
    
    # по строкам из журнала смертности "всего Внешние причины" текущего года
    
    """
    # Старая версия:
    
    for row in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                '"' + smertnost_variables.column_period_po_zags + '"' + " " + \
                                                "==" + \
                                                " " + '"' + smertnost_variables.outer_month + '"' + " " + \
                                                smertnost_variables.AND + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[0] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[1] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[2] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[3] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[4] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[5] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[6] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[7] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[8] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[9] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[10] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[11] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[12] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[13] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[14] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[15] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[16] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[17] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[18] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[19] + '"' + " " + \
                                                smertnost_variables.AND + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.NOT + " " + smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[20] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        """
    
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
                                                " " + '"' + smertnost_variables.sql_Outer_causes[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Outer_causes[6] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
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

        # учитываем по нарастающей текущего года
        smertnost_variables.Outer_causes_vsego += row[0]
        # проверяет есть ли смертность за данный месяц
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Outer_causes_vsego
        else:
            # либо оставляем нули до конца текущего года
            temp_for_sql = smertnost_variables.tire

        # внесение сведений в обзор смертности за текущий год "Внешние причины всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.Outer_causes + " " + str(
            smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'")
        # переменная по строкам "всего прирост/убыль Внешние причины" за текущий год
        smertnost_variables.Raznost_Outer_causes = smertnost_variables.Outer_causes_vsego - smertnost_variables.Outer_causes_vsego_prev
        # проверяет есть ли смертность за данный месяц
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Raznost_Outer_causes
        else:
            # либо оставляем нули по строкам "всего прирост/убыль Внешние причины" до конца текущего года
            temp_for_sql = smertnost_variables.tire

        # внесение разности между обоими годами в свод обзора смертности "всего прирост/убыль Внешние причины"
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
                                         smertnost_variables.Outer_causes + " " + \
                                         smertnost_variables.prirost + " " + \
                                         str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                         smertnost_variables.slash + \
                                         str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + \
                                         "'")


