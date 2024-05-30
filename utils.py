from getpass import getpass
import os

def valida_usuario():
    logado = False
    while True: 
        arquivo = open("arquivos/usuarios.txt", 'r')
        user_atual = input("Digite o usuario: ")
        senha_atual = getpass("Digite a senha: ")

        for i in arquivo:
          user_arquivo = i.split(";")[0]
          senha_arquivo = i.split(";")[1].replace("\n", "")

          if user_atual == user_arquivo and senha_atual == senha_arquivo:
            logado = True
            print("Logado com Sucesso!")

        if logado:
          return user_atual
        else:
          print("Usuário ou Senha Incorretas")
          return False

def cadastra_usuario():
  try:
    qtde_user = int(input("Quantos usuários gostaria de cadastrar? "))
    users = []
    passw = []

    for _ in range(qtde_user):
      users.append(input("\nQual o login do usuário: "))
      passw.append(getpass("Digite a senha do usuário: "))

    if not os.path.exists("arquivos/"):
        os.makedirs("arquivos")

    with open("arquivos/usuarios.txt", "a+") as arq_users:
      for indice, user in enumerate(users):
        arq_users.write(user + ";" + passw[indice])
        arq_users.write("\n")
  except:
    print("Digite um valor válido!")

# CADASTRA PRODUTOS
def cadastra_produtos():
  qtde_prods = int(input("Quantos produtos gostaria de cadastrar? "))
  produtos = []
  precos = []
  

  for _ in range(qtde_prods):
    produtos.append(input("\nQual o nome do produto: "))
    precos.append(float(input("Digite o preço do produto: ")))

  with open("arquivos/produtos.txt", "a+") as arq_prods:
    for indice, produto in enumerate(produtos):
      arq_prods.write(produto + ";" + str(precos[indice]))
      arq_prods.write("\n")

# COMPRA PRODUTOS
def compra_produtos():
  carrinho = []
  produtos = open("arquivos/produtos.txt", "r").readlines()
  while True:
    print("Esses são nossos produtos, caso queria cancelar o processo de compra, digite: SAIR")
    for indice, prod in enumerate(produtos):
      print("| ***---- ", indice, prod.split(";")[0] + " - R$", prod.split(";")[1].replace("\n", ""),   "---- *** |")
    print("-------------------------------------------------")

    escolha = input("Digite o número do produto que quer comprar ou SAIR: ")

    if "SAIR" == escolha.upper():
      return False
    while True:
      try:    
        print("Você escolheu o produto: ", produtos[int(escolha)].split(";")[0], " - R$ ", produtos[int (escolha)].split(";")[1].replace("\n", ""))
        break
      except:
        print("####### Digite um número válido! ######")
        continue
      
    adicionar = input("Deseja adicionar ao carrinho? S/N ")

    if adicionar.upper() == "S":
      while True:
        qtde = int(input("Qual quantidade deseja adicionar? "))
        if qtde <= 0:
          print("Digite uma quantidade maior do que 0")
          continue
        else:
          preco_produto = produtos[int (escolha)].split(";")[1].replace("\n","")
          carrinho.append([produtos[int(escolha)].split(";")[0],preco_produto, round(float(preco_produto) * qtde, 2), qtde])
          break
        

    continuar_comprando = input("Deseja continuar comprando? (S/N)").upper()
    if(continuar_comprando == "N"):
      return carrinho
    else:
      continue

def retirar_de_estoque(indice):
  pass
      
def salvar_compra(carrinho):
  if len(carrinho) > 0:
    vr_total = 0
    with open("arquivos/orcamento.txt", "w") as arq_orc:
      for indice, produto in enumerate(carrinho):
        ln = f"{indice+1} | Nome: {produto[0]} | Qtde: {produto[-1]} | Preço: R${produto[1]} | Vr Total: R${produto[2]}"
        arq_orc.write(ln+"\n")
        print(ln)
        vr_total += produto[2]
    print(f"\n############ VALOR TOTAL: R${round(vr_total,2)}")
    print("\nSalvando arquivo de orçamento. Obrigado por comprar conosco!")