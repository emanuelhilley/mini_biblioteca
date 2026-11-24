from .livros import Livro
from .usuarios import Usuario
from .emprestimos import Emprestimo

def executar():
    u = Usuario("Ana", "123")
    l = Livro("Harry Potter","JK","L1")
    e = Emprestimo(l,u)
    print(f"Emprestado: {l.titulo}, Disponivel: {l.disponivel}")
    e.devolver()
    print(f"Devolvido|Disponível: {l.disponivel}, Ativo: {e.ativo}")

if __name__ == "__main__":
    executar()