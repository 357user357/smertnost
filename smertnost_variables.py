
import smertnost_puti


import datetime
from datetime import timedelta
from datetime import date
import time
import re

edge_of_man_age = 60

edge_of_woman_age = 55

lists_woman_birth_death = []

lists_man_birth_death = []

# for_calculation_birth_date_for_death_person = datetime.datetime(1800, 1, 1)


date_today = str(date.today())
# сейчас планирую вычислять возраст не от даты выполнения программы, а
# от даты смерти (пусть даже они в основном будут совпадать так как разность при
# регулярном ежемесячном выполнении программы не превышает получается 1 месяц - зато
# можно потом будет дополнительно убедиться в ранние периоды в правильности сведений)
# наиболее удобно применять дату смерти непосредственно при обработке запроса совместно
# с выгрузком даты рождения и пола.
# Временно все равно буду использовать начало время юникс как отправную в том числе точку
# для расчетов (можно было бы использовать текущую дату но легче ту дату, с которой производится
# подсчет в секундах начиная с нуля)

century_before_unix_begin_datetime = datetime.datetime(1870, 1, 1)

#print(date_today)
p = re.compile(r'(\d+)-(\d+)-(\d+).*')
m = p.findall(date_today)
# печать буквенного начала ячейки
current_year = int(m[0][0])
current_month = int(m[0][1])
current_day = int(m[0][2])
#print(current_month_birth)
current_datetime = datetime.datetime(current_year, current_month, current_day)
#print(current_datetime)
datetime_for_woman_edge_trud = datetime.datetime(current_year - edge_of_woman_age, current_month, current_day)
datetime_for_man_edge_trud = datetime.datetime(current_year - edge_of_man_age, current_month, current_day)
#print(datetime_for_woman_edge_trud)
#print(datetime_for_man_edge_trud)
#quit()

seconds_for_trud__man = 60*(365*24*60*60)

seconds_for_trud__woman = 55*(365*24*60*60)

count_all_trud = 0

# временные переменные в которых хранятся сведения "по нарастающей" с предыдущих месяцев
# обоих годов временные переменные по болезни кровообращения и другим профилям
nuli_month = 0
temp_for_sql = 0
tekushee_kolichestvo_vsego, tekushee_kolichestvo_vsego_prev = 0, 0

Raznost_tekushee_kolichestvo = 0, 0, 0

BSK_vsego_prev, BSK_vsego, Raznost_BSK = 0, 0, 0
# если сведения из ЗАГС поступили то for_update_only_current_month не равно нулю
for_update_only_current_month = 0

outer_month = ""
update_or_not = []

BSK = "БСК"

OIM_vsego_prev, OIM_vsego, Raznost_OIM = 0, 0, 0
OIM = "ОИМ"

ONMK_vsego_prev, ONMK_vsego, Raznost_ONMK = 0, 0, 0
ONMK = "ОНМК"

IBS_vsego_prev, IBS_vsego, Raznost_IBS = 0, 0, 0
IBS = "ИБС"

GB_vsego_prev, GB_vsego, Raznost_GB = 0, 0, 0
GB = "ГБ"

TSA_vsego_prev, TSA_vsego, Raznost_TSA = 0, 0, 0
TSA = "Церебр. атероск-з"

P_ONMK_vsego_prev, P_ONMK_vsego, Raznost_P_ONMK = 0, 0, 0
P_ONMK = "Послед. ОНМК"

Polik_Arterii_arterioli_kapilary_vsego_prev, Polik_Arterii_arterioli_kapilary_vsego, Raznost_Polik_Arterii_arterioli_kapilary = 0, 0, 0
Polik_Arterii_arterioli_kapilary = "Б-ни арт-й, арт-л и к."

ZNO_vsego_prev, ZNO_vsego, Raznost_ZNO = 0, 0, 0
ZNO = "ЗНО"

Rak_nosa_vsego = 0
Rak_nosa = "Рак носа и среднего уха"

Rak_pizhevoda_vsego = 0
Rak_pizhevoda = "Рак пищевода"

Rak_zheludka_vsego = 0
Rak_zheludka = "Рак желудка"

Rak_pryamoy_kishki_vsego = 0
Rak_pryamoy_kishki = "Рак прямой кишки"

Rak_legkogo_vsego = 0
Rak_legkogo = "Рак легкого"

Rak_soed_tkaney_vsego = 0
Rak_soed_tkaney = "Рак костей, хрящей и соед. тканей"

Rak_molochnoy_zhel_vsego = 0
Rak_molochnoy_zhel = "Рак молоч. железы"

Rak_hepar_vsego = 0
Rak_hepar = "Рак печени"

Rak_zhelchnogo_protoka_vsego = 0
Rak_zhelchnogo_protoka = "Рак желч. протока"

