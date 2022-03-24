import smertnost_puti
import smertnost_begin_sql
import smertnost_variables


INSERT_to_death_svod = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                         smertnost_variables.table_death_svod + ' ' + smertnost_variables.VALUES + ' ' + '(' + "'"


smertnost_variables.update_or_not = []

first_insert_Travmy_zahvat_neskolko_oblastej_tela = 1
first_insert_Travmy_neutoch_chasti_tela = 1
first_insert_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya = 1
first_insert_Termicheskie_i_himicheskie_ozhogi = 1
first_insert_Otmorozhenie = 1
first_insert_Otr_lek_sr_med_i_biol_v_mi = 1
first_insert_Toks_d_e_v_v_preim_nemed_nazn_ya = 1
first_insert_Dr_i_neut_eff_vozd_ya_vnesh_prichin = 1
first_insert_Nek_e_rannie_oslozh_travmy = 1
first_insert_Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n = 1
first_insert_Transportnye_neschastnye_sluchai = 1
first_insert_Dr_vn_prich_travm_pri_nesch_sl_h = 1
first_insert_Prednamerennoe_samopovrezhdenie = 1
first_insert_D_ya_predusm_zakonom_i_voen_op_i = 1
first_insert_Osl_ter_i_hir_vm_v = 1
first_insert_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i = 1
first_insert_Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r = 1
first_insert_COVID_dr_kody_dlya_osobyh_celej = 1



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


    # по строкам текущего года "всего по всем месяцам "Травмы голеностоп. сустава и стопы""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[7] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_zahvat_neskolko_oblastej_tela:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_zahvat_neskolko_oblastej_tela + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_zahvat_neskolko_oblastej_tela = 0
    
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
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_zahvat_neskolko_oblastej_tela[6] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы голеностоп. сустава и стопы"
          smertnost_variables.Travmy_zahvat_neskolko_oblastej_tela_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы голеностоп. сустава и стопы"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_zahvat_neskolko_oblastej_tela_vsego
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
                                         " " + "'" + str(smertnost_variables.Travmy_zahvat_neskolko_oblastej_tela) + "'")



    # по строкам текущего года "всего по всем месяцам "Травмы неуточ. части тела""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[6] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Travmy_neutoch_chasti_tela:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Travmy_neutoch_chasti_tela + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Travmy_neutoch_chasti_tela = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Травмы неуточ. части тела""
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
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Travmy_neutoch_chasti_tela[6] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Травмы неуточ. части тела"
          smertnost_variables.Travmy_neutoch_chasti_tela_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Травмы неуточ. части тела"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Travmy_neutoch_chasti_tela_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Травмы неуточ. части тела"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Травмы неуточ. части тела" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Travmy_neutoch_chasti_tela) + "'")



    # по строкам текущего года "всего по всем месяцам "Последствия проникн. инород. тела через естеств-е отверстия""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[4] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Последствия проникн. инород. тела через естеств-е отверстия""
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
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya[4] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Последствия проникн. инород. тела через естеств-е отверстия"
          smertnost_variables.Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Последствия проникн. инород. тела через естеств-е отверстия"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Последствия проникн. инород. тела через естеств-е отверстия"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Последствия проникн. инород. тела через естеств-е отверстия" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya) + "'")




    # по строкам текущего года "всего по всем месяцам "Термические и химические ожоги""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[3] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Termicheskie_i_himicheskie_ozhogi:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Termicheskie_i_himicheskie_ozhogi + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Termicheskie_i_himicheskie_ozhogi = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Термические и химические ожоги""
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
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Termicheskie_i_himicheskie_ozhogi[3] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Термические и химические ожоги"
          smertnost_variables.Termicheskie_i_himicheskie_ozhogi_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Термические и химические ожоги"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Termicheskie_i_himicheskie_ozhogi_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Термические и химические ожоги"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Термические и химические ожоги" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Termicheskie_i_himicheskie_ozhogi) + "'")



    # по строкам текущего года "всего по всем месяцам "Отморожение""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otmorozhenie[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otmorozhenie[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otmorozhenie[2] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Otmorozhenie:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Otmorozhenie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Otmorozhenie = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Отморожение""
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
                                                " " + '"' + smertnost_variables.sql_Otmorozhenie[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otmorozhenie[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otmorozhenie[2] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Отморожение"
          smertnost_variables.Otmorozhenie_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Отморожение"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Otmorozhenie_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Отморожение"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Отморожение" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Otmorozhenie) + "'")



    # по строкам текущего года "всего по всем месяцам "Отр. лек. ср., мед. и биол. в-ми""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[5] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Otr_lek_sr_med_i_biol_v_mi:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Otr_lek_sr_med_i_biol_v_mi + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Otr_lek_sr_med_i_biol_v_mi = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Отр. лек. ср., мед. и биол. в-ми""
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
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Otr_lek_sr_med_i_biol_v_mi[5] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Отр. лек. ср., мед. и биол. в-ми"
          smertnost_variables.Otr_lek_sr_med_i_biol_v_mi_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Отр. лек. ср., мед. и биол. в-ми"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Otr_lek_sr_med_i_biol_v_mi_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Отр. лек. ср., мед. и биол. в-ми"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Отр. лек. ср., мед. и биол. в-ми" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Otr_lek_sr_med_i_biol_v_mi) + "'")




    # по строкам текущего года "всего по всем месяцам "Токс. д-е в-в, преим. немед. назн-я""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[10] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[11] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[12] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[13] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[14] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Toks_d_e_v_v_preim_nemed_nazn_ya:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Toks_d_e_v_v_preim_nemed_nazn_ya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Toks_d_e_v_v_preim_nemed_nazn_ya = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Токс. д-е в-в, преим. немед. назн-я""
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
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[10] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[11] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[12] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[13] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Toks_d_e_v_v_preim_nemed_nazn_ya[14] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Токс. д-е в-в, преим. немед. назн-я"
          smertnost_variables.Toks_d_e_v_v_preim_nemed_nazn_ya_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Токс. д-е в-в, преим. немед. назн-я"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Toks_d_e_v_v_preim_nemed_nazn_ya_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Токс. д-е в-в, преим. немед. назн-я"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Токс. д-е в-в, преим. немед. назн-я" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Toks_d_e_v_v_preim_nemed_nazn_ya) + "'")



    # по строкам текущего года "всего по всем месяцам "Др. и неут эфф. возд-я внеш. причин""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[10] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Dr_i_neut_eff_vozd_ya_vnesh_prichin:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Dr_i_neut_eff_vozd_ya_vnesh_prichin + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Dr_i_neut_eff_vozd_ya_vnesh_prichin = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Др. и неут эфф. возд-я внеш. причин""
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
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin[10] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Др. и неут эфф. возд-я внеш. причин"
          smertnost_variables.Dr_i_neut_eff_vozd_ya_vnesh_prichin_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Др. и неут эфф. возд-я внеш. причин"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Dr_i_neut_eff_vozd_ya_vnesh_prichin_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Др. и неут эфф. возд-я внеш. причин"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Др. и неут эфф. возд-я внеш. причин" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Dr_i_neut_eff_vozd_ya_vnesh_prichin) + "'")






    # по строкам текущего года "всего по всем месяцам "Нек-е ранние ослож. травмы""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Nek_e_rannie_oslozh_travmy[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Nek_e_rannie_oslozh_travmy[1] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Nek_e_rannie_oslozh_travmy:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Nek_e_rannie_oslozh_travmy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Nek_e_rannie_oslozh_travmy = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Нек-е ранние ослож. травмы""
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
                                                " " + '"' + smertnost_variables.sql_Nek_e_rannie_oslozh_travmy[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Nek_e_rannie_oslozh_travmy[1] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Нек-е ранние ослож. травмы"
          smertnost_variables.Nek_e_rannie_oslozh_travmy_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Нек-е ранние ослож. травмы"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Nek_e_rannie_oslozh_travmy_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Нек-е ранние ослож. травмы"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Нек-е ранние ослож. травмы" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Nek_e_rannie_oslozh_travmy) + "'")



    # по строкам текущего года "всего по всем месяцам "Послед-я травм, отр-й и др. возд-й внеш. пр-н""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Послед-я травм, отр-й и др. возд-й внеш. пр-н""
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
                                                " " + '"' + smertnost_variables.sql_Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Послед-я травм, отр-й и др. возд-й внеш. пр-н"
          smertnost_variables.Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Послед-я травм, отр-й и др. возд-й внеш. пр-н"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Послед-я травм, отр-й и др. возд-й внеш. пр-н"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Послед-я травм, отр-й и др. возд-й внеш. пр-н" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n) + "'")




    # по строкам текущего года "всего по всем месяцам "Транспортные несчастные случаи""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Transportnye_neschastnye_sluchai[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Transportnye_neschastnye_sluchai:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Transportnye_neschastnye_sluchai + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Transportnye_neschastnye_sluchai = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Транспортные несчастные случаи""
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
                                                " " + '"' + smertnost_variables.sql_Transportnye_neschastnye_sluchai[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Транспортные несчастные случаи"
          smertnost_variables.Transportnye_neschastnye_sluchai_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Транспортные несчастные случаи"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Transportnye_neschastnye_sluchai_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Транспортные несчастные случаи"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Транспортные несчастные случаи" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Transportnye_neschastnye_sluchai) + "'")






    # по строкам текущего года "всего по всем месяцам "Др. вн. прич. травм при несч. сл-х""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[6] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Dr_vn_prich_travm_pri_nesch_sl_h:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Dr_vn_prich_travm_pri_nesch_sl_h + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Dr_vn_prich_travm_pri_nesch_sl_h = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Др. вн. прич. травм при несч. сл-х""
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
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dr_vn_prich_travm_pri_nesch_sl_h[6] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Др. вн. прич. травм при несч. сл-х"
          smertnost_variables.Dr_vn_prich_travm_pri_nesch_sl_h_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Др. вн. прич. травм при несч. сл-х"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Dr_vn_prich_travm_pri_nesch_sl_h_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Др. вн. прич. травм при несч. сл-х"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Др. вн. прич. травм при несч. сл-х" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Dr_vn_prich_travm_pri_nesch_sl_h) + "'")




    # по строкам текущего года "всего по всем месяцам "Преднамеренное самоповреждение""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[10] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[11] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Prednamerennoe_samopovrezhdenie:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Prednamerennoe_samopovrezhdenie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Prednamerennoe_samopovrezhdenie = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Преднамеренное самоповреждение""
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
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[8] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[9] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[10] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Prednamerennoe_samopovrezhdenie[11] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Преднамеренное самоповреждение"
          smertnost_variables.Prednamerennoe_samopovrezhdenie_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Преднамеренное самоповреждение"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Prednamerennoe_samopovrezhdenie_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Преднамеренное самоповреждение"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Преднамеренное самоповреждение" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Prednamerennoe_samopovrezhdenie) + "'")




    # по строкам текущего года "всего по всем месяцам "Д-я, предусм. законом, и воен. оп-и""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_D_ya_predusm_zakonom_i_voen_op_i[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_D_ya_predusm_zakonom_i_voen_op_i[1] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_D_ya_predusm_zakonom_i_voen_op_i:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.D_ya_predusm_zakonom_i_voen_op_i + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_D_ya_predusm_zakonom_i_voen_op_i = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Д-я, предусм. законом, и воен. оп-и""
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
                                                " " + '"' + smertnost_variables.sql_D_ya_predusm_zakonom_i_voen_op_i[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_D_ya_predusm_zakonom_i_voen_op_i[1] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Д-я, предусм. законом, и воен. оп-и"
          smertnost_variables.D_ya_predusm_zakonom_i_voen_op_i_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Д-я, предусм. законом, и воен. оп-и"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.D_ya_predusm_zakonom_i_voen_op_i_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Д-я, предусм. законом, и воен. оп-и"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Д-я, предусм. законом, и воен. оп-и" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.D_ya_predusm_zakonom_i_voen_op_i) + "'")





    # по строкам текущего года "всего по всем месяцам "Осл. тер. и хир. вм-в""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[8] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Osl_ter_i_hir_vm_v:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Osl_ter_i_hir_vm_v + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Osl_ter_i_hir_vm_v = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Осл. тер. и хир. вм-в""
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
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[4] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[5] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[6] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[7] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Osl_ter_i_hir_vm_v[8] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Осл. тер. и хир. вм-в"
          smertnost_variables.Osl_ter_i_hir_vm_v_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Осл. тер. и хир. вм-в"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Osl_ter_i_hir_vm_v_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Осл. тер. и хир. вм-в"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Осл. тер. и хир. вм-в" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Osl_ter_i_hir_vm_v) + "'")




    # по строкам текущего года "всего по всем месяцам "Посл. воз-я внеш. пр-н заб-ти и см-и""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[4] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Посл. воз-я внеш. пр-н заб-ти и см-и""
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
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[0] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[1] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[2] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[3] + '"' + " " + \
                                                smertnost_variables.OR + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i[4] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Посл. воз-я внеш. пр-н заб-ти и см-и"
          smertnost_variables.Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Посл. воз-я внеш. пр-н заб-ти и см-и"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Посл. воз-я внеш. пр-н заб-ти и см-и"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Посл. воз-я внеш. пр-н заб-ти и см-и" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i) + "'")




    # по строкам текущего года "всего по всем месяцам "Доп. ф-ры, им. от-е к прич. заб. и см., кл. в др. р.""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "Доп. ф-ры, им. от-е к прич. заб. и см., кл. в др. р.""
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
                                                " " + '"' + smertnost_variables.sql_Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "Доп. ф-ры, им. от-е к прич. заб. и см., кл. в др. р."
          smertnost_variables.Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "Доп. ф-ры, им. от-е к прич. заб. и см., кл. в др. р."
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "Доп. ф-ры, им. от-е к прич. заб. и см., кл. в др. р."
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""Доп. ф-ры, им. от-е к прич. заб. и см., кл. в др. р." всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r) + "'")





    # по строкам текущего года "всего по всем месяцам "COVID, др. коды для особых целей""
    
    for row_all_months in smertnost_begin_sql.cur2.execute(smertnost_variables.SELECT + \
                                                ' ' + smertnost_variables.count_row + ' ' + \
                                                smertnost_variables.FROM + \
                                                ' ' + smertnost_variables.table_death_cur + ' ' + \
                                                smertnost_variables.WHERE + " " + \
                                                "(" + \
                                                " " + '"' + smertnost_variables.column_cause_death + '"' + " " + \
                                                smertnost_variables.LIKE + \
                                                " " + '"' + smertnost_variables.sql_COVID_dr_kody_dlya_osobyh_celej[0] + '"' + " " + \
                                                ")"):
      if row_all_months[0] and first_insert_COVID_dr_kody_dlya_osobyh_celej:
        smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.COVID_dr_kody_dlya_osobyh_celej + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
        first_insert_COVID_dr_kody_dlya_osobyh_celej = 0
    
    if row_all_months[0]:
      # по строкам текущего года за текущий месяц "всего "COVID, др. коды для особых целей""
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
                                                " " + '"' + smertnost_variables.sql_COVID_dr_kody_dlya_osobyh_celej[0] + '"' + " " + \
                                                ")" + " " + \
                                                ")"):
          # учитываем по нарастающей предыдущего года: "COVID, др. коды для особых целей"
          smertnost_variables.COVID_dr_kody_dlya_osobyh_celej_vsego += row[0]
          # проверяет есть ли смертность за данный месяц по поводу "COVID, др. коды для особых целей"
          if select_cur_total[0] != '0':
              temp_for_sql = smertnost_variables.COVID_dr_kody_dlya_osobyh_celej_vsego
          else:
              # либо оставляем нули до конца текущего года по поводу "COVID, др. коды для особых целей"
              temp_for_sql = smertnost_variables.tire

          # внесение сведений за текущий год в свод таблицы смертности ""COVID, др. коды для особых целей" всего"
          smertnost_begin_sql.cur2.execute(smertnost_variables.UPDATE + \
                                         " " + smertnost_variables.table_death_svod + " " + \
                                         smertnost_variables.SET + \
                                         " " + smertnost_variables.outer_month + " " + \
                                         "=" + \
                                         " " + "'" + str(temp_for_sql) + "'" + " " + \
                                         smertnost_variables.WHERE + \
                                         " " + smertnost_variables.column_pokazalel + " " + \
                                         "=" + \
                                         " " + "'" + str(smertnost_variables.COVID_dr_kody_dlya_osobyh_celej) + "'")









