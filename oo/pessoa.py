class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Hello'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    #class attribute
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    #the class attributes all come from the same place
    print('Pessoa:', id(Pessoa.olhos), 'luciano:', id(luciano.olhos), 'renzo:', id(renzo.olhos))
    #the dunder dict doesn't show the class attributes by default
    #if you alter the class attribute for an object then it shows on the
    #dunder dict list
    luciano.olhos = 1
    print(luciano.__dict__)
    #obviously the object address for the luciano "olhos" attribute changes
    print('Pessoa:', id(Pessoa.olhos), 'luciano:', id(luciano.olhos), 'renzo:', id(renzo.olhos))
    #static methods
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    #class methods
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())
