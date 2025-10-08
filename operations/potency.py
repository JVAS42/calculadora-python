def potency(*args):
    if not args:
        return 0
    total = args[0]
    for valor in args[1:]:
        total **= valor
    return total