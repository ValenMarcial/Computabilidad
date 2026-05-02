def enumerar_pares():
    suma = 0
    while True:
        i = 0
        while i <= suma:
            j = suma - i
            yield (i, j)
            i += 1
        suma += 1
