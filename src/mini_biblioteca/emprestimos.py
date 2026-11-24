class Emprestimo:
    def __init__(self, livro, usuario):
        if not livro.disponivel:
            raise ValueError("O livro não está disponível")
        self.livro = livro
        self.usuario = usuario
        self.ativo = True
        livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True