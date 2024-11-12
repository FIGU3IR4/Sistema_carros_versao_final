import json
import os
from datetime import datetime


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'
    
    
    
    #FUNÇÃO MENU LOCADORA ADMINISTRADOR
def exibir_menu_adm_locadora():

    print("\nMENU:")
    print("1. ADICIONAR LOCADORA")
    print("2. LISTAR LOCADORA")
    print("3. ATUALIZAR LOCADORA")
    print("4. EXCLUIR LOCADORA")
    print("5. LISTAR UMA LOCADORA")
    print("6. VOLTAR AO MENU ANTERIOR")

def menuLocadora ():
    print ('=' * 50)
    print ("| 1 - LOCADORA CADASTRADA |\n| 2 - CADASTRAR LOCADORA |\n| 3 - LISTA DE LOCADORAS |\n| 4 - EXCLUIR LOCADORA |\n| 5 - VOLTAR AO MENU PRINCIPAL |\n| 6 - ENCERRA PROGRAMA |\n")

# CADASTRAR LOCADORA
def salvar_locadora(dados_locadoras, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados_locadoras, f, indent=4)
    print("Locadora Cadastrada com sucesso!")

#LISTAR LOCADORA FUNÇÃO
def listar_locadora():
    os.system('cls')
    with open('dados_locadora.json') as meu_json:
        dados =json.load(meu_json)
        
    
         
        for nome, info in dados.items():
            print("*" * 50)
            print(f"Nome: {nome}")
            print("Dados:")
            print(f"  Codigo Locadora: {info['codigo_locadora']}")
            print(f"  Contato Locadora: {info['contato_locadora']}")
            print(f"  Endereço Locadora: {info['endereco_locadora']}")
            print("=" * 50)

def apagar_locadora():
    apagar = input("Digite o nome da locadora a ser apagado: ").strip()  # Remove espaços em branco

    with open('dados_locadora.json', 'r') as apagar_dados:
        data = json.load(apagar_dados)

        # Normaliza os nomes no dicionário para comparação
        nomes_normalizados = {nome.lower(): nome for nome in data.keys()}

        # Verifica se o nome da locadora existe
        nome_key = nomes_normalizados.get(apagar.lower())  # Usa .lower() para normalizar

        if nome_key:
            data.pop(nome_key)  # Remove a locadora
            
            # Salvar os dados atualizados no mesmo arquivo
            with open('dados_locadora.json', 'w') as salvar_dados:
                json.dump(data, salvar_dados, indent=4)  # Salva os dados atualizados
                print("LOCADORA EXCLUIDA COM SUCESSO")
        else:
            print(f"LOCADORA '{apagar}' não encontrado.")

 #LISTA DE CARROS DE CADA LOCADORA
def lista_carros():
    os.system('cls')
    with open('dados_carros.json') as meu_json:
        dados =json.load(meu_json)
        
        for nome, info in dados.items():
            print("*" * 50)
            print(f"Nome: {nome}")
            print("Dados:")
            print(f"  marca do carro: {info['marca']}")
            print(f"  cor do carro: {info['cor']}")
            print("=" * 50)

# MENU CARROS
def menu_carros():
    print(cor.VERDE+'------------------------------------------------')
    print('| 1 - VER CARROS')
    print('| 2 - ADICIONAR  CARROS')
    print('| 3 - ATUALIZAR CARROS')
    print('| 4 - VER CARROS')
    print('------------------------------------------------')

# CADASTRAR CARROS
def salvar_carros(dados_carros, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados_carros, f, indent=4)
    print("Carro Cadastrado com sucesso!")

# EXCLUIR CARROS
    apagar = input("Digite o nome do carro a ser apagado: ").strip()  # Remove espaços em branco

    with open('dados_carros.json', 'r') as apagar_dados:
        data = json.load(apagar_dados)

        # Normaliza os nomes no dicionário para comparação
        nomes_normalizados = {nome.lower(): nome for nome in data.keys()}

        # Verifica se o nome do carro existe
        nome_key = nomes_normalizados.get(apagar.lower())  # Usa .lower() para normalizar

        if nome_key:
            data.pop(nome_key)  # Remove o carro
            
            # Salvar os dados atualizados no mesmo arquivo
            with open('dados_carros.json', 'w') as salvar_dados:
                json.dump(data, salvar_dados, indent=4)  # Salva os dados atualizados
                print("CARRO EXCLUIDO COM SUCESSO")
        else:
            print(f" Carro '{apagar}' não encontrado.")            
            
            
