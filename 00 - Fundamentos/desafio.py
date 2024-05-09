menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor>0:
            saldo+= valor

            extrato+= (f"\nDeposito do valor R$ {valor:.2f}")
        else:
            print("Operação inválida,valor desconhecido!!")
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        saldo_insuficiente = valor>saldo

        limite_excedido = valor>limite

        limite_diario_excedido = numero_saques>=LIMITE_SAQUES 

        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif limite_excedido:
            print("Operação falhou! O valor excedeu o limite por saque.")
        elif limite_diario_excedido:
            print("Operação falhou! Você passou do limite de saques por dia")
        else:
            valor>0
            saldo-=valor
            numero_saques+=1
            extrato+= (f"\nSaque do valor R$ {valor:.2f}")
            print("Saque efetuado com sucesso!!")     

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
