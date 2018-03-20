#abrindo um aquivo para escrita no inicio do arquivo
arquivo = open('index.txt','w')

arquivo.write('primeira linha')
arquivo.write(' continua')
arquivo.write(' \nnova linha')

arquivo.close()

#abrindo um aquivo para escrita no final do arquivo
arquivo = open('index.txt','a')
arquivo.write('\nterceira linha\n')
arquivo.close()

#abrindo um aquivo para escrita no final do arquivo
arquivo = open('index.txt','r')
#ler uma linha
print(arquivo.readline())
#ler todas as linhas
print(arquivo.readlines())
#voltar para o inicio do arquivo
arquivo.seek(0)

#ler todo o arquivo
print(arquivo.read())
arquivo.close()

