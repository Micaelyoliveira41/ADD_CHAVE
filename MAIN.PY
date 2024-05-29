#Dicionário
pessoa= {
    'Nome': 'Micaely Oliveira',
    'Idade': 24,
    'Profissão': 'Tec Enfermagem'
}

nova_chave = input('Digite o nome do campo: ')
novo_valor = input('Informe o valor do nov campo: ')
pessoa[nova_chave] = novo_valor

#exibe os dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')