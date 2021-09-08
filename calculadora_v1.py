# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")


print('''Qual operação deseja realizar?"
1-soma
2-subtração
3-multiplicação
4-divisão''')
opcao=int(input("Digite (1/2/3/4):"))

if opcao==1:
    n1=int(input("Digite o primeiro número:"))
    n2=int(input("Digite o segundo número"))
    result=n1+n2
    print("Resultado=",result)
elif opcao==2:
    n1=int(input("Digite o primeiro número:"))
    n2=int(input("Digite o segundo número"))
    result=n1-n2
    print("Resultado=",result)
elif opcao==3:
    n1=int(input("Digite o primeiro número:"))
    n2=int(input("Digite o segundo número"))
    result=n1*n2
    print("Resultado=",result)
elif opcao==4:
    n1=int(input("Digite o primeiro número:"))
    n2=int(input("Digite o segundo número"))
    result=n1/n2
    print("Resultado=",result)
else:
     print("Opção Inválida")