Malignant_neoplasm_obodochnoy_colon_vsego = 0
Malignant_neoplasm_obodochnoy_colon = "Рак обод. кишки"

Rak_podzheludochnoy_zhelezy_vsego = 0
Rak_podzheludochnoy_zhelezy = "Рак поджел. железы"

Malignant_neoplasm_uteri_vsego = 0
Malignant_neoplasm_uteri = "Рак матки"

Rak_yichnika_vsego = 0
Rak_yichnika = "Рак яичника"

Rak_predstat_zhelezy_vsego = 0
Rak_predstat_zhelezy = "Рак предстат. железы"

Malignant_neoplasm_kidney_vsego = 0
Malignant_neoplasm_kidney = "Рак почки"

Malignant_neoplasm_bladder_vsego = 0
Malignant_neoplasm_bladder = "Рак других мочевых органов"

Malignant_neoplasm_brain_vsego = 0
Malignant_neoplasm_brain = "Рак нервной системы"

Malignant_neoplasm_thyroid_gland_vsego = 0
Malignant_neoplasm_thyroid_gland = "Рак эндокринных желез"

Malignant_neoplasm_Multiple_myeloma_vsego = 0
Malignant_neoplasm_Multiple_myeloma = "Миелома и плазмокл. ЗНО"

Malignant_neoplasm_Leukaemia_vsego = 0
Malignant_neoplasm_Leukaemia = "ЗНО Лейкоз"

Malignant_neoplasm_lymph_nodes_vsego = 0
Malignant_neoplasm_lymph_nodes = "Рак вторичных и неуточнен. лок-ций"


Benign_neoplasm_vsego_prev, Benign_neoplasm_vsego, Raznost_Benign_neoplasm = 0, 0, 0
Benign_neoplasm = "Добр. новообр-я"

sql_Benign_neoplasm = "D%"


Fe_deficit_anemia_vsego_prev, Fe_deficit_anemia_vsego, Raznost_Fe_deficit_anemia = 0, 0, 0
Fe_deficit_anemia = "ЖДА"

sql_Fe_deficit_anemia = "D50%"


Diagnoz_ne_opredelen_vsego_prev, Diagnoz_ne_opredelen_vsego, Raznost_Diagnoz_ne_opredelen = 0, 0, 0
Diagnoz_ne_opredelen = "ДНО"

sql_Diagnoz_ne_opredelen = ""


Tuberculosis_vsego_prev, Tuberculosis_vsego, Raznost_Tuberculosis = 0, 0, 0
Tuberculosis = "Тубер-з"

VICH_vsego_prev, VICH_vsego, Raznost_VICH = 0, 0, 0
VICH = "ВИЧ"


Respiratory_vsego_prev, Respiratory_vsego, Raznost_Respiratory = 0, 0, 0
Respiratory = "Орг. дыхания"

Pneumonia_vsego_prev, Pneumonia_vsego, Raznost_Pneumonia = 0, 0, 0
Pneumonia = "Пневм."

sql_Pneumonia = ["J12%", "J13%", "J14%", "J15%", "J16%", "J17%", "J18%"]

HOBL_vsego_prev, HOBL_vsego, Raznost_HOBL = 0, 0, 0
HOBL = "ХОБЛ"

sql_HOBL = "J44%"


Asthma_vsego_prev, Asthma_vsego, Raznost_Asthma = 0, 0, 0
Asthma = "Бронх. астма"

sql_Asthma = ["J45%", "J46%"]


Digestive_vsego_prev, Digestive_vsego, Raznost_Digestive = 0, 0, 0
Digestive = "Забол. ЖКТ"

sql_Digestive = "K%"


Alcohol_pancreatitis_vsego_prev, Alcohol_pancreatitis_vsego, Raznost_Alcohol_pancreatitis = 0, 0, 0
Alcohol_pancreatitis = "Хрон. алк. панкр-т"

sql_Alcohol_pancreatitis = "K86.0%"


Fibrosis_liver_vsego_prev, Fibrosis_liver_vsego, Raznost_Fibrosis_liver = 0, 0, 0
Fibrosis_liver = "Цирроз печени"

sql_Fibrosis_liver = "K74%"



Krona_disease_vsego_prev, Krona_disease_vsego, Raznost_Krona_disease = 0, 0, 0
Krona_disease = "Б-нь Крона"

sql_Krona_disease = "K50%"



Endocrine_vsego_prev, Endocrine_vsego, Raznost_Endocrine = 0, 0, 0
Endocrine = "Б-ни эндокр. сист."

sql_Endocrine = "E%"




Senility_vsego_prev, Senility_vsego, Raznost_Senility = 0, 0, 0
Senility = "Смерт. от старости"

sql_Senility = "R54%"




