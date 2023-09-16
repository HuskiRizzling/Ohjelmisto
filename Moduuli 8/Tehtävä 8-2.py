import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='huskiz',
         autocommit=True
         )


def haeLentokentät(maakoodi):
    sql = "SELECT type FROM airport WHERE iso_country = '" + maakoodi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


maakoodi = input("Anna maakoodi: ")
tyypit = haeLentokentät(maakoodi)
c, s, m, l, sea, h, b = 0, 0, 0, 0, 0, 0, 0
for i in tyypit:
    if i[0] == 'closed':
        c += 1
    elif i[0] == 'small_airport':
        s += 1
    elif i[0] == 'medium_airport':
        m += 1
    elif i[0] == 'large_airport':
        l += 1
    elif i[0] == 'seaplane_base':
        sea += 1
    elif i[0] == 'heliport':
        h += 1
    else:
        b += 1
print(f"Suljettuja lentokenttiä: {c}\nPieniä lentokenttiä: {s}\nKeskikokoisia lentokenttiä: {m}\nIsoja lentokenttiä: {l}\nVesistökenttiä: {sea}\nHelikopterikenttiä: {h}\nKuumailmapallokenttiä: {b}")