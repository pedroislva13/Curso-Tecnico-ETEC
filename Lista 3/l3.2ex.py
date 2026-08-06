usuario = input("Nome de usuário: ")
senha = input("Senha: ")

while senha == usuario:
    print("Erro: A senha não pode ser igual ao nome de usuário.")
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

print("Cadastro realizado com sucesso!")
