import smertnost_begin_sql
import smertnost_puti
import smertnost_variables

smertnost_variables.update_or_not = []

for smertnost_variables.outer_month in smertnost_puti.months:
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
    # по строкам текущего года "всего ЗНО пищевода"
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
                                                " " + '"' + smertnost_variables.sql_Rak_pizhevoda + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак пищевода
        smertnost_variables.Rak_pizhevoda_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак пищевода
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_pizhevoda_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак пищевода
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак пищевода всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_pizhevoda) + "'")
    
    ###smertnost_begin_sql.conn.commit()
    
    # по строкам текущего года "всего ЗНО желудка"
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
                                                " " + '"' + smertnost_variables.sql_Rak_zheludka + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак желудка
        smertnost_variables.Rak_zheludka_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак желудка
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_zheludka_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак желудка
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак желудка всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_zheludka) + "'")

    # по строкам текущего года "всего ЗНО прямой кишки"
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
                                                " " + '"' + smertnost_variables.sql_Rak_pryamoy_kishki[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_pryamoy_kishki[1] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак прямой кишки
        smertnost_variables.Rak_pryamoy_kishki_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак прямой кишки
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_pryamoy_kishki_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак прямой кишки
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак прямой кишки всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_pryamoy_kishki) + "'")

    # по строкам текущего года "всего ЗНО легкого"
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
                                                " " + '"' + smertnost_variables.sql_Rak_legkogo + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак легкого
        smertnost_variables.Rak_legkogo_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак легкого
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_legkogo_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак легкого
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак легкого всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_legkogo) + "'")



    # по строкам текущего года "всего ЗНО соединит. тканей"
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
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_soed_tkaney[7] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак соединит. тканей
        smertnost_variables.Rak_soed_tkaney_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак соединит. тканей
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_soed_tkaney_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак соединит. тканей
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак соединит. тканей всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_soed_tkaney) + "'")



    # по строкам текущего года "всего ЗНО молочной железы"
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
                                                " " + '"' + smertnost_variables.sql_Rak_molochnoy_zhel + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак молочной железы
        smertnost_variables.Rak_molochnoy_zhel_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак молочной железы
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_molochnoy_zhel_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак молочной железы
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак молочной железы всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_molochnoy_zhel) + "'")

    # по строкам текущего года "всего ЗНО печени"
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
                                                " " + '"' + smertnost_variables.sql_Rak_hepar + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак печени
        smertnost_variables.Rak_hepar_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак печени
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_hepar_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак печени
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак печени всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_hepar) + "'")


    # по строкам текущего года "всего ЗНО носа"
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
                                                " " + '"' + smertnost_variables.sql_Rak_nosa + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак носа
        smertnost_variables.Rak_nosa_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак носа
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_nosa_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак носа
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак носа всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_nosa) + "'")


    # по строкам текущего года "всего ЗНО желчного протока"
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
                                                " " + '"' + smertnost_variables.sql_Rak_zhelchnogo_protoka + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак желчного протока
        smertnost_variables.Rak_zhelchnogo_protoka_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак желчного протока
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_zhelchnogo_protoka_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак желчного протока
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак желчного протока всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_zhelchnogo_protoka) + "'")


    # по строкам текущего года "всего ЗНО поджелудочной железы"
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
                                                " " + '"' + smertnost_variables.sql_Rak_podzheludochnoy_zhelezy + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак поджелудочной железы
        smertnost_variables.Rak_podzheludochnoy_zhelezy_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак поджелудочной железы
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_podzheludochnoy_zhelezy_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак поджелудочной железы
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак поджелудочной железы всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_podzheludochnoy_zhelezy) + "'")


    # по строкам текущего года "всего ЗНО яичника"
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
                                                " " + '"' + smertnost_variables.sql_Rak_yichnika + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак яичника
        smertnost_variables.Rak_yichnika_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак яичника
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_yichnika_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак яичника
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак яичника всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_yichnika) + "'")


    # по строкам текущего года "всего ЗНО предстательной железы"
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
                                                " " + '"' + smertnost_variables.sql_Rak_predstat_zhelezy + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак предстательной железы
        smertnost_variables.Rak_predstat_zhelezy_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак предстательной железы
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_predstat_zhelezy_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак предстательной железы
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак предстательной железы всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_predstat_zhelezy) + "'")


    # по строкам текущего года "всего ЗНО матки"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_uteri[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_uteri[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_uteri[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак матки
        smertnost_variables.Malignant_neoplasm_uteri_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак матки
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_uteri_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак матки
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак матки всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_uteri) + "'")



    # по строкам текущего года "всего ЗНО почки"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_kidney[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_kidney[1] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак почки
        smertnost_variables.Malignant_neoplasm_kidney_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак почки
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_kidney_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак почки
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак почки всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_kidney) + "'")


    # по строкам текущего года "всего ЗНО мочевого пузыря"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_bladder[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_bladder[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_bladder[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак мочевого пузыря
        smertnost_variables.Malignant_neoplasm_bladder_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак мочевого пузыря
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_bladder_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак мочевого пузыря
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак мочевого пузыря всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_bladder) + "'")


    # по строкам текущего года "всего ЗНО головного мозга"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_brain[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_brain[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_brain[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак головного мозга
        smertnost_variables.Malignant_neoplasm_brain_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак головного мозга
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_brain_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак головного мозга
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак головного мозга всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_brain) + "'")


    # по строкам текущего года "всего ЗНО щитовидной железы"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_thyroid_gland[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_thyroid_gland[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_thyroid_gland[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак щитовидной железы
        smertnost_variables.Malignant_neoplasm_thyroid_gland_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак щитовидной железы
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_thyroid_gland_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак щитовидной железы
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак щитовидной железы всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_thyroid_gland) + "'")



    # по строкам текущего года "всего ЗНО ободочной кишки"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_obodochnoy_colon[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: Онкология Рак ободочной кишки
        smertnost_variables.Malignant_neoplasm_obodochnoy_colon_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу Онкология Рак ободочной кишки
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_obodochnoy_colon_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу Онкология Рак ободочной кишки
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "Рак ободочной кишки всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_obodochnoy_colon) + "'")


    # по строкам текущего года "всего ЗНО Множественная миелома"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_Multiple_myeloma + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: ЗНО Множественная миелома
        smertnost_variables.Malignant_neoplasm_Multiple_myeloma_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу ЗНО Множественная миелома
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_Multiple_myeloma_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу ЗНО Множественная миелома
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "ЗНО Множественная миелома всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_Multiple_myeloma) + "'")


    # по строкам текущего года "всего ЗНО Лейкоз"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_Leukaemia[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_Leukaemia[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_Leukaemia[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_Leukaemia[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_Leukaemia[4] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: ЗНО Лейкоз
        smertnost_variables.Malignant_neoplasm_Leukaemia_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу ЗНО Лейкоз
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_Leukaemia_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу ЗНО Лейкоз
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "ЗНО Лейкоз всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_Leukaemia) + "'")


    ###########################################################################
    # по строкам текущего года "всего ЗНО лимфатических узлов"
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
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_lymph_nodes[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_lymph_nodes[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_lymph_nodes[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_lymph_nodes[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Malignant_neoplasm_lymph_nodes[4] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: ЗНО лимфатических узлов
        smertnost_variables.Malignant_neoplasm_lymph_nodes_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу ЗНО лимфатических узлов
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Malignant_neoplasm_lymph_nodes_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу ЗНО лимфатических узлов
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности "ЗНО лимфатических узлов всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Malignant_neoplasm_lymph_nodes) + "'")
    
    
    
    # по строкам текущего года "всего "Губы, полости рта и глотки""
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
                                                " " + '"' + smertnost_variables.sql_ZNO_Guby_polosti_rta_i_glotki[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Guby_polosti_rta_i_glotki[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Guby_polosti_rta_i_glotki[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Guby_polosti_rta_i_glotki[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Guby_polosti_rta_i_glotki[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Guby_polosti_rta_i_glotki[5] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Губы, полости рта и глотки"
        smertnost_variables.ZNO_Guby_polosti_rta_i_glotki_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Губы, полости рта и глотки"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.ZNO_Guby_polosti_rta_i_glotki_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Губы, полости рта и глотки"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Губы, полости рта и глотки" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.ZNO_Guby_polosti_rta_i_glotki) + "'")
    
    
    
    
    # по строкам текущего года "всего "Рак тонкого кишечника""
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
                                                " " + '"' + smertnost_variables.sql_Rak_tonkogo_kishechnika[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак тонкого кишечника"
        smertnost_variables.Rak_tonkogo_kishechnika_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак тонкого кишечника"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_tonkogo_kishechnika_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак тонкого кишечника"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак тонкого кишечника" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_tonkogo_kishechnika) + "'")
    
    
    
    
    # по строкам текущего года "всего "Рак ректосигмоидного соединения""
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
                                                " " + '"' + smertnost_variables.sql_Rak_rektosigmoidnogo_soedineniya[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак ректосигмоидного соединения"
        smertnost_variables.Rak_rektosigmoidnogo_soedineniya_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак ректосигмоидного соединения"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_rektosigmoidnogo_soedineniya_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак ректосигмоидного соединения"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак ректосигмоидного соединения" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_rektosigmoidnogo_soedineniya) + "'")
    
    
    
    # по строкам текущего года "всего "Рак желчного пузыря""
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
                                                " " + '"' + smertnost_variables.sql_Rak_zhelchnogo_puzyrya[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак желчного пузыря"
        smertnost_variables.Rak_zhelchnogo_puzyrya_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак желчного пузыря"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_zhelchnogo_puzyrya_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак желчного пузыря"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак желчного пузыря" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_zhelchnogo_puzyrya) + "'")
    
    
    
    # по строкам текущего года "всего "Рак других органов пищеварения""
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
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_organov_pishchevareniya[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак других органов пищеварения"
        smertnost_variables.Rak_drugih_organov_pishchevareniya_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак других органов пищеварения"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_drugih_organov_pishchevareniya_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак других органов пищеварения"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак других органов пищеварения" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_drugih_organov_pishchevareniya) + "'")
    
    
    # по строкам текущего года "всего "Рак придаточных пазух, гортани и трахеи""
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
                                                " " + '"' + smertnost_variables.sql_Rak_pridatochnyh_pazuh_gortani_i_trahei[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_pridatochnyh_pazuh_gortani_i_trahei[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_pridatochnyh_pazuh_gortani_i_trahei[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак придаточных пазух, гортани и трахеи"
        smertnost_variables.Rak_pridatochnyh_pazuh_gortani_i_trahei_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак придаточных пазух, гортани и трахеи"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_pridatochnyh_pazuh_gortani_i_trahei_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак придаточных пазух, гортани и трахеи"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак придаточных пазух, гортани и трахеи" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_pridatochnyh_pazuh_gortani_i_trahei) + "'")


    # по строкам текущего года "всего "Рак других органов дыхания""
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
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_organov_dyhaniya[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_organov_dyhaniya[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_organov_dyhaniya[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак других органов дыхания"
        smertnost_variables.Rak_drugih_organov_dyhaniya_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак других органов дыхания"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_drugih_organov_dyhaniya_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак других органов дыхания"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак других органов дыхания" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_drugih_organov_dyhaniya) + "'")
    
    
    
    # по строкам текущего года "всего "Рак женских половых органов""
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
                                                " " + '"' + smertnost_variables.sql_Rak_zhenskih_polovyh_organov[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_zhenskih_polovyh_organov[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_zhenskih_polovyh_organov[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_zhenskih_polovyh_organov[3] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак женских половых органов"
        smertnost_variables.Rak_zhenskih_polovyh_organov_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак женских половых органов"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_zhenskih_polovyh_organov_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак женских половых органов"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак женских половых органов" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_zhenskih_polovyh_organov) + "'")
    
    
    # по строкам текущего года "всего "Рак других мужских половых органов""
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
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_muzhskih_polovyh_organov[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_muzhskih_polovyh_organov[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Rak_drugih_muzhskih_polovyh_organov[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак других мужских половых органов"
        smertnost_variables.Rak_drugih_muzhskih_polovyh_organov_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак других мужских половых органов"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_drugih_muzhskih_polovyh_organov_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак других мужских половых органов"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак других мужских половых органов" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_drugih_muzhskih_polovyh_organov) + "'")
    
    
    
    # по строкам текущего года "всего "Рак глаза""
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
                                                " " + '"' + smertnost_variables.sql_Rak_glaza[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Рак глаза"
        smertnost_variables.Rak_glaza_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Рак глаза"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Rak_glaza_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Рак глаза"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Рак глаза" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Rak_glaza) + "'")
    
    
    
    # по строкам текущего года "всего "Лимфомы""
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
                                                " " + '"' + smertnost_variables.sql_ZNO_Limfomy[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Limfomy[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Limfomy[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Limfomy[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Limfomy[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_ZNO_Limfomy[5] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Лимфомы"
        smertnost_variables.ZNO_Limfomy_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Лимфомы"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.ZNO_Limfomy_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Лимфомы"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Лимфомы" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.ZNO_Limfomy) + "'")
    
    
    # по строкам текущего года "всего "Злокач. иммунопролиф. б-ни""
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
                                                " " + '"' + smertnost_variables.sql_Zlokach_immunoprolif_b_ni[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Злокач. иммунопролиф. б-ни"
        smertnost_variables.Zlokach_immunoprolif_b_ni_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Злокач. иммунопролиф. б-ни"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Zlokach_immunoprolif_b_ni_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Злокач. иммунопролиф. б-ни"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Злокач. иммунопролиф. б-ни" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Zlokach_immunoprolif_b_ni) + "'")
    
    
    # по строкам текущего года "всего "Другие ЗНО лимфоид. и кроветвор. тканей""
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
                                                " " + '"' + smertnost_variables.sql_Drugie_ZNO_limfoid_i_krovetvor_tkanej[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
        # учитываем по нарастающей предыдущего года: "Другие ЗНО лимфоид. и кроветвор. тканей"
        smertnost_variables.Drugie_ZNO_limfoid_i_krovetvor_tkanej_vsego += row[0]
        # проверяет есть ли смертность за данный месяц по поводу "Другие ЗНО лимфоид. и кроветвор. тканей"
        if select_cur_total[0] != '0':
            temp_for_sql = smertnost_variables.Drugie_ZNO_limfoid_i_krovetvor_tkanej_vsego
        else:
            # либо оставляем нули до конца текущего года по поводу "Другие ЗНО лимфоид. и кроветвор. тканей"
            temp_for_sql = smertnost_variables.tire

        # внесение сведений за текущий год в свод таблицы смертности ""Другие ЗНО лимфоид. и кроветвор. тканей" всего"
        smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Drugie_ZNO_limfoid_i_krovetvor_tkanej) + "'")






