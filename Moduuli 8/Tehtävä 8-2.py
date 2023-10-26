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
