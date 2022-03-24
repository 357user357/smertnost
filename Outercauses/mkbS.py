
import smertnost_puti
import smertnost_begin_sql
import smertnost_variables


INSERT_to_death_svod = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                         smertnost_variables.table_death_svod + ' ' + smertnost_variables.VALUES + ' ' + '(' + "'"


smertnost_variables.update_or_not = []

first_insert_Travmy_golovy = 1
first_insert_Travmy_shei = 1
first_insert_Travmy_grudnoj_kletki = 1
first_insert_Travmy_zhivota_nizhnej_chasti_spiny_i_taza = 1
first_insert_Travmy_plechevogo_poyasa_i_plecha = 1
first_insert_Travmy_loktya_i_predplechya = 1
first_insert_Travmy_zapyastya_i_kisti = 1
first_insert_Travmy_tazobedr_sustava_i_bedra = 1
first_insert_Travmy_kolena_i_goleni = 1
first_insert_Travmy_golenostop_sustava_i_stopy = 1

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
    

    # по строкам текущего года "всего по всем месяцам "Травмы головы""

    # SELECT count(*) FROM death WHERE ( "Причина смерти" LIKE "S0%" )
        
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_golovy[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_golovy:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_golovy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_golovy = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы головы""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_golovy[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы головы"
          smertnost_variables.Travmy_golovy_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы головы"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_golovy_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы головы"
              temp_for_sql = smertnost_variables.tire
          
          # внесение сведений за текущий год в свод таблицы смертности ""Травмы головы" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_golovy) + "'")
    
    
    
    # по строкам текущего года "всего по всем месяцам "Травмы шеи""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_shei[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_shei:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_shei + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_shei = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы шеи""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_shei[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы шеи"
          smertnost_variables.Travmy_shei_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы шеи"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_shei_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы шеи"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы шеи" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_shei) + "'")
    
    
    # по строкам текущего года "всего по всем месяцам "Травмы грудной клетки""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_grudnoj_kletki[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_grudnoj_kletki:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_grudnoj_kletki + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_grudnoj_kletki = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы грудной клетки""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_grudnoj_kletki[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы грудной клетки"
          smertnost_variables.Travmy_grudnoj_kletki_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы грудной клетки"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_grudnoj_kletki_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы грудной клетки"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы грудной клетки" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_grudnoj_kletki) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы живота, нижней части спины и таза""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zhivota_nizhnej_chasti_spiny_i_taza[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_zhivota_nizhnej_chasti_spiny_i_taza:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_zhivota_nizhnej_chasti_spiny_i_taza + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_zhivota_nizhnej_chasti_spiny_i_taza = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы живота, нижней части спины и таза""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_zhivota_nizhnej_chasti_spiny_i_taza[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы живота, нижней части спины и таза"
          smertnost_variables.Travmy_zhivota_nizhnej_chasti_spiny_i_taza_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы живота, нижней части спины и таза"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_zhivota_nizhnej_chasti_spiny_i_taza_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы живота, нижней части спины и таза"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы живота, нижней части спины и таза" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_zhivota_nizhnej_chasti_spiny_i_taza) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы плечевого пояса и плеча""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_plechevogo_poyasa_i_plecha[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_plechevogo_poyasa_i_plecha:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_plechevogo_poyasa_i_plecha + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_plechevogo_poyasa_i_plecha = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы плечевого пояса и плеча""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_plechevogo_poyasa_i_plecha[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы плечевого пояса и плеча"
          smertnost_variables.Travmy_plechevogo_poyasa_i_plecha_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы плечевого пояса и плеча"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_plechevogo_poyasa_i_plecha_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы плечевого пояса и плеча"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы плечевого пояса и плеча" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_plechevogo_poyasa_i_plecha) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы локтя и предплечья""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_loktya_i_predplechya[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_loktya_i_predplechya:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_loktya_i_predplechya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_loktya_i_predplechya = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы локтя и предплечья""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_loktya_i_predplechya[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы локтя и предплечья"
          smertnost_variables.Travmy_loktya_i_predplechya_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы локтя и предплечья"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_loktya_i_predplechya_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы локтя и предплечья"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы локтя и предплечья" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_loktya_i_predplechya) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы запястья и кисти""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zapyastya_i_kisti[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_zapyastya_i_kisti:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_zapyastya_i_kisti + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_zapyastya_i_kisti = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы запястья и кисти""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_zapyastya_i_kisti[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы запястья и кисти"
          smertnost_variables.Travmy_zapyastya_i_kisti_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы запястья и кисти"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_zapyastya_i_kisti_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы запястья и кисти"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы запястья и кисти" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_zapyastya_i_kisti) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы тазобедр. сустава и бедра""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_tazobedr_sustava_i_bedra[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_tazobedr_sustava_i_bedra:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_tazobedr_sustava_i_bedra + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_tazobedr_sustava_i_bedra = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы тазобедр. сустава и бедра""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_tazobedr_sustava_i_bedra[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы тазобедр. сустава и бедра"
          smertnost_variables.Travmy_tazobedr_sustava_i_bedra_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы тазобедр. сустава и бедра"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_tazobedr_sustava_i_bedra_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы тазобедр. сустава и бедра"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы тазобедр. сустава и бедра" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_tazobedr_sustava_i_bedra) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы колена и голени""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_kolena_i_goleni[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_kolena_i_goleni:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_kolena_i_goleni + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_kolena_i_goleni = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы колена и голени""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_kolena_i_goleni[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы колена и голени"
          smertnost_variables.Travmy_kolena_i_goleni_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы колена и голени"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_kolena_i_goleni_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы колена и голени"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы колена и голени" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_kolena_i_goleni) + "'")




    # по строкам текущего года "всего по всем месяцам "Травмы голеностоп. сустава и стопы""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_golenostop_sustava_i_stopy[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_golenostop_sustava_i_stopy:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_golenostop_sustava_i_stopy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_golenostop_sustava_i_stopy = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы голеностоп. сустава и стопы""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_golenostop_sustava_i_stopy[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы голеностоп. сустава и стопы"
          smertnost_variables.Travmy_golenostop_sustava_i_stopy_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы голеностоп. сустава и стопы"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_golenostop_sustava_i_stopy_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы голеностоп. сустава и стопы"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы голеностоп. сустава и стопы" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_golenostop_sustava_i_stopy) + "'")