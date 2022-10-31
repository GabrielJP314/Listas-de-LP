def number_phone_br(number):
    """Converte a entrada para um inteiro correspondente ao número de telefone inserido"""
    number = str(number)
    list = ["(", ")", " ", "-", "+55"]
    for i in list:
        number = number.replace(i, "")
    if len(number) < 10:
        number = int("21" + number)
    return int(number)