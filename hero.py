class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo.lower() ==  "mago":
            ataque = "Magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "Espada"
        elif self.tipo.lower() ==  "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"   

        else:
            ataque = "Tipo Desconhecido"         


        return print(f'O {self.tipo} atacou usando {ataque}')


ninja = Hero("João",24,"ninja")

ninja.atacar()

mago = Hero("Maria",15,"MAGO")

mago.atacar()

guerreiro = Hero("Ana",22,"guerreiro")

guerreiro.atacar()

monge =  Hero("Gabriel",21,"monge")

monge.atacar()
           