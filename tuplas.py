# Para declarar uma tuplas, geralmente, os valores podem estar contidos entre parênteses.
# tupla = (1, 3, 'Alex')
# Uma característica das tuplas é que elas são imutáveis.
# Ou seja, quando fizermos qualquer operação, um novo objeto é criado
# tupla = tupla + (2, 4, 'Matias')
# print(tupla)

# Por essa limitação, as tuplas têm pouco métodos disponíveis.
# print(help(tuple))
# Também é possível fazer uma atribuição diretamente. Mas no caso abaixo,
# o Python vai separar item por item na atribuição
# print(tuple('Alexsandro'))

# Da mesma forma, é possível realizar uma conversão de uma lista em uma tupla.
# print(tuple([1,2,3]))
# Similarmente as listas, as tuplas podem armazenar qualquer tipo de valor:
# tupla_completa = ("Alexsandro", 3.14, len, 4j, False)
# Como se trata de uma sequência, é possível acessar os índices dos elementos, assim como os slicing.
# print(tupla_completa[1])
# print(tupla_completa[:4])
# Como a tupla é uma sequência imutável, quando se faz uma cópia ela retorna ela própria.
# nova_tupla = tupla_completa[:]
# print(id(nova_tupla), id(tupla_completa))
# Ou seja, elas apontam para o mesmo endereço de memória, em outras palavras,
# apontam para a mesma referência (mesmo objeto).

# Outra característica da tupla é que ela pode ser criada com valores
# entre vírgulas e não necessariamente os '()'. Tanto que é possível apenas colocar
# a vírgula depois do elemento.
# numero = 3,
# print(type(numero))
# Outro exemplo para provar que o parênteses não implica na geração de uma tupla:
numero = (3)
# print(type(numero)) - <class 'int'> e não uma tupla.

# Para criar uma tupla vazia:
tuple_vazia = ()
segunda_tuple_vazia = tuple()

# terceira_tupla = 1, 2, 3, 4
# print(terceira_tupla)

# A ideia dos parênteses é justamente pela ideia matemática de agrupamento de termos semelhantes.
# Ou até mesmo pela ideia de precedência matemática.

primeira_tupla = 'a', 'b', 'c'
# Se se tentar concatenar uma tupla da forma
# segunda_tupla = 'd', 'e' + primeira_tupla
# seguirá um erro -   segunda_tupla = 'd', 'e' + primeira_tupla
#                          ~~~~^~~~~~~~~~~~~~~~
# TypeError: can only concatenate str (not "tuple") to str.
# Isso ocorre por que é primeira a tupla com a string 'e' dando erro de tipo.
# Então para se criar a tupla e depois concaternar as tuplas, se faz necessários os parênteses.
# segunda_tupla = ('d', 'e') + primeira_tupla
# print(segunda_tupla)
