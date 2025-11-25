# Função para adicionar contatos
def adicionar_contato(contatos, nome):
    contato = {
        "contato": nome,
        "favorito": False
    }
    contatos.append(contato)
    print(f"Contato '{nome}' foi adicionado com sucesso!")

# Função para ver a agenda de contatos
def ver_contato(contatos):
    print("\nAgenda de contatos:")
    if not contatos:
        print("Nenhum contato salvo ainda.")
        return

    for indice, contato in enumerate(contatos, start=1):
        status = "x" if contato["favorito"] else " "
        print(f"{indice}. [{status}] {contato['contato']}")

# Função para atualizar os contatos
def atualizar_contato(contatos, indice_contato, novo_nome):
    indice = indice_contato - 1
    if 0 <= indice < len(contatos):
        contatos[indice]["contato"] = novo_nome
        print("Contato atualizado com sucesso!")
    else:
        print("Contato inexistente!")

# Função para marcar um contato como favorito
def marcar_favorito(contatos, indice_contato):
    indice = indice_contato - 1
    if 0 <= indice < len(contatos):
        contatos[indice]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito!")
    else:
        print("Contato inexistente!")

# Função para deletar contatos favoritos
def deletar_contatos(contatos):
    contatos[:] = [c for c in contatos if not c["favorito"]]
    print("Contatos favoritos foram removidos!")


contatos = []

# Looping para ver as opções da agenda de contato
while True:
    print("\nAgenda de contatos")
    print("1 - Salvar contato")
    print("2 - Ver contatos")
    print("3 - Editar contato")
    print("4 - Deletar contatos favoritos")
    print("5 - Marcar contato como favorito")
    print("6 - Sair")

    escolha = input("Escolha uma opção: ")

    # Usando IF, ELIF e ELSE, para cada função do gerenciador
    if escolha == "1":
        nome = input("Nome do contato: ")
        adicionar_contato(contatos, nome)

    elif escolha == "2":
        ver_contato(contatos)

    elif escolha == "3":
        ver_contato(contatos)
        indice = int(input("Número do contato para editar: "))
        novo_nome = input("Novo nome: ")
        atualizar_contato(contatos, indice, novo_nome)

    elif escolha == "4":
        deletar_contatos(contatos)

    elif escolha == "5":
        ver_contato(contatos)
        indice = int(input("Número do contato para favoritar: "))
        marcar_favorito(contatos, indice)

    elif escolha == "6":
        print("Programa finalizado!")
        break

    else:
        print("Opção inválida, tente de novo.")
