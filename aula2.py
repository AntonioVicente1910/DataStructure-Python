class Pessoa:
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    nomeCompleto = nome + '' + sobrenome
    cpf = input('Digite seu CPF: ')
    dataNascimento = input('Data de nascimento (dd/mm/aaaa): ')
    altura = input('Altura: ')

print(Pessoa.dataNascimento)

