from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario

def test_livro_comeca_disponivel():
    livro = Livro("Harry Potter", "JK", "L1")
    assert livro.disponivel is True

def test_usuario_guarda_dados():
    usuario = Usuario("Ana","123")
    assert usuario.nome == "Ana"
    assert usuario.id_usuario == "123"