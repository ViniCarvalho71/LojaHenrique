import utils
while True:
  login_ou_cadastro = input("Digite 'login' para realizar um login ou 'cadastrar' para realizar o cadastro de um novo usuário: ").lower()
  if(login_ou_cadastro == 'login' ):

    print("Por favor, faça seu login para acessar nossa loja:")
    try:
      user_atual = utils.valida_usuario()

      if type(user_atual) == bool:
        exit()
      else:
        print("-------------------------------------------------")
        print("| ***---- BEM-VINDO ", user_atual ,"---- *** |")

        

        while True:
          comprar_ou_adicionar_produtos = input("Digite 'comprar' se deseja comprar novos produtos ou 'adicionar' se deseja repor estoque:").lower()
          if (comprar_ou_adicionar_produtos == 'comprar'):
            try:
                resp = utils.compra_produtos()
                if(resp == False):
                  break
                utils.salvar_compra(resp)
                  
            except FileNotFoundError:
              print("Não há produtos cadastrados!")
              continue
          elif (comprar_ou_adicionar_produtos == 'adicionar'):
            utils.cadastra_produtos()
          else:
            print("Digite uma opção válida")
    except FileNotFoundError:
      print("Não há nenhum usário cadastrado ainda.")
      continue
    
  elif (login_ou_cadastro == 'cadastrar'):
      utils.cadastra_usuario()
  else:
      print("Digite um opção válida!")
      continue
