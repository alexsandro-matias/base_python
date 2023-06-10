def main():
    # para o uso de strings em python é possível o uso de aspas simples ou aspas duplas.
    # A única que é iniciada com aspas simples deve terminar com aspas simples.
    # print('aspas simples')
    # print("aspas duplas")
    # # Mesmo que haja aspas duplas abram e fechem na string, o conteúdo é lido como texto normalmente
    # print("Vou comer no Hamburguer no Bob's.")
    # # Agora, se usar aspas simples e, mesmo assim, precisar utilizar aspas simples na string,
    # # se faz necessário usar o caracter se escape (scaping) que no caso é \.
    # # Quando encontra esse caractere especial, o interpretador ignora a \ até encontrar o fechamento da String.
    # print('Vou comer esfirra no Habibb\'s.')
    #
    # Diferentemente de outras linguagens que consideram uma string como uma sequência de Bytes,
    # em Python uma string é um objeto de alto nível que implementa toda a complexidade do unicode
    # que somente neste momento é que pode ser transferido. No exemplo abaixo:
    nome = 'Alexsandro'
    sobrenome = 'Matias'

    # print(type(nome))
    # # Para ver o encoding dessa variável:
    # print(nome.encode())
    # Neste momento é possível perceber que se retorna uma sequência de Bytes.
    # Isso se torna mais claro que se usa acentos.
    descricao = "sandrinho é preguiçoso."

    # print(descricao.encode())
    # b'sandrinho \xc3\xa9 pregui\xc3\xa7oso.' - Representação em UTF-8 que é o padrão em Python
    # A vantagem dessa abordagem é que
    # qualquer caracter que possa ser representado por UTF-8 pode ser presentado em Python,
    # ou seja grande maioria dos caracteres descritos no mundo. Desta forma,
    # problemas como paginação de código (latin-1, UTF-8 ou ASCI),
    # não se tornam mais um problema, já que para linguagem, a representação é padronizada.
    # A partir da linha anterior,
    # se torna possível instânciar um objeto da classe str para outros objetos,
    # mesmo que sejam de outros tipo
    # inteiro = str(1)
    # print(inteiro)
    #
    # flutuante = str(1.1)
    # print(flutuante)
    # Como vimos, strings são objetos, então possui métodos, para ver tais métodos, usamos a função help:
    #     print(help(str))
    # outra característica das strings é a imutabilidade, ou seja,
    # toda e qualquer operação resulta em nova string mantendo a anterior.
    # Assim, os principais métodos são:
    # print(descricao.capitalize())
    # print(descricao.upper())
    # print(descricao.title())
    # Provando que a variável descrição ficou inalterada.
    # Métodos de manipulação
    # Replace - nova string com - descricao.replace(o que vai ser substituido , para o que vai se tornar)
    # print(descricao)
    # print(descricao.replace('é' , 'eh'))
    # split - separa a string em uma linha de strings, que por padrão, o delimitador é o espaço
    # print(descricao.split('é'))
    # Para concatenação de Strings usa-se o operador "+"
    # print(nome + ' ' + sobrenome)
    # Neste caso, 3 strings estão sendo manipuladas para geração de uma nova.
    # O que não pode ser eficiente quando precisamos manipular uma quantidade maior strings.
    # Uma forma eficiente para uma quantidade maior que de strings concatenadas é o método join.
    # 'delimitador'.join(listas_de_strings)
    # print(' '.join([nome, sobrenome]))
    # Isso também se aplica a caracteres de escape.
    # print('\n'.join([nome,sobrenome]))
    # O método join se torna eficiente uma vez que ele qual
    # o tamanho de cada string já considerando o espaço do delimitador.
    # Em baixo nível, o interpretador aloca uma varíavel com um tamanho maior da soma das strings,
    # realizando essa operação apenas uma vez.
    # O método que verifica o tamanho da string (do objeto) é o método len().
    # print(len(nome + sobrenome))


if __name__ == '__main__':
    main()
