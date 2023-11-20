# Listas dados do cliente
dadoscliente = [False]
# verificador de cadastro [0]
# numconta [1]
# nome do cliente [2]
# telefone [3]
# email [4]
# saldo [5]
# limite [6]
# senha [7]
# bloqueio [8]

#Listas Saldo, limite e saldo
extrato = []
limite = []

# imports de bibliotecas usados
import random
import os
import re


#Funções Mack Bank
def validar_email(email): #
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(padrao, email):
        return True
    else:
        return False


def limpar_tela(): #Limpa o terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def geradordeconta(): #Gera uma conta aleatoria de 4 digitos 1000-9999
    return random.randint(1000, 9999)


def print_color(text, color_code): #PRINTS COM CORES
  print(f'{color_code}{text}\033[0m')


def cadastro(): #Cadastro de contas.
    
    
    print_color('MACK BANK – CADASTRO DE CONTA', '\033[41m' )

    geradordeconta()
    num_conta = geradordeconta()


    print("NÚMERO DA CONTA: ", num_conta) 
    dadoscliente.append(num_conta)

    while True:  # verifica e pede um nome valido para o usuario
        nomecliente = input("NOME DO CLIENTE: ")
        if nomecliente.replace(" ", "").isalpha():
            dadoscliente.append(nomecliente)
            break
        else:
            print("Por favor, digite um nome válido.")

    while True:  # verifica e pede um telefone valido para o usuario
        telefonecliente = input("TELEFONE.......: ")
        if telefonecliente.isdigit():
            dadoscliente.append(telefonecliente)
            break
        else:
            print("Por favor, digite um numero de telefone valido!")

    while True:  #Pede um email para cadastro do cliente e verifica se ele e valido!
        emailcliente = input("EMAIL..........: ")
        if validar_email(emailcliente):
            dadoscliente.append(emailcliente)
            break
        else:
            print("O e-mail não é válido.")

    while True:  
        saldocliente = input("SALDO INICIAL...: R$ ")
        if (saldocliente.isalpha()):
            print("Por favor, insira um número válido.")
        else:
            numero = (saldocliente)

            if numero >= "1000":
                saldocliente = float(saldocliente)
                dadoscliente.append(saldocliente)
                break
            else:
                print(
                    "Saldo insuficiente para o cadastro, solicitamos um saldo inicial maior que 1000 para prosseguir!")

    while True:
        limitecliente = float(input("LIMITE DE CRÉDITO: R$ "))

        if limitecliente >= 0:
            dadoscliente.append(limitecliente)
            break

        else:
            print("O limite deve ser maior ou igual a zero")

    while True:  
        senhacliente = input("SENHA............: ")
        quantidade_caracteres_senha = len(senhacliente)
        if quantidade_caracteres_senha == 6:

            if (senhacliente.isnumeric()) == True:

                senhacliente = (senhacliente)
                dadoscliente.append(senhacliente)
                
                break
            else:
                print("Senha não númerica, por favor digite novamente! ")

        elif quantidade_caracteres_senha > 6:
            if (senhacliente.isnumeric()) == True:
                print("A senha não pode ser maior que 6 digitos, por favor, digitar novamente!")
            else:
                print("Senha não númerica e maior que 6 digitos, digite novamente! ")

        elif quantidade_caracteres_senha < 6:
            if (senhacliente.isnumeric()) == True:
                print("A senha e menor que seis digitos. Digite novamente!")
            else:
                print("Senha não númerica e menor que o solicitado. Digite novamente! ")

    while True:
                    veri_senha = input("REPITA A SENHA...: ")
                    if veri_senha in dadoscliente:

                        input("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

                        cadastro_completo = True
                        dadoscliente[0] = cadastro_completo

                        limpar_tela()
                        return dadoscliente
                        

                    else:
                        print("A Senha não e igual a acima")


def Depositar(dadoscliente, extrato): #Função de deposito no banco
    limpar_tela()

    while True:
       
        print_color('MACK BANK – DEPÓSITO EM CONTA', '\033[41m')
        num_conta = int(input("INFORME O NÚMERO DA CONTA: "))

        if (num_conta == dadoscliente[1]):
            print(f"NOME DO CLIENTE: {dadoscliente[2]} ")
            deposito = float(input("VALOR DO DEPÓSITO: R$ "))

            if deposito > 0:

                add_deposito = (f"DEPÓSITO: R$ {deposito:,.2f}")
                extrato.append(add_deposito)

                dadoscliente[5] += deposito


                input("DEPÓSITO REALIZADO COM SUCESSO!")
                limpar_tela()
                return dadoscliente, extrato
            
            else:
                limpar_tela()
                input("O Valor do deposito e invalido, operação cancelada!")
                break
            
        else:
            limpar_tela()
            print("A conta não existe, digite novamente!")


def sacar(dadoscliente, extrato): #Função de saque
    limpar_tela()
    tentativas_senha = 0
    
    print_color('MACK BANK – SAQUE DA CONTA', '\033[41m')
    while True:

            num_conta = int(input("INFORME O NÚMERO DA CONTA: "))
            if (num_conta == dadoscliente[1]):
                print(f"NOME DO CLIENTE: {dadoscliente[2]} ")

                while True:

                    if tentativas_senha < 3:
                        senha = input("INFORME A SENHA: ")

                        if (senha == dadoscliente[7]):

                            saque = float(input("VALOR DO SAQUE: R$ "))


                            if dadoscliente[5] >= saque:

                                    
                                    add_saque = (f"SAQUE: R$ {saque:,.2f}")                                      
                                    
                                    saldo_saque = dadoscliente[5] - saque
                                    dadoscliente[5] = saldo_saque
                                    saque = saldo_saque
                                    extrato.append(add_saque)

                                    input("SAQUE REALIZADO COM SUCESSO!")
                                    limpar_tela()

                                    return dadoscliente, extrato

                            else:

                                print("Seu saldo e insuficiente para sacar esse valor, deseja utilizar seu limite?: [Sim] ou [Não]")
                                continuar = int(input("Digite [1] para continuar\nDigite [2] para sair\n>>>>: "))

                                if continuar == 1:
                                        
                                        add_saque_limite = (f"SAQUE COM LIMITE: R$ {saque:,.2f}") 

                                        (dadoscliente[5] + dadoscliente[6]) >= saque
                                        saldo_saque = (dadoscliente[5] + dadoscliente[6]) - saque
                                        dadoscliente[5] = dadoscliente[5] - saque 
                                        dadoscliente[6] = saldo_saque


                                        extrato.append(add_saque_limite)
                                        

                                        print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO.")
                                        input("SAQUE REALIZADO COM SUCESSO!\nAperte enter para voltar ao menu.")
                                        limpar_tela()
                                            
                                        return dadoscliente, extrato
                                else:
                                    print("Operação cancelada")
                                    limpar_tela()
                                    return menu()
                                    
                            

                        else:
                            if tentativas_senha < 2:
                                tentativas_senha += 1
                                print(f"Senha incorreta. Você ainda tem {3 - tentativas_senha} tentativas restantes.")
                            else:
                                limpar_tela()
                                print("Senha incorreta. Acesso bloqueado.")
                                bloqueio = "blocked"
                                dadoscliente.append(bloqueio)
                                return dadoscliente


            else:
                print("Conta inexistente, digite novamente.")

def saldo(dadoscliente): #função consultar saque.

    
    tentativas_senha = 0
    limpar_tela()
    
    print_color('MACK BANK – CONSULTA SALDO', '\033[41m')

    while True:
        num_conta = int(input("INFORME O NÚMERO DA CONTA: "))
        if (num_conta == dadoscliente[1]):
            print(f"NOME DO CLIENTE: {dadoscliente[2]} ")
            while True:
                if tentativas_senha < 3:
                    senha = input("INFORME A SENHA: ")
                    if (senha == dadoscliente[7]):
                        print(f"SALDO EM CONTA: R$ {dadoscliente[5]:,.2f}")
                        print(f"LIMITE DE CRÉDITO: R$ {dadoscliente[6]:,.2f}")
                        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
                        limpar_tela()
                        return menu()

                

                    else:
                        if tentativas_senha < 2:
                            tentativas_senha += 1
                            print(f"Senha incorreta. Você ainda tem {3 - tentativas_senha} tentativas restantes.")
                        else:
                            limpar_tela()
                            print("Senha incorreta. Acesso bloqueado.")
                            bloqueio = "blocked"
                            dadoscliente.append(bloqueio)
                            return dadoscliente
        else:
            print("Conta inexistente, digite novamente.")


def consulta_extrato(dadoscliente, extrato): #Consulta extrato

    limpar_tela()
    
    tentativas_senha = 0

    print_color('MACK BANK – EXTRATO DA CONTA', '\033[41m')

    while True:
        num_conta = int(input("INFORME O NÚMERO DA CONTA: "))
        if (num_conta == dadoscliente[1]):
            print(f"NOME DO CLIENTE: {dadoscliente[2]} ")
            while True:
                if tentativas_senha < 3:
                    senha = input("INFORME A SENHA: ")
                    if (senha == dadoscliente[7]):

                    
                        print(f"LIMITE DE CRÉDITO: R$ {dadoscliente[6]:,.2f}")
                        print_color('ÚLTIMAS OPERAÇÕES:', '\033[41m' )
                        print('\n'.join(extrato))
                        print(f"SALDO EM CONTA: R$ {dadoscliente[5]:,.2f}")
                        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
                        limpar_tela()
                        return menu()

                

                    else:
                        if tentativas_senha < 2:
                            tentativas_senha += 1
                            print(f"Senha incorreta. Você ainda tem {3 - tentativas_senha} tentativas restantes.")
                        else:
                            limpar_tela()
                            print("Senha incorreta. Acesso bloqueado.")
                            bloqueio = "blocked"
                            dadoscliente.append(bloqueio)

                            return dadoscliente
        else:
            print("Conta inexistente, digite novamente.")
    

def menu(): #Menu principal do programa
    
    
    while True:
        
        print_color('MACK BANK – ESCOLHA UMA OPÇÃO', '\033[41m')
        print("""
        (1) CADASTRAR CONTA CORRENTE
        (2) DEPOSITAR
        (3) SACAR
        (4) CONSULTAR SALDO
        (5) CONSULTAR EXTRATO
        (6) FINALIZAR
        """)

      


        

        try:
            escolha = int(input("SUA OPÇÃO: "))
        except:
            input("Essa opção não é valida. Tente novamente.")
            limpar_tela()
            menu()

        #Inicia o cadastro!
        if escolha == 1:
            if dadoscliente[0] == False:
                limpar_tela()
                cadastro()
            else:
                print("Você ja está cadastrado em nosso banco.")
                input("Aperte enter para voltar.")
                limpar_tela()
            

        #Inicia os depositos
        elif escolha == 2:

            limpar_tela()
            if dadoscliente[0] == True:
                Depositar(dadoscliente, extrato)
                
            else:
                limpar_tela()
                print("Você não pode acessar o programa.")
                input("Aperte enter para voltar.")
                limpar_tela()

        #Inicia os saques
        elif escolha == 3:
            if dadoscliente[0] == True:
                if "blocked" not in dadoscliente:
                    sacar(dadoscliente, extrato)

                else:
                    limpar_tela()

                    print("Sua conta está bloqueada, reinicie o Aplicativo do banco!")
                    input("Pressione enter para reiniciar o aplicativo do banco.")

                    limpar_tela()

                    #Limpeza das listas
                    dadoscliente.clear()
                    extrato.clear()
                    limite.clear()

                    desbloqueio_cadastro = False
                    dadoscliente.append(desbloqueio_cadastro)
                
                
            else:
                limpar_tela()
                print("Você não pode acessar o programa.")
                input("Aperte enter para voltar.")
                limpar_tela()

        #inicia a consulta de saldo
        elif escolha == 4:
            if dadoscliente[0] == True:
                if "blocked" not in dadoscliente:
                    saldo(dadoscliente)
                
                else:
                    limpar_tela()

                    print("Sua conta está bloqueada, reinicie o Aplicativo do banco!")
                    input("Pressione enter para reiniciar o aplicativo do banco.")

                    limpar_tela()

                    #Limpeza das listas
                    dadoscliente.clear()
                    extrato.clear()
                    limite.clear()

                    desbloqueio_cadastro = False
                    dadoscliente.append(desbloqueio_cadastro)

            else:
                limpar_tela()
                print("Você não pode acessar o programa.")
                input("Aperte enter para voltar.")
                limpar_tela()

        #Inicia o extrato bancario do cliente
        elif escolha == 5:
            if dadoscliente[0] == True:
                if "blocked" not in dadoscliente:
                    consulta_extrato(dadoscliente, extrato)

                else:
                    limpar_tela()

                    print("Sua conta está bloqueada, reinicie o Aplicativo do banco!")
                    input("Pressione enter para reiniciar o aplicativo do banco.")

                    limpar_tela()

                    #Limpeza das listas
                    dadoscliente.clear()
                    extrato.clear()
                    limite.clear()

                    desbloqueio_cadastro = False
                    dadoscliente.append(desbloqueio_cadastro)

            else:
                limpar_tela()
                print("Você não pode acessar o programa.")
                input("Aperte enter para voltar.")
                limpar_tela()

        #Sobre o programa e consulta das listas!
        elif escolha == 6:
            limpar_tela()
            print("""MACK BANK – SOBRE
            Este programa foi desenvolvido por
            Thiago Kauã Pestana do Amaral - 32397739
            """)

            input("Aperte enter para voltar ao banco!")
            limpar_tela()

limpar_tela()
menu()