Mental_disorders_vsego_prev, Mental_disorders_vsego, Raznost_Mental_disorders = 0, 0, 0
Mental_disorders = "Психич. забол-я"

sql_Mental_disorders = "F%"




Nervous_system_vsego_prev, Nervous_system_vsego, Raznost_Nervous_system = 0, 0, 0
Nervous_system = "Б-ни нерв. системы"

sql_Nervous_system = "G%"




Sided_amiotrophic_sclerosis_vsego_prev, Sided_amiotrophic_sclerosis_vsego, Raznost_Sided_amiotrophic_sclerosis = 0, 0, 0
Sided_amiotrophic_sclerosis = "Бок. амиотроф. склероз"

sql_Sided_amiotrophic_sclerosis = "G12.2%"




Musculoskeletal_system_vsego_prev, Musculoskeletal_system_vsego, Raznost_Musculoskeletal_system = 0, 0, 0
Musculoskeletal_system = "Остеопороз М"

sql_Musculoskeletal_system = "M%"


Genitourinary_system_vsego_prev, Genitourinary_system_vsego, Raznost_Genitourinary_system = 0, 0, 0
Genitourinary_system = "ХПН (б-ни почек)"

sql_Genitourinary_system = "N%"


Outer_causes_vsego_prev, Outer_causes_vsego, Raznost_Outer_causes = 0, 0, 0
Outer_causes = "Внеш. причины"

# старая версия "Внешних причин":
"""
sql_Outer_causes = ["A15%", "A16%", "A17%",         "A18%", "A19%",         "B20%", "B21%", "B22%",      "B23%", "B24%", \
                        "C%", "D%", "E%", "F%", "G%", "I%", "J%", "K%", "M%", "N%", "R54%"]
"""

sql_Outer_causes = [ "S%", "T%", "V%",          "W%", "X%", "Y%",       "U%" ]


Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH_vsego = 0
Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH = "Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ"
# МКБ A10-A14, B28, B29 не существует
sql_Infekc_i_parazitar_b_ni_krome_tub_za_i_VICH = ["A0%", "A2%", "A3%",         "A4%", "A5%", "A6%",        "A7%", "A8%", "A9%",    \
                                                        "B0%", "B25%", "B26%",          "B27%", "B3%", "B4%",           \
                                                        "B5%", "B6%", "B7%",        "B8%", "B9%" ]


Travmy_golovy_vsego = 0
Travmy_golovy = "Травмы головы"
# МКБ A10-A14, B28, B29 не существует
sql_Travmy_golovy = ["S0%" ]

Travmy_shei_vsego = 0
Travmy_shei = "Травмы шеи"
sql_Travmy_shei = ["S1%" ]

Travmy_grudnoj_kletki_vsego = 0
Travmy_grudnoj_kletki = "Травмы грудной клетки"
sql_Travmy_grudnoj_kletki = ["S2%" ]

Travmy_zhivota_nizhnej_chasti_spiny_i_taza_vsego = 0
Travmy_zhivota_nizhnej_chasti_spiny_i_taza = "Травмы живота, нижней части спины и таза"
sql_Travmy_zhivota_nizhnej_chasti_spiny_i_taza = ["S3%" ]

Travmy_plechevogo_poyasa_i_plecha_vsego = 0
Travmy_plechevogo_poyasa_i_plecha = "Травмы плечевого пояса и плеча"
sql_Travmy_plechevogo_poyasa_i_plecha = ["S4%" ]

Travmy_loktya_i_predplechya_vsego = 0
Travmy_loktya_i_predplechya = "Травмы локтя и предплечья"
sql_Travmy_loktya_i_predplechya = ["S5%" ]

Travmy_zapyastya_i_kisti_vsego = 0
Travmy_zapyastya_i_kisti = "Травмы запястья и кисти"
sql_Travmy_zapyastya_i_kisti = ["S6%" ]

Travmy_tazobedr_sustava_i_bedra_vsego = 0
Travmy_tazobedr_sustava_i_bedra = "Травмы тазобедр. сустава и бедра"
sql_Travmy_tazobedr_sustava_i_bedra = ["S7%" ]


Travmy_kolena_i_goleni_vsego = 0
Travmy_kolena_i_goleni = "Травмы колена и голени"
sql_Travmy_kolena_i_goleni = ["S8%" ]


Travmy_golenostop_sustava_i_stopy_vsego = 0
Travmy_golenostop_sustava_i_stopy = "Травмы голеностоп. сустава и стопы"
sql_Travmy_golenostop_sustava_i_stopy = ["S9%" ]



Travmy_zahvat_neskolko_oblastej_tela_vsego = 0
Travmy_zahvat_neskolko_oblastej_tela = "Травмы, захват. несколько областей тела"
sql_Travmy_zahvat_neskolko_oblastej_tela = ["T00%", "T01%", "T02%",         "T03%", "T04%", "T05%",         "T06%", "T07%" ]

