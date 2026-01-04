import re
import sys

# cpf_enviado_pelo_cliente = '499.628.990-28'.replace('.', '').replace('-', '')
cpf_enviado_pelo_cliente = re.sub(
    r'[^0-9]',
    '',
    '499.628.990-28'
)

cpf_e_sequencial = cpf_enviado_pelo_cliente == len(cpf_enviado_pelo_cliente) * cpf_enviado_pelo_cliente[0]

if cpf_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digito =  cpf_enviado_pelo_cliente[:9]
contador_regressivo = 10
resultado = 0

# PEGANDO O PRIMEIRO DIGITO DE UM CPF

for digito in nove_digito:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

primeiro_digito = ((resultado * 10) % 11)
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0


# PEGANDO O SEGUNDO DIGITO DE UM CPF

dez_digito =  nove_digito + str(primeiro_digito)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digito:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = ((resultado_digito_2 * 10) % 11)
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# VALIDAÇÃO

cpf_gerado_pelo_calculo = f'{nove_digito}{primeiro_digito}{segundo_digito}'
print(cpf_gerado_pelo_calculo)

if cpf_enviado_pelo_cliente == cpf_gerado_pelo_calculo:
    print(f'O {cpf_enviado_pelo_cliente} é válido')
else:
    print('O CPF enviado pelo cliente não é válido')