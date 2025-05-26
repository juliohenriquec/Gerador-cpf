import sys
cpf = input('Digite o cpf: ').replace('.', '-').replace('-', '')

entrada_repetida = cpf == cpf[0] * len(cpf)
if entrada_repetida:
    print('cpf invalido')
    sys.exit()

contador_regressivo_1 = 10
resultado_digito_1 = 0
nove_digitos = cpf[0:9]
for digito_1 in range(0,9):
    resultado_digito_1 += int(cpf[digito_1]) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

if digito_1 > 9:
    resultado = 0
else:
    resultado = digito_1

contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito_2 in range(0,10):
    resultado_digito_2 += int(cpf[digito_2]) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) %  11

if digito_2 > 9:
    resultado2 = 0
else:
    resultado2 = digito_2

cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

print(f'O primeiro digito {resultado}')
print(f'O primeiro digito {resultado2}')
if cpf == cpf_gerado_calculo:
    print('CPF válido')
else:
    print('CPF invalido')
