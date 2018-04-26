
print('entrou nas rotinas')

def soma(num1,num2):
    return num1+num2

print(__name__)

if __name__=='__main__':
    print('executou o main das rotinas')
    print('soma = ',soma(5,5))