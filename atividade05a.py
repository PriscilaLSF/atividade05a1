#Faça um algoritmo que ajude uma empresa de limpeza. Para isso o programa deve ler a largura e o comprimento de um cômodo e calcular e mostrar a área a ser limpa e a quantidade de produto necessária para o serviço, sabendo que cada litro de produto limpa uma área de 2 metros quadrados.

ainput= input("Digite a largura do cômodo em metros: ")
binput= input("Digite o comprimento do cômodo em metros: ")

a= float(ainput)
b= float(binput)

area= a * b

produto= area / 2

print( "Para limpar essa área você precisará de " + str(produto)+" litros do produto.")