Travmy_neutoch_chasti_tela_vsego = 0
Travmy_neutoch_chasti_tela = "Травмы неуточн. части тела"
sql_Travmy_neutoch_chasti_tela = ["T08%", "T09%", "T10%",       "T11%", "T12%", "T13%",         "T14%" ]

Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya_vsego = 0
Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya = "Послед. прон. ин. тела ч-з ест-ые отв-я"
sql_Posledstviya_pronikn_inorod_tela_cherez_estestv_e_otverstiya = ["T15%", "T16%", "T17%",         "T18%", "T19%" ]

Termicheskie_i_himicheskie_ozhogi_vsego = 0
Termicheskie_i_himicheskie_ozhogi = "Термические и химические ожоги"
sql_Termicheskie_i_himicheskie_ozhogi = ["T2%", "T30%", "T31%", 		"T32%" ]

Otmorozhenie_vsego = 0
Otmorozhenie = "Отморожение"
sql_Otmorozhenie = [ "T33%", "T34%", "T35%" ]

Otr_lek_sr_med_i_biol_v_mi_vsego = 0
Otr_lek_sr_med_i_biol_v_mi = "Отр. лек. ср., мед. и биол. в-ми"
sql_Otr_lek_sr_med_i_biol_v_mi = [ "T36%", "T37%", "T38%", 		"T39%", "T4%", "T50%" ]

Toks_d_e_v_v_preim_nemed_nazn_ya_vsego = 0
Toks_d_e_v_v_preim_nemed_nazn_ya = "Токс. д-е в-в, преим. немед. назн-я"
sql_Toks_d_e_v_v_preim_nemed_nazn_ya = [ "T51%", "T52%", "T53%", 		"T54%", "T55%", "T56%", 		"T57%", "T58%", "T59%", 	\
                                           "T60%", "T61%", "T62%", 		"T63%", "T64%", "T65%" ]

Dr_i_neut_eff_vozd_ya_vnesh_prichin_vsego = 0
Dr_i_neut_eff_vozd_ya_vnesh_prichin = "Др. и неут. эфф. возд-я внеш. причин"
sql_Dr_i_neut_eff_vozd_ya_vnesh_prichin = [ "T66%", "T67%", "T68%", 		"T69%", "T70%", "T71%", 		\
                                                 "T73%", "T74%", "T75%", 		"T76%", "T78%" ]

Nek_e_rannie_oslozh_travmy_vsego = 0
Nek_e_rannie_oslozh_travmy = "Осл. травмы, тер. и хир. вмеш-в не кл. в др. р."
sql_Nek_e_rannie_oslozh_travmy = [ "T79%", "T8%" ]

Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n_vsego = 0
Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n = "Послед-я травм, отр-й и др. возд-й внеш. пр-н"
sql_Posled_ya_travm_otr_j_i_dr_vozd_j_vnesh_pr_n = [ "T9%" ]

Transportnye_neschastnye_sluchai_vsego = 0
Transportnye_neschastnye_sluchai = "Транспортные несчастные случаи"
sql_Transportnye_neschastnye_sluchai = [ "V%" ]

Dr_vn_prich_travm_pri_nesch_sl_h_vsego = 0
Dr_vn_prich_travm_pri_nesch_sl_h = "Др. вн. прич. травм при несч. сл-х"
sql_Dr_vn_prich_travm_pri_nesch_sl_h = [ "W%", "X0%", "X1%",        "X2%", "X3%", "X4%",        "X5%" ]

Prednamerennoe_samopovrezhdenie_vsego = 0
Prednamerennoe_samopovrezhdenie = "Предн. самоповр., напад., повр. с неопр. нам."
sql_Prednamerennoe_samopovrezhdenie = [ "X6%", "X7%", "X8%", 		"X9%", "Y0%", "Y1%", 		\
                                               "Y2%", "Y30%", "Y31%", 		"Y32%", "Y33%", "Y34%" ]

D_ya_predusm_zakonom_i_voen_op_i_vsego = 0
D_ya_predusm_zakonom_i_voen_op_i = "Д-я, предусм. законом, и воен. оп-и"
sql_D_ya_predusm_zakonom_i_voen_op_i = [ "Y35%", "Y36%" ]

