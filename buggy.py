def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')


buggy('b')  # Se esperaría ['b']