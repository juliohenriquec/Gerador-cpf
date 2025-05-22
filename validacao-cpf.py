cpf = input('Digite o cpf: ').replace('.', '-').replace('-', '')
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito_1 in range(0,9):
    resultado_digito_1 += int(cpf[digito_1]) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

if digito_1 > 9:
    resultado = 0
else:
    resultado = digito_1

print(f'O primeiro digito {resultado}')
