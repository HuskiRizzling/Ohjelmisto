leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))
mg = ((leiviska*20*32+naula*32+luoti)*13.3)%1000
mk = (((leiviska*20*32+naula*32+luoti)*13.3)-mg)/1000
print(f"{mk:.0f} kiloa ja", f"{mg:.2f} grammaa")