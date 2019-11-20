class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Hello'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    print(luciano.filhos)
    luciano.sobrenome = 'Ramalho'
    print(luciano.__dict__)
    print(renzo.__dict__)
    print('Removing the "filhos" attribute from the "luciano" object')
    del luciano.filhos
    print(luciano.__dict__)