Osl_ter_i_hir_vm_v_vsego = 0
Osl_ter_i_hir_vm_v = "Осл. тер. и хир. вм-в"
sql_Osl_ter_i_hir_vm_v = [ "Y4%", "Y5%", "Y6%", 		"Y7%", "Y80%", "Y81%", 		\
                                                "Y82%", "Y83%", "Y84%" ]

Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i_vsego = 0
Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i = "Посл. воз-я внеш. пр-н заб-ти и см-и"
sql_Posl_voz_ya_vnesh_pr_n_zab_ti_i_sm_i = [ "Y85%", "Y86%", "Y87%",        "Y88%", "Y89%" ]

Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r_vsego = 0
Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r = "Доп. ф., им. от. к прич. заб. и см., кл. в др. р."
sql_Dop_f_ry_im_ot_e_k_prich_zab_i_sm_kl_v_dr_r = [ "Y9%" ]

COVID_dr_kody_dlya_osobyh_celej_vsego = 0
COVID_dr_kody_dlya_osobyh_celej = "COVID, др. коды для особых целей"
sql_COVID_dr_kody_dlya_osobyh_celej = [ "U%" ]


############## ТАК КАК ВНЕШНИЕ ПРИЧИНЫ ИСКЛЮЧАЮТСЯ ТО ДО 100% НАДО ОТДЕЛЬНОЙ СТРОКОЙ ПОЛУЧАЕТСЯ УКАЗЫВАТЬ ВИЧ, 
############## ТУБЕРКУЛЕЗ, ДОБРОКАЧ. Н-Я, ОПОРНО-ДВИГАТЕЛЬНЫЙ АППАРАТ И СТАРОСТЬ : ВСЕГО 5 РУБРИК 
# ТАКЖЕ ПОМИМО УКАЗАНИЙ НА ПРОЦЕНТ - СТОИЛО БЫ РАСПРЕДЕЛЯТЬ ПО УДЕЛЬНОМУ ПРОЦЕНТУ - ЕСЛИ НАЙДУ РЕГИОНАЛЬНЫЙ ПРОЦЕНТ ТО УКАЗАТЬ ЕГО ПОТОМ


"""
(A00-B99)		Все что не включает туберкулез 5 мкбешек минус 5 мкбешек по вич
["A15%", "A16%", "A17%",         "A18%", "A19%",         "B20%", "B21%", "B22%",        "B23%", "B24% ] 
Инфекц. и паразитар. б-ни кроме туб-за и ВИЧ

Болезни глаз и уха:

VII Болезни глаза и его придаточного аппарата
(H00-H59)
VIII    Болезни уха и сосцевидного отростка
(H60-H95)

XII Болезни кожи и подкожной клетчатки
(L00-L99)

XV  Беременность, роды и послеродовой период
(O00-O99)

XVI Отдельные состояния, возникающие в перинатальном периоде
(P00-P96)

XVII    Врожденные аномалии [пороки развития], деформации и хромосомные нарушения
(Q00-Q99)




XIX Травмы, отравления и некоторые другие последствия воздействия внешних причин
(S00-T98)

S00-S09 Травмы головы
S10-S19 Травмы шеи
S20-S29 Травмы грудной клетки
S30-S39 Травмы живота, нижней части спины, поясничного отдела позвоночника и таза
S40-S49 Травмы плечевого пояса и плеча
S50-S59 Травмы локтя и предплечья
S60-S69 Травмы запястья и кисти
S70-S79 Травмы области тазобедренного сустава и бедра
S80-S89 Травмы колена и голени
S90-S99 Травмы области голеностопного сустава и стопы


T00-T07 Травмы, захватывающие несколько областей тела
T08-T14 Травмы неуточненной части туловища, конечности или области тела
T15-T19 Последствия проникновения инородного тела через естественные отверстия
T20-T32 Термические и химические ожоги
T33-T35 Отморожение
T36-T50 Отравления лекарственными средствами, медикаментами и биологическими веществами
T51-T65 Токсическое действие веществ, преимущественно немедицинского назначения
T66-T78 Другие и неуточненные эффекты воздействия внешних причин
T79-T79 Некоторые ранние осложнения травмы
T80-T88 Осложнения хирургических и терапевтических вмешательств, не классифицированные в других рубриках
T90-T98 Последствия травм, отравлений и других воздействий внешних причин

XX  Внешние причины заболеваемости и смертности
(V01-Y98) :

V01-V99 — Транспортные несчастные случаи
W00-X59 — Другие внешние причины травм при несчастных случаях
X60-X84 — Преднамеренное самоповреждение
X85-Y09 — Нападение
Y10-Y34 — Повреждение с неопределенными намерениями
Y35-Y36 — Действия, предусмотренные законом, и военные операции
Y40-Y84 — Осложнения терапевтических и хирургических вмешательств
Y85-Y89 — Последствия воздействия внешних причин заболеваемости и смертности
Y90-Y98 — Дополнительные факторы, имеющие отношение к причинам заболеваемости и смертности, классифицированным в других рубриках


COVID и другие коды для особых целей:

XXII    Коды для особых целей
(U00-U85)

"""


