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





smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 "Численность населения на " + str(smertnost_puti.year_prev) + " всего: " + \
                                     str(smertnost_puti.population_prev_year) + "'" + ", " + smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 "Численность населения на " + str(smertnost_puti.year_current) + " всего: " + \
                                     str(smertnost_puti.population_current_year) + "'" + ", " + smertnost_puti.tire_12 + ")")

"""
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 "-" + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")
"""

smertnost_begin_sql.cur2.execute(insert_title)

# вносим шаблонные строки для заготовки таблицы смертности
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 smertnost_variables.death_all_cause + " " + smertnost_variables.total + smertnost_variables.dvoetotsie + "'" + ", " + smertnost_puti.tire_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.total + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.total + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.BSK + " " + smertnost_variables.total + smertnost_variables.dvoetotsie + " " + "'" + ", " + smertnost_puti.tire_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.BSK + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.BSK + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.BSK + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + smertnost_variables.slash + \
                                 str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + " " + smertnost_variables.v_tom_tsisle + smertnost_variables.dvoetotsie + \
                                 "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.OIM + smertnost_variables.star + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.OIM + smertnost_variables.star + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.OIM + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + smertnost_variables.slash + \
                                 str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ONMK + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ONMK + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ONMK + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + smertnost_variables.slash + \
                                 str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.IBS + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.IBS + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.IBS + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + smertnost_variables.slash + \
                                 str(smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.GB + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.GB + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.GB + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + smertnost_variables.slash + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.TSA + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.TSA + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.TSA + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + smertnost_variables.slash + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.nuli_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.P_ONMK + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.P_ONMK + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.P_ONMK + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + smertnost_variables.slash + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.nuli_12 + ")")

if smertnost_puti.poliklinika:
  #print("poliklinika")
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Polik_Arterii_arterioli_kapilary + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Polik_Arterii_arterioli_kapilary + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Polik_Arterii_arterioli_kapilary + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + smertnost_variables.slash + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.nuli_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.VK_about_death + " " + smertnost_variables.OIM + ", " + smertnost_variables.ONMK + "'" + " , " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(insert_title)

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ZNO + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ZNO + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ZNO + " " + smertnost_variables.prirost + " " + str(
    smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + smertnost_variables.slash + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.nuli_12 + ")")


if not smertnost_puti.poliklinika:
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Po_local + smertnost_variables.dvoetotsie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ZNO_Guby_polosti_rta_i_glotki + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_soed_tkaney + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_nosa + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_pridatochnyh_pazuh_gortani_i_trahei + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_drugih_organov_dyhaniya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_legkogo + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_pizhevoda + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_zheludka + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_hepar + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_zhelchnogo_puzyrya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_zhelchnogo_protoka + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_podzheludochnoy_zhelezy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_tonkogo_kishechnika + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_obodochnoy_colon + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_rektosigmoidnogo_soedineniya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_pryamoy_kishki + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_drugih_organov_pishchevareniya + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_uteri + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_molochnoy_zhel + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_yichnika + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_zhenskih_polovyh_organov + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_predstat_zhelezy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_drugih_muzhskih_polovyh_organov + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_kidney + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_bladder + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Rak_glaza + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_brain + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_thyroid_gland + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.ZNO_Limfomy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Zlokach_immunoprolif_b_ni + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_Multiple_myeloma + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_Leukaemia + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Malignant_neoplasm_lymph_nodes + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Drugie_ZNO_limfoid_i_krovetvor_tkanej + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(insert_title)
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Po_local + smertnost_variables.dvoetotsie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Rak_zheludka + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Rak_legkogo + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Malignant_neoplasm_colon + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Malignant_neoplasm_rectosigmoid + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Rak_pizhevoda + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Rak_predstat_zhelezy + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Malignant_neoplasm_thyroid_gland + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Malignant_neoplasm_Maxillary_sinus + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Malignant_neoplasm_cervix_uteri + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Number_3_4_Neoplasm_short + " " + smertnost_variables.Rak_hepar + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 "-" + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")



smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.VK_about + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

if smertnost_puti.poliklinika:
    smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Zapuzhenaya_stadia + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

if not smertnost_puti.poliklinika:
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Benign_neoplasm + " " + smertnost_variables.total + smertnost_variables.dvoetotsie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Benign_neoplasm + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Benign_neoplasm + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Benign_neoplasm + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(insert_title)
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Tuberculosis + " " + smertnost_variables.total + smertnost_variables.dvoetotsie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Tuberculosis + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Tuberculosis + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Tuberculosis + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.VICH + " " + smertnost_variables.total + smertnost_variables.dvoetotsie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.VICH + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.VICH + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.VICH + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Respiratory + " " + smertnost_variables.total + smertnost_variables.dvoetotsie + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Respiratory + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Respiratory + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Respiratory + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Pneumonia + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Pneumonia + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Pneumonia + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.HOBL + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.HOBL + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.HOBL + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Asthma + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Asthma + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Asthma + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")





smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Digestive + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Digestive + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Digestive + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")




smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Alcohol_pancreatitis + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Alcohol_pancreatitis + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Alcohol_pancreatitis + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")




smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Fibrosis_liver + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Fibrosis_liver + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Fibrosis_liver + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")



if smertnost_puti.poliklinika:
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Krona_disease + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Krona_disease + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Krona_disease + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")



smertnost_begin_sql.cur2.execute(insert_title)



smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Endocrine + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Endocrine + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Endocrine + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")






smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Senility + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Senility + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Senility + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")



smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Mental_disorders + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Mental_disorders + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Mental_disorders + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")




smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Nervous_system + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Nervous_system + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Nervous_system + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")



if smertnost_puti.poliklinika:
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Sided_amiotrophic_sclerosis + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Sided_amiotrophic_sclerosis + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Sided_amiotrophic_sclerosis + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")




smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Musculoskeletal_system + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Musculoskeletal_system + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Musculoskeletal_system + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")





smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Genitourinary_system + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Genitourinary_system + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Genitourinary_system + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")




if smertnost_puti.poliklinika:
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Fe_deficit_anemia + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Fe_deficit_anemia + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Fe_deficit_anemia + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")
  
  
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Diagnoz_ne_opredelen + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Diagnoz_ne_opredelen + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Diagnoz_ne_opredelen + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")





if not smertnost_puti.poliklinika:
  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Outer_causes + " " + str(smertnost_puti.year_prev) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Outer_causes + " " + str(smertnost_puti.year_current) + \
                                 " " + smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")

  smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.Outer_causes + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(insert_title)


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.death_all_cause2 + " " + str(
    smertnost_puti.year_prev) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.death_all_cause2 + " " + str(
    smertnost_puti.year_current) + " " + smertnost_variables.year_point + "'" + ", " + smertnost_puti.nuli_12 + ")")

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod + \
                                 smertnost_variables.death_all_cause2 + " " + smertnost_variables.prirost + " " + \
                                 str(smertnost_puti.year_prev) + " " + smertnost_variables.year_point + \
                                 smertnost_variables.slash + str(smertnost_puti.year_current) + " " + \
                                 smertnost_variables.year_point + "'" + ", " + \
                                 smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod +
                                 smertnost_variables.percent_death_title + "'" + ", " + smertnost_puti.tire_12 + ")")



















