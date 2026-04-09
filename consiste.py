def consiste(ini: int, fim: int):
    if ini > fim: ini, fim = fim, ini
    num = fim + 1
    erro = True
    while erro:
        try:
            prompt = f"Número no intervalo [{ini} - {fim}]:"
            num = int(input(prompt))
            if ini <= num <= fim: erro = False
        except ValueError: erro = True
        if erro: print("Número errado! Digite novamente!")