nome = 'Alexsandro'

# for letra in nome:
# Nesta primeira situação apenas para imprimir as vogais em letras maiúsculas
# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#     print(letra.upper())
# # Mas se houvesse apenas o if somente iria encontrar as vogais e depois imprimi-las em maiúsculas.
# # Por isso, precisa deste else para que - em caso contrário das vogais - imprima o restante.
# else:
#     print(letra)

# Essa verificação de comparação entre dois valores é através do operador "==" ou
# também chamado de operador de equivalência.

# Mas de qualquer forma esse código pode ser melhorado uma vez que podemos agrupar
# as vogais numa tupla e depois verificar se a letra da iteração está contida nesta tupla.

# for letra in nome:
#     if letra in ('a','e','i','o','u'):
#         print(letra.upper())
#     else:
#         print(letra)

# O operador in tem a funçao de verificar se algum elemento está contido numa determinada sequência.
# O python isso ainda mais em alto nível por que se pode deixar todas as letras numa mesma string.
# O interpretador é inteligente o suficiente para verificar caracter por caracter está numa sequência. Então,
# o mesmo efeito pode ser obtido pelo código:

# for letra in nome:
#     if letra in 'aeiou':
#         print(letra.upper())
#     else:
#         print(letra)

# Agora, vamos supor que precise imprimir no lugar do 's' o caracter '$'.
# Pode-se imaginar primeiramente o seguinte código:
# for letra in nome:
#     if letra in ('a','e','i','o','u'):
#         print(letra.upper())
#     else:
#         print(letra)
#     if letra == 's':
#         print('$')

# Porém nesta abordagem, temos um erro semâtico, já que os 'if's são totalmente independentes um do outro.
# Para que um se torne seja executando caso o if não seja atendido, mas que também não seja executado no else,
# usa-se a função elif:
# for letra in nome:
#     if letra in ('a', 'e', 'i', 'o', 'u'):
#         print(letra.upper())
#     elif letra == 's':
#         print('$')
#     else:
#         print(letra)

# Em outras linguagens existem uma abordagem parecida como else if que pode causar ambiguidades.
# No caso do Python existe uma palavra reservada pra isso. Sintanticamente, somente pode existir um elif
# se houver um if anterior.

# Palavras Reservadas
# True e false são singletons em python, ou seja, somente existem uma instância de cada uma desses objetos.
# Mas ao mesmo tempo, a inexistência ou nulidade de itens no contexto de tabela verdade implica em falso. Por exemplo:

# print(bool(None))
# print(bool(False))
# print(bool(0))
# print(bool(''))
# print(bool([]))
# print(bool({}))
# print(bool(()))

# Então para qualquer outro valor, representa verdadeiro.
# print(bool(1))
# print(bool(True))
# print(bool('a'))
# print(bool([1,3]))
# print(bool({'Nome':'Alexsandro'}))
# print(bool((19,10)))

# O python também utiliza o conceito de curto-cirtuito de comparações:
# print(True and 'ab') - retorno 'ab' mesmo que os dois tenham a saída lógica verdadeira.
# Já que o python retorna o último elemento avaliado.
#
# print(True and []) - retorno [] por que o python compara um valor True com uma lista vazia que é o valor falso.
# Como o valor de saída é falso, o retorno é a própria lista vazia.

# Invertendo as comparações:
# print('abc' and True) - Como  a última comparação foi True, este será o valor retornado.

# Porém se o primeiro valor for falso e qualquer outra coisa,
# o Python ignora o restante por que sabe que o restante será falso. Assim:
# print([] and True) - O valor falso é a lista vazia,
# logo nem é comparado o restante da expressão retornando o valor falso representado pela lista vazia.
# Esse comportamento é chamado de curto circuito.
# Pode explicitado tentando comparar uma variável com uma variável que nem foi declarada,
# e mesmo assim o código executa sem erros.
# print(1 or variavel). Isso somente é possível por que como o valor 1 é verdadeiro,
# o restante da expressão e ignorada e retorna o valor verdadeiro expressado pelo valor 1.