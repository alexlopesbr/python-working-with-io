# mode='w' sobrescreve o arquivo, apagando o anterior e criando um novo
contact_file = open('dados/contatos_escrita.csv', encoding='latin_1', mode='w+')

# mode='a' atualiza o aqruivo inserindo novas linhas na última posição
# contact_file = open('dados/contatos_escrita.csv', encoding='latin_1', mode='a')

contacts = [
    '11,New,new@new.com.br\n',
    '12,New2,new2@new.com.br\n',
    '13,New3,new3@new.com.br\n',
    '14,New4,new4@new.com.br\n',
]

for contact in contacts:
    contact_file.write(contact)

# força a inserção de dados sem a necessidade de fechar o arquivo
contact_file.flush()

# move o cursor para posição inicial
contact_file.seek(0)

for l in contact_file:
    print(l, end='')
