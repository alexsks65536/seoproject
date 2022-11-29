import sqlite3


def generate_data(counter: int):
    con = sqlite3.connect('db.sqlite3')
    con.execute('DELETE FROM mainapp_company')
    for el in range(1, counter):
        con.execute(f"INSERT INTO mainapp_company (name, description, services, rating, stars, photo, slug, time_create) "
                    f"VALUES ("
                    f"'Клиника № {el}', 'Тест', 'Тест', 1, 2, 'photo.jpg', 'url{el}.ru', '2022-11-20')")
    return con.commit()


generate_data(15)




