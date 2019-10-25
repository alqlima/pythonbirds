class Pessoa:
    def __init__(self, *filhos, nome=None, idade=99):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    André = Pessoa(nome='André')
    Silvana = Pessoa(André, nome='Silvana')
    print(Pessoa.cumprimentar(Silvana))
    print(id(Silvana))
    print(Silvana.cumprimentar())
    print(Silvana.nome)
    print(Silvana.idade)
    for filho in Silvana.filhos:
        print(filho.nome)




