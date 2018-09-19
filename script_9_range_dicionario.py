cesta = {"Banana":1.6, "Uva": 2.5}
for fruta in cesta.keys():
    print(fruta)

for fruta,preco in cesta.items():
    print("Fruta: {}, Valor: R${}".format(fruta, preco))
