# estrutura de repetição para que o algoritmo continue a acontecer
while True:
    # versão com for.
    # para inserir o 0 no range e só tirar o 1 que está antes do 11.
    num = int(input("*** Gerador de Tabuada *** \n Digite o número que desenha multiplicar: "))
    for x in range(1,11):
        print("{} X {} = {}".format(num,x,(num*x)))

    # versão com while.
    # para inserir o 0 no range e só tirar o 1 que está antes do 11.    
    num = int(input("*** Gerador de Tabuada V:While *** \n Digite o número que desenha multiplicar: "))
    j = 1
    while j <= 10:
        print("{} X {} = {}".format(num,j,(num*j)))
        j = j + 1;
        # não esqueça de atribuir um valor para evitar o loop infinito
        
    controle = input("Digite: Y para continuar e N para encerrar")
    #variável de controle para exibição do programa
    
    if controle.upper() != 'Y':
        break; #comando para encerrar programa
