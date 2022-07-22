def method_produkt():
    produkte = []

    for i in range (produkte):

        produkte.append(input("Geben Sie ein, was Sie möchten: "))
        teureProdukte = []
        günstigeProdukte = []
        if len(produkte[i])>5:
            teureProdukte.append(produkte[i])
        else:
           günstigeProdukte.append(produkte[i])
        if len(produkte)==10:
            break




    print(produkte)
method_produkt()