percent_death_title = "Стр. пок-лей смер. (уд. вес от всех причин %)"

first_place = "Первое место"
second_place = "Второе место"
third_place = "Третье место"
place_4 = "Четвертое место"
place_5 = "Пятое место"
place_6 = "Шестое место"
place_7 = "Седьмое место"
place_8 = "Восьмое место"
place_9 = "Девятое место"

place_10 = "Десятое место"
place_11 = "Одиннадцатое место"
place_12 = "Двенадцатое место"
place_13 = "Тринадцатое место"
place_14 = "Четырнадцатое место"



percent_BSK_vsego_prev, percent_BSK_vsego = 0, 0
percent_BSK = "БСК 36%"

Benign_Oncology_vsego = 0
ZNO_Oncology_vsego = 0

Oncology_vsego = 0
percent_Oncology_vsego = 0
title_percent_Oncology = "Онко. 15,6%"

Respiratory_system_vsego = 0
percent_Respiratory_system_vsego = 0
title_percent_Respiratory_system = "ДС 6%"


Endocrine_system_vsego = 0
percent_Endocrine_system_vsego = 0
if smertnost_puti.poliklinika:
    title_percent_Endocrine_system = "энд. 5%"
else:
    title_percent_Endocrine_system = "энд. 1,7%"


Senility_vsego = 0
percent_Senility_vsego = 0
title_percent_Senility = "старость 3,5%"


Mental_disorders_vsego = 0
percent_Mental_disorders_vsego = 0
#print("pre title_percent_Mental_disorders")
if smertnost_puti.poliklinika:
    #print("poliklinika title_percent_Mental_disorders")
    title_percent_Mental_disorders = "псих. 3%"
else:
    title_percent_Mental_disorders = "псих. 3,1%"

#print("title_percent_Mental_disorders =  " + title_percent_Mental_disorders)

Digestive_system_vsego = 0
percent_Digestive_system_vsego = 0
title_percent_Digestive_system = "пищ. 6%"


Nervous_system_vsego = 0
percent_Nervous_system_vsego = 0
title_percent_Nervous_system = "ЦНС 1,7%"


Genitourinary_system_vsego = 0
percent_Genitourinary_system_vsego = 0
title_percent_Genitourinary_system = "МПС 0,4%"


Outer_causes_vsego = 0
percent_Outer_causes_vsego = 0
title_percent_Outer_causes = "Внеш. причины"

before_this_month_do_sort = ""

array_nosology_for_sort_month = {}

which_next_month_or_cur_december = ""

total = "всего"
Total = "Всего"

year_point = 'г.'
point = "."
star = "*"
slash = "/"
dvoetotsie = ":"

zero = "0"

CREATE = "CREATE"
TABLE = "TABLE"
AND = "AND"
count_row = "count(" + star + ")"
FROM = "FROM"
INSERT = "INSERT"
INTO = "INTO"
LIKE = "LIKE"
NOT = "NOT"
OR = "OR"
SELECT = "SELECT"
SET = "SET"
UPDATE = "UPDATE"
VALUES = "VALUES"
WHERE = "WHERE"

table_death_prev = "death_prev"
table_death_cur = "death"
table_death_svod = "death_svod"
table_death_svod_percent = "death_svod_percent"
table_death_pokazateli = "death_pokazateli"


column_period_po_zags = "Период по ЗАГС"


column_date_birth = "Дата рождения"
column_date_death = "Дата смерти"
column_gender = "Пол"


column_pokazalel = "Показатель"
column_cause_death = "Причина смерти"
column_name_month = "Наименование: месяц"


title_death_all_cause_1000_human = "Смертность от всех причин, на 1000 населения"
title_death_all_cause_1000_human_dvoetotsie_year_cur = title_death_all_cause_1000_human + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_all_cause_1000_human_dvoetotsie_year_prev = title_death_all_cause_1000_human + dvoetotsie + " " + str(smertnost_puti.year_prev)

column_name_1000_relative = title_death_all_cause_1000_human

column_name_trud = "Смертность в трудоспособном возрасте, на 100000 населения"
column_name_trud_dvoetotsie_year_cur = column_name_trud + dvoetotsie + " " + str(smertnost_puti.year_current)
column_name_trud_dvoetotsie_year_prev = column_name_trud + dvoetotsie + " " + str(smertnost_puti.year_prev)

column_name_pokazatel = "Наименование: показатель"
column_name_pokazatal_month = "Наименование: месяц"


