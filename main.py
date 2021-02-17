def calculo():
    salario = get_salario()
#INSS
    if (salario <= 1100):
        inss = round(salario * 0.075,2)
    elif (salario <= 2203.48):
        inss = round((salario * 0.09) - 15.67,2)
    elif (salario <= 3305.22):
        inss = round((salario * 0.12) - 82.60,2)
    else:
        inss = round((salario * 0.14) - 148.71,2)

    if (inss < 0):
        inss = 0

#IRPF
    if (salario <= 1903.98):
        irpf = 0
    elif (salario <= 2826.60):
        irpf = round((salario * 0.075) - 142.80,2)
    elif (salario <= 3751.05):
        irpf = round((salario * 0.15) - 354.80,2)
    elif (salario <= 4664.68):
        irpf = round((salario * 0.225) - 636.13,2)
    else:
        irpf = round((salario * 0.275) - 869.36,2)


    if (irpf < 0):
        irpf = 0

    impostos = inss+irpf
    salario_liquido = round(salario - impostos,2)

    print(f'O seu salario bruto é R${salario}')
    print(f'Você paga R${inss} de INSS')
    print(f'Você paga R${irpf} de IRPF')
    print(f'Seu Salario Liquido é R${salario_liquido}')

def get_salario():
    salario = float(input("Qual o seu salario bruto?:"))
    return salario

if (__name__ == "__main__"):
    calculo()
