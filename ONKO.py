import smertnost_begin_sql
import smertnost_puti
import smertnost_variables

smertnost_variables.update_or_not = []

for smertnost_variables.outer_month in smertnost_puti.months:
        # по строкам "всего Онкология" предыдущего года
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
                                                " " + '"' + smertnost_variables.sql_Onko + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология
        smertnost_variables.ZNO_vsego_prev += row[0]

        # внесение сведений за предыдущий год в свод таблицы смертности "Онкология всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.ZNO_vsego_prev) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.ZNO + " " + str(
            smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'")

    # по строкам "всего Онкология" текущего года
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
                                                " " + '"' + smertnost_variables.sql_Onko + '"' + " " + \
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

        # учитываем по нарастающей текущего года: Онкология
        smertnost_variables.ZNO_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.ZNO_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология
            temp_for_sql = smertnost_variables.tire

        # внесение сведений в обзор смертности за текущий год "Онкология всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.ZNO + " " + str(
            smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'")

        # по строкам "всего прирост/убыль Онкология"
        Raznost_ZNO = smertnost_variables.ZNO_vsego - smertnost_variables.ZNO_vsego_prev
        # проверяет есть ли смертность за данный месяц по поводу Онкология
        if select_cur_total[0] != '0':
            temp_for_sql = Raznost_ZNO
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология
            temp_for_sql = smertnost_variables.tire

        # внесение разности между обоими годами в свод обзора смертности
        # "всего прирост/убыль Онкология"
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
                                         smertnost_variables.ZNO + " " + \
                                         smertnost_variables.prirost + " " + \
                                         str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                         smertnost_variables.slash + \
                                         str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + \
                                         "'")



for smertnost_variables.outer_month in smertnost_puti.months:
        # по строкам "всего Онкология доброкачественная и/или неуточненная" предыдущего года
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
                                                " " + '"' + smertnost_variables.sql_Benign_neoplasm + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология доброкачественная и/или неуточненная
        smertnost_variables.Benign_neoplasm_vsego_prev += row[0]

        # внесение сведений за предыдущий год в свод таблицы смертности "Онкология доброкачественная и/или неуточненная всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Benign_neoplasm_vsego_prev) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.Benign_neoplasm + " " + str(
            smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'")

    # по строкам "всего Онкология доброкачественная и/или неуточненная" текущего года
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
                                                " " + '"' + smertnost_variables.sql_Benign_neoplasm + '"' + " " + \
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

        # учитываем по нарастающей текущего года: Онкология доброкачественная и/или неуточненная
        smertnost_variables.Benign_neoplasm_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология доброкачественная и/или неуточненная
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Benign_neoplasm_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология доброкачественная и/или неуточненная
            temp_for_sql = smertnost_variables.tire

        # внесение сведений в обзор смертности за текущий год "Онкология доброкачественная и/или неуточненная всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + smertnost_variables.Benign_neoplasm + " " + str(
            smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'")

        # по строкам "всего прирост/убыль Онкология доброкачественная и/или неуточненная"
        RaBenign_neoplasmst_Benign_neoplasm = smertnost_variables.Benign_neoplasm_vsego - smertnost_variables.Benign_neoplasm_vsego_prev
        # проверяет есть ли смертность за данный месяц по поводу Онкология доброкачественная и/или неуточненная
        if select_cur_total[0] != '0':
            temp_for_sql = RaBenign_neoplasmst_Benign_neoplasm
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология доброкачественная и/или неуточненная
            temp_for_sql = smertnost_variables.tire

        # внесение разности между обоими годами в свод обзора смертности
        # "всего прирост/убыль Онкология доброкачественная и/или неуточненная"
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
                                         smertnost_variables.Benign_neoplasm + " " + \
                                         smertnost_variables.prirost + " " + \
                                         str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                         smertnost_variables.slash + \
                                         str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + \
                                         "'")












