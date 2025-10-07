def division(*args):
    values = args
    division = 0
    for value in range (0, len(values)):
        if value == 0:
            division = values[value]
        else:
            division /= values[value]
    return division
