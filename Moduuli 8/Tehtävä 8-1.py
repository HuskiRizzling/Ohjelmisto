import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='huskiz',
         autocommit=True
         )

def haeLentokenttäICAOlla(ICAO):
    sql = "SELECT name, iso_region FROM airport WHERE ident = '" + ICAO + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for i in tulos:
            print(f"Lentokentän nimi on {i[0]} ja sen sijaintikunta on {i[1]}")

ICAO = input("Anna ICAO-koodi: ")
haeLentokenttäICAOlla(ICAO)