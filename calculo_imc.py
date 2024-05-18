nome = input("Informe o nome do aluno:\n")
peso = str(input("Informe o peso do aluno:\n")).replace(',','.')
altura = str(input("Informe a altura do aluno:\n")).replace(',','.')

peso = float(peso)
altura = float(altura)

imc = (peso) / (altura * altura)
print(f'IMC: {imc:,.2f}.')

if imc >= 40:
    print(f'{nome} tem obesidade grau III - grave.')
elif imc >= 35:
    print(f'{nome} tem obesidade grau II.')
elif imc >= 30:
    print(f'{nome} tem obesidade grau I.')
elif imc >= 25:
    print(f'{nome} está sobrepeso.')
elif imc >= 18.5:
    print(f'{nome} está com peso normal.')
elif imc >= 17:
    print(f'{nome} está abaixo do peso.')
else:
    print(f'{nome} está muito abaixo do peso.')