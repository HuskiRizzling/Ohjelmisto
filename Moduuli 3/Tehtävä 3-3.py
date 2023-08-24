sp = input("Kerro sukupuolesi mies/nainen: ")
hg = int(input("Mikä on hemoglobiiniarvosi (g/l)?: "))
if hg < 134 and sp == "mies" or sp == "Mies":
    print("Hemoglobiiniarvosi on alhainen.")
elif hg > 195 and sp == "mies" or sp == "Mies":
    print("Hemoglobiiniarvosi on korkea.")
elif 134 <= hg <= 195 and sp == "mies" or sp == "Mies":
    print("Hemoglobiiniarvosi on normaali.")
elif hg < 117 and sp == "nainen" or sp == "Nainen":
    print("Hemoglobiiniarvosi on alhainen.")
elif hg > 175 and sp == "nainen" or sp == "Nainen":
    print("Hemoglobiiniarvosi on korkea.")
elif 117 <= hg <= 175 and sp == "nainen" or sp == "Nainen":
    print("Hemoglobiiniarvosi on normaali.")