title_death_trud_100_000_human = "Смертность в трудоспособном возрасте, на 100000 населения"
title_death_trud_100_000_human_year_cur = title_death_trud_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_trud_100_000_human_year_prev = title_death_trud_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_prev)
title_death_BSK_100_000_human = "Смертность от болезней системы кровообращения, на 100000 населения"
title_death_BSK_100_000_human_year_cur = title_death_BSK_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_BSK_100_000_human_year_prev = title_death_BSK_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_prev)
title_death_Onco_100_000_human = "Смертность от новообразований, на 100000 населения"
title_death_Onco_100_000_human_year_cur = title_death_Onco_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_Onco_100_000_human_year_prev = title_death_Onco_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_prev)
DTP = "ДТП"
sql_DTP = "V%"
calc_100000_DTP_human = 0
title_death_DTP_100_000_human = "Смертность от ДТП, на 100000 населения"
title_death_DTP_100_000_human_year_cur = title_death_DTP_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_DTP_100_000_human_year_prev = title_death_DTP_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_prev)


calc_100000_tuberculosis_human = 0

title_death_Tuber_100_000_human = "Смертность от туберкулеза, на 100000 населения"
title_death_Tuber_100_000_human_year_cur = title_death_Tuber_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_Tuber_100_000_human_year_prev = title_death_Tuber_100_000_human + dvoetotsie + " " + str(smertnost_puti.year_prev)
title_death_Child = "Младенческая смертность"
title_death_Child_year_cur = title_death_Child + dvoetotsie + " " + str(smertnost_puti.year_current)
title_death_Child_year_prev = title_death_Child + dvoetotsie + " " + str(smertnost_puti.year_prev)



death_all_cause = "Умерло от всех причин"
death_all_cause2 = "От всех причин"
VK_about_death = "Провед. ВК по пов. смерти от"
VK_about = "Проведено ВК"
Zapuzhenaya_stadia = "Кол-во выяв. б-х в запущ. ст./д-з уст. на вскр."
Po_local = "По локализации"
Number_3_4_Neoplasm = "Кол-во выяв. б-ных 3-4 ст. ЗНО"
Number_3_4_Neoplasm_short = "3-4 ст."
Malignant_neoplasm_colon = "Рак кишечника"
Malignant_neoplasm_rectosigmoid = "Рак сигмы"
Malignant_neoplasm_Fibrosarkoma = "Фибросаркома"
Malignant_neoplasm_Maxillary_sinus = "Рак в/чел пазухи"
Malignant_neoplasm_cervix_uteri = "Рак шейки матки"

prirost = "прир./уб."
v_tom_tsisle = "в т.ч."


sql_Tuberculosis = ["A15%", "A16%", "A17%", "A18%", "A19%"]
sql_BSK = "I%"
sql_GB = ["I10%", "I11%", "I12%", "I13%", "I14%", "I15%"]
sql_OIM = ["I21%", "I22%"]
sql_IBS = ["I20%", "I21%", "I22%", "I23%", "I24%", "I25%"]
sql_ONMK = ["I60%", "I61%", "I62%", "I63%", "I64%"]
sql_TSereb_ater_z = ["I67.2%", "I67.8%"]
sql_P_ONMK = "I69%"

sql_Polik_Arterii_arterioli_kapilary = "I7%"

sql_Onko = "C%"

# C00-C14 Губы, полости рта и глотки
ZNO_Guby_polosti_rta_i_glotki_vsego = 0
ZNO_Guby_polosti_rta_i_glotki = "Рак губы, полости рта и глотки"
sql_ZNO_Guby_polosti_rta_i_glotki = ["C0%", "C10%", "C11%", "C12%", "C13%", "C14%"]
sql_Rak_pizhevoda = "C15%"
sql_Rak_zheludka = "C16%"
#ZNO_Drugie_ZNO_obodochnoj_kishki_vsego = 0
#ZNO_Drugie_ZNO_obodochnoj_kishki = "Другое ЗНО ободочной кишки"
#sql_ZNO_Drugie_ZNO_obodochnoj_kishki = ["C18.0%", "C18.1%", "C18.3%", "C18.5%", "C18.7%", "C18.8%"]
# не все C18 указаны ранее - исправил чтобы все отображались
#sql_Malignant_neoplasm_obodochnoy_colon = ["C18.2%", "C18.4%", "C18.6%", "C18.9%"]
Rak_tonkogo_kishechnika_vsego = 0
Rak_tonkogo_kishechnika = "Рак тонкого кишечника"
sql_Rak_tonkogo_kishechnika = ["C17%"]
sql_Malignant_neoplasm_obodochnoy_colon = ["C18%"]
Rak_rektosigmoidnogo_soedineniya_vsego = 0
Rak_rektosigmoidnogo_soedineniya = "Рак ректосигмоидного соединения"
sql_Rak_rektosigmoidnogo_soedineniya = ["C19%"]
sql_Rak_pryamoy_kishki = ["C20%", "C21%"]
sql_Rak_hepar = "C22%"
Rak_zhelchnogo_puzyrya_vsego = 0
Rak_zhelchnogo_puzyrya = "Рак желчного пузыря"
sql_Rak_zhelchnogo_puzyrya = ["C23%"]
sql_Rak_zhelchnogo_protoka = "C24%"
sql_Rak_podzheludochnoy_zhelezy = "C25%"
Rak_drugih_organov_pishchevareniya_vsego = 0
Rak_drugih_organov_pishchevareniya = "Рак других органов пищеварения"
sql_Rak_drugih_organov_pishchevareniya = ["C26%"]