# Função para carregar os dados do arquivo json1
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar os dados no arquivo json   CREATE
def salvar_dados(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
    print("Dados salvos com sucesso!")


# Função para atualizar os dados no arquivo json   UPDATE
def atualizar_clientes():
    os.system('cls')
    atualizar = input("Digite o nome do cliente a ser atualizado: ").strip()
    
    with open('dados_clientes.json', 'r') as atualizar_cliente:
        atualizacao = json.load(atualizar_cliente)
        
    # Normaliza os nomes no dicionário para comparação
    nomes_normalizados = {nome.lower(): nome for nome in atualizacao.keys()}
    
    # Verifica se o nome do cliente existe
    nome_key = nomes_normalizados.get(atualizar.lower())  # Usa .lower() para normalizar
    
    if nome_key:
        print('Atualizar Dados cliente cliente')
        cpf_cliente = input('Digite O novo CPF: ')
        nascimento_cliente = input('A nova data de nascimento: ')
        numero_cliente = input('Digite o noco número para contato: ')
        cnh_cliente = input('Digite o novo número de sua CNH: ')
        
        # Atualiza os dados do cliente
        atualizacao[nome_key] = {
            'cpf': cpf_cliente,
            'nascimento': nascimento_cliente,
            'numero': numero_cliente,
            'cnh': cnh_cliente
        }
        
        # Salvar os dados no arquivo JSON
        with open('dados_clientes.json', 'w') as salvar_dados:
            json.dump(atualizacao, salvar_dados, indent=4)  # Salva os dados atualizados
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(f'Cliente {nome_key} atualizado com sucesso!')
    else:
        print(f"Cliente '{atualizar}' não encontrado.")
            
            
  
# Função para Ler  os dados do arquivo json1    READ
def listar_clientes():
    with open('dados_clientes.json') as meu_json:
        dados =json.load(meu_json)
    
   
        for nome, info in dados.items():
            print("*" * 50)
            print(f"Nome: {nome}")
            print("Dados:")
            print(f"  CPF: {info['cpf']}")
            print(f"  Data de Nascimento: {info['nascimento']}")
            print(f"  Número: {info['numero']}")
            print(f"  CNH: {info['cnh']}")
            print("=" * 50)






# Função para APAGAR os dados do Administrador   DELETE
def apagar_adm():
    apagar = input("Digite o nome do Administrador a ser apagado: ").strip()  # Remove espaços em branco

    with open('dados_administradores.json', 'r') as apagar_dados:
        data = json.load(apagar_dados)

        # Normaliza os nomes no dicionário para comparação
        nomes_normalizados = {nome.lower(): nome for nome in data.keys()}

        # Verifica se o nome do administrador existe
        nome_key = nomes_normalizados.get(apagar.lower())  # Usa .lower() para normalizar

        if nome_key:
            data.pop(nome_key)  # Remove o administrador
            
            # Salvar os dados atualizados no mesmo arquivo
            with open('dados_administradores.json', 'w') as salvar_dados:
                json.dump(data, salvar_dados, indent=4)  # Salva os dados atualizados
                print("ADMINISTRADOR APAGADO COM SUCESSO")
        else:
            print(f"ADMINISTRADOR '{apagar}' não encontrado.")

#Função ATUALIZAR ADMINISTRADOR
def atualizar_administrador():
    os.system('cls')
    atualizar = input("Digite o usuário do administrador a ser atualizado: ").strip()
    
    with open('dados_administradores.json', 'r') as atualizar_administrador:
        atualizacao = json.load(atualizar_administrador)
        
    # Normaliza os nomes no dicionário para comparação
    nomes_normalizados = {nome.lower(): nome for nome in atualizacao.keys()}
    
    # Verifica se o nome do cliente existe
    nome_key = nomes_normalizados.get(atualizar.lower())  # Usa .lower() para normalizar
    
    if nome_key:
        print('Atualizar Dados do administrador')
        nome_completo_adm = input('Digite seu nome completo atualizado: ')
        senha_adm = input('Informe sua nova senha: ')
        
        
        # Atualiza os dados do cliente
        atualizacao[nome_key] = {
            'nome': nome_completo_adm,
            'senha': senha_adm,
            
        }
        
        # Salvar os dados no arquivo JSON
        with open('dados_administradores.json', 'w') as salvar_dados:
            json.dump(atualizacao, salvar_dados, indent=4)  # Salva os dados atualizados
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print(f'Administrador {nome_key} atualizado com sucesso!')
    else:
        print(f"Administrador '{atualizar}' não encontrado.")

#FUNÇÃO LISTAR ADMINISTRADORES
def listar_administradores():
    os.system('cls')
    with open('dados_administradores.json') as meu_json:
        dados =json.load(meu_json)

        for nome, info in dados.items():
            print("*" * 50)
            print(f"Usuário: {nome}")
            print("Dados:")
            print(f"  Nome: {info['nome']}")
            
# Função para APAGAR  os dados do arquivo json1   DELETE
def apagar_usuario():
    apagar = input("Digite o nome do Cliente a ser apagado: ").strip()  # Remove espaços em branco

    with open('dados_clientes.json', 'r') as apagar_dados:
        data = json.load(apagar_dados)

        # Normaliza os nomes no dicionário para comparação
        nomes_normalizados = {nome.lower(): nome for nome in data.keys()}

        # Verifica se o nome do cliente existe
        nome_key = nomes_normalizados.get(apagar.lower())  # Usa .lower() para normalizar

        if nome_key:
            data.pop(nome_key)  # Remove o cliente
            
            # Salvar os dados atualizados no mesmo arquivo
            with open('dados_clientes.json', 'w') as salvar_dados:
                json.dump(data, salvar_dados, indent=4)  # Salva os dados atualizados
                print("CLIENTE APAGADO COM SUCESSO")
        else:
            print(f"Cliente '{apagar}' não encontrado.")

          # informaçoes de locadora

def menu_locadora(user_loc):
    print(cor.VERDE+'------------------------------------------------')
    print('        |BEM VINDO|'+user_loc)
    print('------------------------------------------------')
    
    print('| 1 - VER CARROS')
    print('| 2 - ADICIONAR  CARROS')
    print('| 3 - ATUALIZAR CARROS')
    print('| 4 - VER CARROS')
        
        

# Carregar os dados existentes 
dados_clientes = carregar_dados('dados_clientes.json')
dados_adm = carregar_dados('dados_administradores.json')
dados_locadoras = carregar_dados('dados_locadora.json')
dados_carros = carregar_dados('dados_carros.json')


#menu principal
def menuPrincipal():
    print('=================================================')
    print(cor.AMARELO+'|BEM VINDO AO NOSSO SISTEMA DE ALUGUEL DE CARROS|')
    print('=================================================')
    print('\n1 - ADMINISTRADOR\n2 - LOCADORA\n3 - CLIENTE\n4 - SAIR')
    


#menu Secundario 
def exibir_menu():
    
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")

def cadastro_cliente():
    print("Bem-vindo ao sistema de cadastro!\n")
    
    
    nome_cliente = input("Digite seu nome completo: ").strip()
    cpf_cliente = input("Digite seu CPF (apenas números): ").strip()
    nascimento_cliente = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
    numero_cliente = input("Digite seu número para contato: ").strip()
    cnh_cliente = input("Digite o número de sua CNH (Caso tenha): ").strip()
    
 
    if nome_cliente in dados_clientes:
        print(f"O cliente {nome_cliente} já está cadastrado!")
    else:
       
        dados_clientes[nome_cliente] = {
            'cpf': cpf_cliente,
            'nascimento': nascimento_cliente,
            'numero': numero_cliente,
            'cnh': cnh_cliente
        }
        salvar_dados(dados_clientes, 'dados_clientes.json')
        print(f"\nCadastro realizado com sucesso!\nBem-vindo, {nome_cliente}!")   

def calcular_dias(data_retirada, data_devolucao):
    formato = "%d/%m/%Y"
    data_retirada = datetime.strptime(data_retirada, formato)
    data_devolucao = datetime.strptime(data_devolucao, formato)
    dias = (data_devolucao - data_retirada).days
    return dias


def main():

    while True:
        
        menuPrincipal()
        entrada_inicial = int(input('\nDigite a opção desejada: '))
        os.system('cls')
    
    
        match(entrada_inicial):
            case 1:
                while True:
                  os.system('cls')
                  entrada_adm =int(input("\n|1 - ENTRAR NO SISTEMA\n|2 - VOLTAR\n"))
                  os.system('cls')
                

                    
                  if(entrada_adm ==1):
                     user = input('Digite seu usuário: ')
                     senha = input('Digite sua senha: ')
                     
                     if user in dados_adm:
                         if dados_adm[user]['senha']== senha:
                            print('------------------------------------------------')
                            print('        |BEM VINDO ADMINISTRADOR|')
                            print('------------------------------------------------')
                            
                            while True:
                                print('\n1 - ADMINISTRADOR\n2 - LOCADORA\n3 - CLIENTE\n4 - SAIR')
                                entrada_adm2= int(input('\nDigite a opção desejada: '))
                                os.system('cls')
                                
                                match(entrada_adm2):
                                    
                                    case 1:
                                        escolha_adm = int(input('\n1 - ADICIONAR ADMINISTRADOR\n2 - EXCLUIR ADMINISTRADOR\n3 - ATUALIZAR ADMINISTRADOR\n4 - LISTAR ADMINISTRADORES\n5 - VOLTAR AO MENUR ANTERIOR\nDigite a opção desejada: '))

                                        match escolha_adm:
                                            case 1:
                                                print("CADASTRO DE  ADMINISTRADOR")
                                                usuario_adm =input("Digite o usuário do administrador que deseja ultilizar:  ")
                                                nome_comple_adm =input("Digite o nome e sobrenome do Administrador:  ")
                                                senha_adm =input("Digite senha do administrador:  ")
                      
                                                dados_adm[usuario_adm]={
                                                    "nome":nome_comple_adm,
                                                    "senha":senha_adm
                                                }
                                                os.system('cls')
                                                with open('dados_administradores.json', 'w') as f:
                                                    json.dump(dados_adm, f, indent=4)
                                                    print("Dados salvos com sucesso!")

                                                print('\n1 - ADMINISTRADOR\n2 - LOCADORA\n3 - CLIENTE\n4 - SAIR')
                                                entrada_adm2= int(input('\nDigite a opção desejada: '))
                                                os.system('cls')
                                           
                                            case 2:
                                                apagar_adm()

                                            case 3:
                                                atualizar_administrador()

                                            case 4:
                                                listar_administradores()
                                        
                                    case 2:
                                        while True:
                                            exibir_menu_adm_locadora()
                                            entrada_secundaria= int(input("Digite a opção desejada:  "))
                                            
                                            match(entrada_secundaria):
                                                case 1:
                                                
                                                    print("CADASTRO DE  LOCADORA")
                                                    nome_locadora =input("Digite o nome da locadora:  ")
                                                    login_locadora =input("Digite o login da locadora:  ")
                                                    codigo_locadora =input("Digite o codigo de sua locadora:  ")
                                                    senha_locadora =input("Digite senha da locadora:  ")
                                                    contato_locadora =input("Digite o numero para contato:  ")
                                                    endereco_locadora =input("Digite Endereço Locadora:  ")
                                                    
                                                    
                                                
                                                    dados_locadoras[nome_locadora]={
                                                    "login_locadora":login_locadora,
                                                    "codigo_locadora":codigo_locadora,
                                                    "senha_locadora":senha_locadora,
                                                    "contato_locadora":contato_locadora,
                                                    "endereco_locadora":endereco_locadora,
                                                }
                                                    os.system('cls')
                                                    salvar_dados(dados_locadoras, 'dados_locadora.json')
                                                    print(cor.VERDE+'LOCADORA CADASTRADA COM SUCESSO')

                                                    exibir_menu_adm_locadora()
                                                    entrada_secundaria= int(input("Digite a opção desejada:  "))
                                                    
                                                    
                                                case 2:
                                                    listar_locadora()
                                                
                                                    
                                                case 3:
                                                    
                                                    os.system('cls')
                                                    atualizar = input("Digite o nome do locadora a ser atualizado: ").strip()
    
                                                    with open('dados_locadora.json', 'r') as atualizar_locadora:
                                                      atualizacao = json.load(atualizar_locadora)
        
                                                       # Normaliza os nomes no dicionário para comparação
                                                    nomes_normalizados = {nome.lower(): nome for nome in atualizacao.keys()}
    
                                                        # Verifica se o nome do cliente existe
                                                    nome_key = nomes_normalizados.get(atualizar.lower())  # Usa .lower() para normalizar
    
                                                    if nome_key:
                                                       print('Atualizar Dados da locadora')
                                                       login_locadora = input('Digite O novo login: ')
                                                       senha_locadora= input('A nova Locadora: ')
                                                       contato_locadora = input('Digite  o Contato: ')
                                                       endereco_locadora = input('Digite o novo endereço locadora ')
        
                                                     # Atualiza os dados do cliente
                                                       atualizacao[nome_key] = {
                                                        'login_locadora': login_locadora,
                                                        'senha_locadora': senha_locadora,
                                                        'contato_locadora': contato_locadora,
                                                        'endereco': endereco_locadora
        }
        
                                                        # Salvar os dados no arquivo JSON
                                                       with open('dados_locadora.json', 'w') as salvar_dados:
                                                        json.dump(atualizacao, salvar_dados, indent=4)  # Salva os dados atualizados
        
                                                        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
                                                       print(f'Cliente {nome_key} atualizado com sucesso!')
                                                    else:
                                                        print(f"Locadora '{atualizar}' não encontrado.")
                                                    
                                                case 4:
                                                    
                                                    
                                                    apagar = input("Digite o nome da locadora a ser apagado: ").strip()  # Remove espaços em branco

                                                    with open('dados_locadora.json', 'r') as apagar_dados:
                                                     data = json.load(apagar_dados)

                                                     # Normaliza os nomes no dicionário para comparação
                                                     nomes_normalizados = {nome.lower(): nome for nome in data.keys()}

                                                      # Verifica se o nome do cliente existe
                                                     nome_key = nomes_normalizados.get(apagar.lower())  # Usa .lower() para normalizar

                                                     if nome_key:
                                                       data.pop(nome_key)  # Remove o cliente
            
                                                        # Salvar os dados atualizados no mesmo arquivo
                                                       with open('dados_locadora.json', 'w') as salvar_dados:
                                                         json.dump(data, salvar_dados, indent=4)  # Salva os dados atualizados
                                                       print("LOCADORA APAGADO COM SUCESSO")
                                                     else:
                                                          print(f"Cliente '{apagar}' não encontrado.")
                                                        
                                                 
                                                case 5:
                                                 os.system('cls')
                                                 print('FEATURE EM DESENVOLVIMENTO')
                                
                                                case 6:
                                                 os.system('cls')
                                                 print('VOLTANDO AO MENU PRINCIPAL')
                                                 break 
                                        
                                    
                                    case 3:
                                        while True:
                                            
                                            #MENU PRINCIPAL 
                                            exibir_menu()
                                            entrada_secundaria = int(input("Digite a Opção Desejada: "))
                                            
                                            match(entrada_secundaria):
                                                #ADMINISTRADOR
                                                case 1:
                                                    print('Cadastro de cliente')
                                                    nome_cliente = input('Digite seu nome e sobrenome: ')
                                                    cpf_cliente = input('Digite seu CPF: ')
                                                    nascimento_cliente = input('Digite sua data de nascimento: ')
                                                    numero_cliente = input('Digite seu número para contato: ')
                                                    cnh_cliente = input('Digite o número de sua CNH: ')
                                    
                                                    dados_clientes[nome_cliente] = {
                                                    'cpf': cpf_cliente,
                                                    'nascimento': nascimento_cliente,
                                                    'numero': numero_cliente,
                                                    'cnh': cnh_cliente
                                                         }
                                                    os.system('cls')
                                                    salvar_dados(dados_clientes, 'dados_clientes.json')
                                                    print(f'Cliente {nome_cliente} cadastrado com sucesso!')

                                                    exibir_menu()
                                                    entrada_secundaria = int(input("Digite a Opção Desejada: "))
                                                
                                                case 2:
                                                    os.system('cls')
                                                    listar_clientes()
                                                case 3:
                                                   os.system('cls')
                                                   atualizar_clientes()
                                                case 4:
                                                  os.system('cls')
                                                  apagar_usuario()
                                
                                                case 5:
                                                 os.system('cls')
                                                 print('FEATURE EM DESENVOLVIMENTO')
                                
                                                case 6:
                                                 os.system('cls')
                                                 print('VOLTANDO AO MENU PRINCIPAL')
                                                 break
                                
                                                case __:
                                                 print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                    
                                    case 4:
                                        print("VOLTANDO...")   
                                        break     
                     else:
                         print(cor.VERMELHO + "SENHA OU USUARIO INCORRETOS")
                         break
                         
                        
                                                    
                                            
                             
                
                  else:
                     print(cor.VERMELHO+ "VOLTANDO AO MENU ANTERIOR")
                     break
            
            case 2:
                while True:
                    # MENU LOCADORA
                    menuLocadora ()
                    locadora_entrada= int(input('Informe a opção desejada: '))
                    os.system('cls')
                    print ('=' * 50)
                    
                    # CADASTRAR LOCADORA   
                    if(locadora_entrada==1):
                        
                        nome_locadora = input('Digite o nome da locadora: \n')
                        senha = input('Digite sua senha: \n').lower ()
                        os.system('cls')
                        if nome_locadora in dados_locadoras:
                           if dados_locadoras[nome_locadora]['senha_locadora']== senha:
                            print ('=' * 50)
                            print (f'\nBem vindo {nome_locadora} !\n')
                            print ('=' * 50)

                            # MENU CARROS
                            print ('=' * 50)
                            print ('| 1 - LISTA DE CARROS |\n| 2 - CADASTRAR NOVO CARRO |\n| 3 - EXCLUIR CARRO |\n| 4 - VOLTAR AO MENU ANTERIOR |\n| 5 - VOLTAR AO MENU PRINCIPAL |\n| 6 - ENCERRAR O PROGRAMA |\n')
                            opc_carros = int(input('\nInforme a opção desejada: '))
                            os.system('cls')
                            print ('=' * 50)

                            # LISTA DE CARROS DE TODAS AS LOCADORAS
                            if (opc_carros == 1):
                                lista_carros ()

                            # CADASTRAMENTO DE CARROS
                            elif (opc_carros == 2):
                                locadora_carro = input ('Informe a locadora proprietária: ')
                                modelo = input ('Informe o modelo do carro: ')
                                marca = input ('Informe a marca: ')
                                tipo = input ('Informe o tipo (SUV, SEDAN, HATCH): ')
                                ano = input ('Informe o ano do carro: ')
                                cor = input ('Informe a cor do carro: ')
                                valor = int(input('Informe o valor da diaria: '))


                                dados_carros[locadora_carro]={
                                    "modelo": modelo,
                                    "marca": marca,
                                    "tipo": tipo,
                                    "ano": ano,
                                    "cor": cor,
                                    "valor": valor
                                }
                                os.system('cls')
                                salvar_carros(dados_carros, 'dados_carros.json')
                                print(f'{modelo} CADASTRADO COM SUCESSO!') 

                            # EXCLUIR/ DELETAR CARROS   
                            elif (opc_carros == 3):
                                print ('em construção')

                            # VOLTAR AO MENU LOCADORA
                            elif (opc_carros == 4):
                                menu_locadora ()

                            # VOLTA AO MENU PRINCIPAL
                            elif (opc_carros == 5):
                                menuPrincipal()

                            # ENCERRAR PROGRAMA    
                            elif (opc_carros == 6):
                                print ('Programa encerrado ...')
                                break 

                            # MENSAGEM DE OPÇÃO INVALIDA 
                            else:
                                print(cor.VERMELHO+ "SENHA OU USUARIO INCORRETOS")
                         
                            
                        
                    elif(locadora_entrada ==2):
                        
                            
                        print("CADASTRO DE  LOCADORA")
                        nome_locadora =input("Digite o nome da locadora:  ")
                        codigo_locadora =input("Digite o codigo de sua locadora:  ")
                        senha_locadora =input("Digite senha da locadora:  ")
                        contato_locadora =input("Digite o numero para contato:  ")
                        endereco_locadora =input("Digite Endereço Locadora:  ")
                        
                        
                      
                        dados_locadoras[nome_locadora]={
                          "codigo_locadora":codigo_locadora,
                          "senha_locadora":senha_locadora,
                          "contato_locadora":contato_locadora,
                          "endereco_locadora":endereco_locadora
                        }
                        os.system('cls')
                        salvar_locadora(dados_locadoras, 'dados_locadora.json')
                        print('LOCADORA CADASTRADA COM SUCESSO')

                    # LISTA DAS LOCADORAS  
                    elif(locadora_entrada == 3):
                        listar_locadora ()
                    
                    # EXCLUIR LOCADORA
                    elif (locadora_entrada == 4):
                        apagar_locadora()
                    
                    # VOLTAR AO MENU PRINCIPAL
                    elif (locadora_entrada == 5):
                        menuPrincipal()
                    
                    # ENCERRAR PROGRAMA
                    elif (locadora_entrada == 6):
                        print ('Programa encerrado...')
                        break
                    # OPÇÃO INVALIDA
                    else:
                        os.system('cls')
                        print(cor.VERMELHO+ "OPÇÃO INVALIDA")
                        
                            
            case 3:
                verificação_cliente = input('Você já é um cliente cadastrado? (s/n) ').lower()
                os.system('cls')
                if verificação_cliente == "s" :
                    nome_cliente = input('Digite seu nome: ')
                    os.system('cls')
                    if nome_cliente in dados_clientes:
                        print(f"Bem-vindo de volta, {nome_cliente}!\n")
                        cpf_cliente = dados_clientes[nome_cliente]['cpf']
                        print(f"Seu CPF: {cpf_cliente}\n")
                else:
                    print("Cliente não encontrado!\n")
                    cadastro_cliente()
                
                print('1-Atualizar informações \n2-aluguel de carros\n')
                decisao_03=int(input('digite a opçao desejada: '))
                os.system('cls')

                if decisao_03==1:
                    atualizar_clientes()

                elif decisao_03==2:
                    for locadora, dados in dados_locadoras.items():
                        endereco_locadora = dados.get('endereco_locadora', 'Endereço não disponível')
                        contato_locadora = dados.get('contato_locadora', 'Contato não disponível')
                        print(f"Locadora: {locadora} - Endereço: {endereco_locadora} - Contato: {contato_locadora}")
                    escolha_locadora=input('Qual a locadora de sua opção?')
                    os.system('cls')
                    for carro, dados in dados_carros.items():
                        marca = dados.get('marca', 'Marca não disponível')
                        ano = dados.get('ano', 'Ano não disponível')
                        tipo = dados.get('tipo', 'Tipo não disponível')
                        cor = dados.get('cor', 'Cor não disponível')
                        valor= dados.get('valor', 'Valor não disponivel')
                        print(f"Carro: {carro} - Marca: {marca} - Ano: {ano} - Tipo: {tipo} - Cor: {cor} - valor {valor}")
                    
                    escolha_carro = input('Escolha o carro desejado: ').strip()
                    os.system('cls')

                    dados_carro_escolhido = dados_carros.get(escolha_carro)
                    if dados_carro_escolhido:
                        valor_carro = dados_carro_escolhido.get('valor', 0)  # Valor específico do carro escolhido

                    
                        data_retirada = input('Digite a data de retirada (dd/mm/aaaa): ')
                        data_devolucao = input('Digite a data de devolução (dd/mm/aaaa): ')

                        dias_aluguel = calcular_dias(data_retirada, data_devolucao)     
                        
                        valor_total= dias_aluguel*valor_carro

                        print(f"\nResumo do aluguel:\nCarro: {escolha_carro}\nLocadora: {escolha_locadora}\n"
                            f"Data de Retirada: {data_retirada}\nData de Devolução: {data_devolucao}\n"
                            f"Duração: {dias_aluguel} dias\nValor Total: R${valor_total:.2f}")
                        print("\nObrigado por usar nosso sistema! Esperamos vê-lo novamente em breve.\n")



                                        
                    break
                      
                          
            case 4:
                print(cor.VERDE+"ENCERRANDO PROGRAMA...")
                break
            
            case __:
                print(cor.VERMELHO+" OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                
                        

                        
                    
                        
                        
        
    
    
    
    
if __name__ == "__main__":
    main()
    
    
