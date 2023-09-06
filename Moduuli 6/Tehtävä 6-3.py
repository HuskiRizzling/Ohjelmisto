def bg(i):
    return i*3.785

while True:
    n = float(input("Anna gallonien määrä: "))
    if n < 0:
        break
    print("Määrä litroina: ", bg(n))