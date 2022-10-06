def sumarec(numero):
    if numero==1:
        return 1
    else:
        return numero + sumarec(numero-1)

print(sumarec(10))

def factorialrec(numero):
    if numero==1:
        return 1
    else:
        return numero * sumarec(numero-1)

print(factorialrec(4))