# C27-C29 отсутствуют в мкб

# не все C30 указаны
#sql_Rak_nosa = "C30.0%"
sql_Rak_nosa = "C30%"
Rak_pridatochnyh_pazuh_gortani_i_trahei_vsego = 0
Rak_pridatochnyh_pazuh_gortani_i_trahei = "Рак придаточных пазух, гортани и трахеи"
sql_Rak_pridatochnyh_pazuh_gortani_i_trahei = ["C31%", "C32%", "C33%"]
sql_Rak_legkogo = "C34%"

# C35-36 отсутствуют в мкб

Rak_drugih_organov_dyhaniya_vsego = 0
Rak_drugih_organov_dyhaniya = "Рак других органов дыхания"
sql_Rak_drugih_organov_dyhaniya = ["C37%", "C38%", "C39%"]

# C42 отсутствуют в мкб

sql_Rak_soed_tkaney = ["C40%", "C41%", "C43%",       "C45%", "C46%", "C47%",         "C48%", "C49%"]
sql_Rak_molochnoy_zhel = "C50%"

Rak_zhenskih_polovyh_organov_vsego = 0
Rak_zhenskih_polovyh_organov = "Рак других женских половых органов"
# C53-C56 идут отдельными рубриками
sql_Rak_zhenskih_polovyh_organov = ["C51%", "C52%",             "C57%", "C58%"]
sql_Malignant_neoplasm_uteri = ["C53%", "C54%", "C55%"]
sql_Rak_yichnika = "C56%"

# C59 отсутствуют в мкб

# C60 будет далее
sql_Rak_predstat_zhelezy = "C61%"
Rak_drugih_muzhskih_polovyh_organov_vsego = 0
Rak_drugih_muzhskih_polovyh_organov = "Рак других мужских половых органов"
sql_Rak_drugih_muzhskih_polovyh_organov = ["C60%", "C62%", "C63%"]
sql_Malignant_neoplasm_kidney = ["C64%", "C65%"]
sql_Malignant_neoplasm_bladder = ["C66%", "C67%", "C68%"]
Rak_glaza_vsego = 0
Rak_glaza = "Рак глаза"
sql_Rak_glaza = ["C69%"]
sql_Malignant_neoplasm_brain = ["C70%", "C71%", "C72%"]
sql_Malignant_neoplasm_thyroid_gland = ["C73%", "C74%", "C75%"]
sql_Malignant_neoplasm_lymph_nodes = ["C76%", "C77%", "C78%",       "C79%", "C80%"]
# Лимфома C81-C86
ZNO_Limfomy_vsego = 0
ZNO_Limfomy = "Лимфомы"
sql_ZNO_Limfomy = ["C81%", "C82%", "C83%",        "C84%", "C85%", "C86%"]

# C87 отсутствуют в мкб

# C88 Злокач. иммунопролиф. б-ни
Zlokach_immunoprolif_b_ni_vsego = 0
Zlokach_immunoprolif_b_ni = "Злокач. иммунопролиф. б-ни"
sql_Zlokach_immunoprolif_b_ni = ["C88%"]

# C89 отсутствуют в мкб

sql_Malignant_neoplasm_Multiple_myeloma = "C90%"
sql_Malignant_neoplasm_Leukaemia = ["C91%", "C92%", "C93%",         "C94%", "C95%"]


# C96 Другие ЗНО лимфоид. и кроветвор. тканей
Drugie_ZNO_limfoid_i_krovetvor_tkanej_vsego = 0
Drugie_ZNO_limfoid_i_krovetvor_tkanej = "Другие ЗНО лимфоид. и кроветвор. тканей"
sql_Drugie_ZNO_limfoid_i_krovetvor_tkanej = ["C96%"]


sql_VICH = ["B20%", "B21%", "B22%", "B23%", "B24%"]
sql_Respiratory = "J%"

select_cur_month_total = []

check = [] 

tire = "-"


pokazatel_short = "Пок-тель"

abs_human = "Абс., чел."

period_month_name = "Период: месяц"  # это старые записи?

period_pokazatel_name = "Период: показатель"  # это старые записи?


calc_1000_human = 0

calc_100000_bsk_human = 0

calc_100000_onco_human = 0

