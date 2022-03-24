
if __name__ == '__main__':
    import smertnost_puti
    
    """
    if smertnost_puti.poliklinika:
        # если обрабатываем поликлинику, то сначала создаю экселевский
        # файл только с содержащими строками "дом" или "другое место смерти дом", а 
        # уже потом создаем в настройках для переменных то, что если обработка по
        # направлению "поликлиника", то берем экселевский файл не "... для программы",
        # а уже поликлинический эксель.
        from Poliklinika import check_polik_death
    """
    
    import smertnost_from_journal_to_svod



# update "death_pokazateli" set "Наименование: месяц" = 0 where 'Наименование: показатель' = "Пок-тель"
# select * from "death_pokazateli"
# ПРАВИЛЬНО: UPDATE death_svod SET Январь = '1' WHERE Показатель = 'Б-ни нерв. системы прир./уб. 2021 г./2022 г.'
# ПРАВИЛЬНО: SELECT * from "death_svod" where "Показатель" = "Б-ни нерв. системы прир./уб. 2021 г./2022 г."
# где указываем where то надо писать без ковычек иначе не читает название столбца
# UPDATE death_pokazateli SET "Смертность от всех причин, на 1000 населения: 2022" = "0" WHERE "Наименование" = "Янв."
# UPDATE death_pokazateli SET "Наименование" = "Мар." where "Показатель" = "Абс., чел."
# SELECT * from "death_pokazateli" where "Труд2022" = "234"
# UPDATE death_pokazateli SET "Смертность от всех причин, на 1000 населения: 2022" = "0" WHERE "Наименование: месяц" = "Янв."
# select * from death_pokazateli WHERE "Наименование: месяц" = "Янв."




