#calculadora
def calc(op, a, b):
    if op == '+':
        soma(a,b)
    elif op == '-':
        subtr(a,b)
    elif op == '*':
        mult(a,b)
    elif op == '/':
        divi(a,b)
    else:
        print("Inválido")
#soma
def soma(a, b):
    print(a+b)

#subtrai
def subtr(a,b):
    print(a-b)

#multiplica
def mult(a,b):
    print(a*b)

#divide
def divi(a,b):
    print(a/b)

