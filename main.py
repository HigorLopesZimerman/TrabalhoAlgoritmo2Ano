from livros import adicionar_livro, buscar_livro, excluir_livro, listar_livros




def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Menu de Livros")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            menu_livros()
        elif opcao == "2":
            print("Saindo do sistema...")
            break
        


def menu_livros():
    while True:
        print("\nMenu de Livros")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Excluir Livro")
        print("4. Listar Livros")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cod_livro = int(input("Código do Livro: "))
            titulo = input("Título: ")
            cod_autor = int(input("Código do Autor: "))
            cod_categoria = int(input("Código da Categoria: "))
            ano_publicacao = int(input("Ano de Publicação: "))
            adicionar_livro(cod_livro, titulo, cod_autor, cod_categoria, ano_publicacao)
            print("Livro adicionado com sucesso!")
        
        elif opcao == "2":
            cod_livro = int(input("Código do Livro a buscar: "))
            livro = buscar_livro(cod_livro)
            if livro:
                print(f"\nLivro encontrado: ")
                print('-' * 120)
                print(f"Código: {livro.get('cod_livro', 'N/A')} | "
              f"Título: {livro.get('titulo', 'N/A')} | "
              f"Autor: {livro.get('cod_autor', 'N/A')} | "
              f"Categoria: {livro.get('cod_categoria', 'N/A')} | "
              f"Ano: {livro.get('ano_publicacao', 'N/A')} | "
              f"Disponibilidade: {livro.get('disponibilidade', 'N/A')}")
                print('-' * 120)
            else:
                print("Livro não encontrado.")
        
        elif opcao == "3":
            cod_livro = int(input("Código do Livro a excluir: "))
            if excluir_livro(cod_livro):
                print("Livro excluído com sucesso!")
            else:
                print("Falha ao excluir o livro.")
        
        elif opcao == "4":
            listar_livros()
        
        elif opcao == "5":
            break
        
        else:
            print("Opção inválida. Tente novamente.") 
            
            
if __name__ == "__main__":
    menu_principal()