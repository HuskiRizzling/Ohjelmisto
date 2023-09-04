kl = int(input("Anna kokonaisluku: "))

if kl == 1:
    print("Luku ei ole alkuluku")
elif kl > 1:
    for i in range(2, kl):
        if kl % i == 0:
            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
