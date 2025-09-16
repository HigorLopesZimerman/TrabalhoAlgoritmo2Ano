from arvore import Arvore
from arquivo import ler_arquivo, salvar_arquivo


livros = ler_arquivo("livros.json")

arvore_livros = None
for pos, livro in enumerate(livros):
    key = int(livro["cod_livro"])   
    if arvore_livros is None:
        arvore_livros = Arvore(key, pos)
    else:
        arvore_livros.add_child(key, pos)




def adicionar_livro(cod_livro, titulo, cod_autor, cod_categoria, ano_publicacao):
    global livro, arvore_livros
    novo = {
        "cod_livro": int(cod_livro),   
        "titulo": titulo,
        "cod_autor": int(cod_autor),
        "cod_categoria": int(cod_categoria),
        "ano_publicacao": int(ano_publicacao),
        "disponibilidade": "disponivel"
    }
    pos = len(livros)
    livros.append(novo)
    salvar_arquivo("livros.json", livros)

    if arvore_livros is None:
        arvore_livros = Arvore(cod_livro, pos)
    else:
        arvore_livros.add_child(cod_livro, pos)

# consulta livro
def buscar_livro(cod_livro):
    pos = arvore_livros.search(int(cod_livro))
    if pos is None:
        return None
    return livros[pos]

#excluir livro
def excluir_livro(cod_livro):
    global arvore_livros, livros
    if arvore_livros is None:
        print("Livro não encontrado!")
        return False 
    
    pos = arvore_livros.search(cod_livro)
    if pos is None:
        print("Livro não encontrado!")
        return False
    
    livros.pop(pos)
    salvar_arquivo("livros.json", livros)

    arvore_livros = None
    for pos, livro in enumerate(livros):
        if arvore_livros is None:
            arvore_livros = Arvore(livro["cod_livro"], pos)
        else:
            arvore_livros.add_child(livro["cod_livro"], pos)
            
    return True


def listar_livros():
    global arvore_livros
    if arvore_livros is None:
        print("Nenhum livro cadastrado.")
        return

    livros = ler_arquivo("livros.json")
    livro_ordem = arvore_livros.crescente()

    print("\nLista de Livros")
    print('-' * 120)
    for item in livro_ordem:
        pos = item["pos"]
        if 0 <= pos < len(livros):
            livro = livros[pos]
            print(f"Código: {livro.get('cod_livro', 'N/A')} | "
                  f"Título: {livro.get('titulo', 'N/A')} | "
                  f"Autor: {livro.get('cod_autor', 'N/A')} | "
                  f"Categoria: {livro.get('cod_categoria', 'N/A')} | "
                  f"Ano: {livro.get('ano_publicacao', 'N/A')} | "
                  f"Disponibilidade: {livro.get('disponibilidade', 'N/A')}")
    print('-' * 120)

