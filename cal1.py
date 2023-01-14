while True:
   
    n1 = input('Digite um valor: ') ### NÚMERO 1
    op = input('Digite um operador: ') ### OPERADOR
    n2 = input('Digite outro valor: ') ### NÚMERO 2

    nv = None ### NÚMERO VÁLIDO 
    nf1 = 0
    nf2 = 0

    try:
        nf1 = float(n1) ### NÚMERO FLUTUANTE 1
        nf2 = float(n2) ### NÚMERO FLUTUANTE 2
        nv = True 

    except: 
        nv = None

    if nv is None:
         print('Algum número está incorreto.')
         continue 
   
    op_p = '+-*/' ### OPERADORES PERMITIDOS 

    if op not in op_p:
        print('Operador invalido')
        continue 
    if len(op) > 1:
        print('Você digitou mais de um operador.')
        continue 

    print('Confira o resultado da sua conta')

    if op == '+':
        print(nf1 + nf2)
    elif op == '-':
        print(nf1 - nf2)
    elif op == '*':
        print(nf1 * nf2)
    elif op == '/':
        print(nf1 / nf2)


    sair = input('Você quer [S]air? ').lower().startswith('s')
    if sair == True:
        break 