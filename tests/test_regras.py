import pytest
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario
from mini_biblioteca.emprestimos import Emprestimo

def test_emmprestimo_deixa_livro_indisponivel():
    livro = Livro("A", "B", "1")
    Emprestimo(livro, Usuario("Ana","123"))
    assert livro.disponivel is False

def test_nao_empresta_livro_indisponivel():
    livro = Livro("A","B","123")
    usuario = Usuario("Ana","123")
    Emprestimo(livro,usuario)
    with pytest.raises(ValueError):
        Emprestimo(livro,usuario)

def test_devolver_libera_livro():
    livro = Livro("A","B","123")
    emprestimo = Emprestimo(livro,Usuario("Ana","123"))
    emprestimo.devolver()
    assert emprestimo.ativo is False
    assert livro.disponivel is True
                  