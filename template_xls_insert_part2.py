
import smertnost_puti
import smertnost_begin_sql
import smertnost_variables


INSERT_to_death_svod_percent = smertnost_variables.INSERT + ' ' + smertnost_variables.INTO + ' ' + \
                         smertnost_variables.table_death_svod_percent + ' ' + smertnost_variables.VALUES + ' ' + '(' + "'"


"""
smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "1', '" +
                                 smertnost_variables.first_place + smertnost_variables.dvoetotsie + " " + smertnost_variables.percent_BSK + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")
"""



smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "1', null, '" +
                                 smertnost_variables.percent_BSK + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "2', null, '" +
                                 smertnost_variables.title_percent_Oncology + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")




smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "3', null, '" +
                                 smertnost_variables.title_percent_Respiratory_system + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")



smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "4', null, '" +
                                 smertnost_variables.title_percent_Endocrine_system + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")



smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "5', null, '" +
                                 smertnost_variables.title_percent_Senility + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")

"""
print(INSERT_to_death_svod_percent + "6', null, '" +
                                 smertnost_variables.title_percent_Mental_disorders + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")
"""

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "6', null, '" +
                                 smertnost_variables.title_percent_Mental_disorders + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "7', null, '" +
                                 smertnost_variables.title_percent_Digestive_system + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "8', null, '" +
                                 smertnost_variables.title_percent_Nervous_system + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "9', null, '" +
                                 smertnost_variables.title_percent_Genitourinary_system + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")


"""

smertnost_begin_sql.cur2.execute(INSERT_to_death_svod_percent + "10', '" +
                                 smertnost_variables.title_percent_Outer_causes + \
                                     "'" + ", " + smertnost_puti.tire_12 + ")")

"""


import Main_percent2












