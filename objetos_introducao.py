# para representar um literal binário usa-se o o termo 0b e a sequencia binária.
# binario = 0b1000001
# letra = chr(binario)
# print(binario)
# print(letra)

# Então o mesmo valor em bits pode ser representado de formas diferentes dependendo do contexto.

pessoas = ['alexsandro', 'maria', 'santos', 'josiane', 'josefa']
# print(id(pessoas), type(pessoas))

# quando o print() é chamado, o que está sendo impresso na tela realmente é o conteúdo do objeto 'pessoas'.
# Da mesma maneira se for impresso o objeto com a função id() será impressa a identidade deste objeto.
# Outra função que mostra mais características do objeto é a função type que, como o próprio nome sugere,
# mostra o tipo dele. Assim, qualquer objeto tem características gerais um valor, tipo e uma identidade. Percebe-se
# que os valores podem ser iguais em alguns contextos, mas caracterizam objetos diferentes.

funcionarios = ['alexsandro', 'maria', 'santos', 'josiane', 'josefa']
# print(id(pessoas))
# print(id(funcionarios))
# Mesmo possuindo os mesmos tipos e valores, a identificação dos objetos é diferente, ou seja,
# são listas totalmente distintas. Para provar que os valores são iguais, basta usar o operador ==
# print(funcionarios == pessoas)
# Agora, para verificar se identidade de uma é igual a outra, o operador utilizado deve ser o 'is'.
print(funcionarios is pessoas)