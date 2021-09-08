def soma(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def div(x,Y):
    return x/Y


print("\n******************* Python Calculator *******************\n")


print('''Qual operação deseja realizar?"
1-soma
2-subtração
3-multiplicação
4-divisão''')

escolha=input("Digite sua opção: ")

num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))

if escolha== '1':
    print("\n")
    print(num1,"+",num2,"=",soma(num1, num2 ))
    print("\n")

elif escolha== '2' :
    print("\n")
    print(num1,"+",num2,"=",sub(num1, num2 ))
    print("\n")

elif escolha== '3':
    print("\n")
    print(num1,"+",num2,"=",multi(num1, num2 ))
    print("\n")

elif escolha=='4':
    print("\n")
    print(num1,"+",num2,"=",div(num1, num2 ))
    print("\n")
else:
   print("\nOpção inválida!")
