cpf = input('Digite o cpf: ')
#cpf = '746.824.890-70'
cpf_limpo = cpf.replace('.', '-').replace('-', '')
cont = 10
soma = 0
for digito in range(0,9):
    multiplicacao = int(cpf_limpo[digito]) * cont
    soma += multiplicacao
    cont -= 1

nova_multiplicao = soma * 10
resto_divisao = nova_multiplicao % 11

if resto_divisao > 9:
    resultado = 0
else:
    resultado = resto_divisao

print(f'O primeiro digito {resultado}')