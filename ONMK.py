import smertnost_begin_sql
import smertnost_puti
import smertnost_variables

smertnost_variables.update_or_not = []

for smertnost_variables.outer_month in smertnost_puti.months:
    ### по строкам из журнала смертности "всего ОНМК" предыдущего года
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
                                                " " + '"' + smertnost_variables.sql_ONMK[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[4] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # переменная по строкам "всего ОНМК" предыдущего года
        smertnost_variables.ONMK_vsego_prev += row[0]
        # внесение сведений за предыдущий год в свод "ОНМК всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.ONMK_vsego_prev) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.ONMK + " " + str(
            smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'")

    # по строкам из журнала смертности "всего ОНМК" текущего года
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
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ONMK[4] + '"' + " " + \
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
        smertnost_variables.ONMK_vsego += row[0]
        # проверяет есть ли смертность за данный месяц
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.ONMK_vsego
        else:
            # либо оставляем нули до конца текущего года
            temp_for_sql = smertnost_variables.tire

        # внесение сведений в обзор смертности за текущий год "ОНМК всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.ONMK + " " + str(
            smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'")
        # переменная по строкам "всего прирост/убыль ОНМК" за текущий год
        Raznost_ONMK = smertnost_variables.ONMK_vsego - smertnost_variables.ONMK_vsego_prev
        # проверяет есть ли смертность за данный месяц
        if select_cur_total[0] != '0':
            temp_for_sql = Raznost_ONMK
        else:
            # либо оставляем нули по строкам "всего прирост/убыль ОНМК" до конца текущего года
            temp_for_sql = smertnost_variables.tire

        # внесение разности между обоими годами в свод обзора смертности "всего прирост/убыль ОНМК"
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
                                         smertnost_variables.ONMK + " " + \
                                         smertnost_variables.prirost + " " + \
                                         str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                         smertnost_variables.slash + \
                                         str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + \
                                         "'")