ARQUIVO = "pessoas.txt"


def carregar_pessoas():
    pessoas = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    nome, idade = linha.split(";")
                    pessoas.append({"nome": nome, "idade": int(idade)})
    except FileNotFoundError:
        pass
    return pessoas


def salvar_pessoas(pessoas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for pessoa in pessoas:
            arquivo.write(f"{pessoa['nome']};{pessoa['idade']}\n")


def ler_nome():
    while True:
        nome = input("Nome: ").strip()
        if nome.replace(" ", "").isalpha():
            return nome.title()
        print("Nome inválido! Use apenas letras.")


def ler_idade():
    while True:
        idade = input("Idade: ").strip()
        if idade.isdigit() and 0 <= int(idade) <= 120:
            return int(idade)
        print("Idade inválida! Digite um número entre 0 e 120.")


def listar(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    print("\n--- Pessoas cadastradas ---")
    for numero, pessoa in enumerate(pessoas, start=1):
        print(f"{numero}. {pessoa['nome']} - {pessoa['idade']} anos")


def cadastrar(pessoas):
    print("\n--- Novo cadastro ---")
    nome = ler_nome()
    idade = ler_idade()
    pessoas.append({"nome": nome, "idade": idade})
    salvar_pessoas(pessoas)
    print("Pessoa cadastrada com sucesso!")

def remover(pessoas):
    listar(pessoas)
    if not pessoas:
        return

    numero = input("Número da pessoa que deseja remover: ").strip()
    if not numero.isdigit() or not 1 <= int(numero) <= len(pessoas):
        print("Número inválido!")
        return

    pessoa = pessoas[int(numero) - 1]
    resposta = input(f"Tem certeza que deseja remover {pessoa['nome']}? (s/n): ").lower()
    if resposta == "s":
        pessoas.remove(pessoa)
        salvar_pessoas(pessoas)
        print("Pessoa removida!")
    else:
        print("Remoção cancelada.")

def main():
    pessoas = carregar_pessoas()
    while True:
        print("\n===== CADASTRO DE PESSOAS =====")
        print("1 - Listar pessoas")
        print("2 - Cadastrar pessoa")
        print("3 - Remover pessoa")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar(pessoas)
        elif opcao == "2":
            cadastrar(pessoas)
        elif opcao == "3":
            remover(pessoas)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


main()