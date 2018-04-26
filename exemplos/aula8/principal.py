
from rotinas import soma

from modulo1.calculadora import Calculadora

if __name__=='__main__':
    calc = Calculadora(3,5)
    
    print('entrou no main do main')
    print('soma',calc.soma())
    print('divisao',calc.divisao())
    print('multiplicacao',calc.multiplicacao())
    print('subtracao',calc.subtracao())