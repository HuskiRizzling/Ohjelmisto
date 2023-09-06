def parilliset(i):
    a = []
    for n in i:
        if n % 2 == 0:
            a.append(n)
    return a


kl = [1,2,3,4,5]
print("Alkuperäinen lista: ", kl)
print("Parillisten lukujen lista: ", parilliset(kl))
