biblioteca = []

def adicionarLivro(titulo, autor, ano):
    livro = {'titulo': titulo, 'autor': autor, 'ano': ano}
    biblioteca.append(livro)
    print(f"Livro '{titulo}' adicionado com êxito!")

def listarLivros():
    if not biblioteca:
        print("Nenhum livro encontrado na biblioteca.")
        return
    for i, livro in enumerate(biblioteca, start=1):
        print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

def buscarPorTitulo(titulo):
    encontrados = []
    for livro in biblioteca:
        if titulo.lower() in livro['titulo'].lower():
            encontrados.append(livro)

    if not encontrados:
        print(f"Nenhum livro encontrado com o título: {titulo}")
        return
    for i, livro in enumerate(encontrados, start=1):  # Corrigido para usar 'encontrados'
        print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

def menu():
    while True:
        print("\nMenu da Biblioteca")
        print("1. Adicionar livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Sair")

        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação do livro: ")
            adicionarLivro(titulo, autor, ano)
        elif escolha == 2:
            listarLivros()
        elif escolha == 3:
            titulo = input("Digite o título do livro: ")
            buscarPorTitulo(titulo)
        elif escolha == 4:
            print("Saindo do programa...")
            break
        else:
            print("ERRO!!!\nDigite uma opção válida")

menu()
