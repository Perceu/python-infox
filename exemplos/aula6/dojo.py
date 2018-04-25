"""
Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, 
com as seguintes exceções:

Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do numero;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do numero;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do numero'.

"""

def fizz3(numero):
    if numero % 3 == 0:
        return "Fizz"
    return ""

def fizzbuzz(numero):
    retorno = ""
    retorno += fizz3(numero)

    if numero%5==0:
        retorno += "Buzz"

    if retorno == "":
        retorno = str(numero)
    
    return retorno
    
assert fizzbuzz(1)=="1"
assert fizzbuzz(3)=="Fizz"
assert fizzbuzz(5)=="Buzz"
assert fizzbuzz(2)=="2"
assert fizzbuzz(15)=="FizzBuzz"
assert fizzbuzz(9)=="Fizz"

