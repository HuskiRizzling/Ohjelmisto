import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='huskiz',
         autocommit=True
         )


def haeKentät(ICAO):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + ICAO + "' "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos


lk1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
lk2 = input("Anna toisen lentokentän ICAO-koodi: ")

lk1ko = haeKentät(lk1)
lk2ko = haeKentät(lk2)

lk1lat, lk1long = lk1ko
lk2lat, lk2long = lk2ko

dis = distance.great_circle((lk1lat, lk1long),(lk2lat, lk2long)).km

print(f"Lentokenttien välinen etäisyys on {dis: .2f} kilometriä")