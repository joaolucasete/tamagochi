# coding: utf-8
from random import randint
import tamagochidb
import logger


class Tamagochi:
    def __init__(self):
        self.nome = 'sem_nome'
        self.nivel = 0
        self.experiencia = 0
        self.fome = 0
        self.vida = 100
        self.energia = 100
        self.felicidade = 100
        self.vivo = True

    # printar
    def printar(self, metodo):
        if callable(metodo):
            print(metodo())
        else:
            print(metodo)

    # save in database and add in log
    def save(self, name):
        tamagochidb.adicionar(self.nome, self.nivel)
        logger.log_info(f"Tamagochi criado - Nome: {tamagochi.nome}")

    # Logger
    def acoes_log(self, acao):
        logger.log_info(f"Nome: {tamagochi.nome} - {acao}")

    # verificar nome
    def verificar_nome(self, name):
        while self.nome == "":
            self.nome = input("Nome: ").strip()
        self.save(name)

    # nome
    def set_nome(self, name):
        return f"O nome do seu tamagochi é {self.nome}."

    # nivel
    def set_nivel(self):
        return f"Nivel: {self.nivel}"

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nome} upou para o nível {self.nivel}")

    # experiencia
    def set_xp(self):
        pass

    def subir_xp(self):
        pass

    # vida
    def set_vida(self):
        return f"Vida: {self.vida}"

    def subir_vida(self):
        n = randint(1, 10)
        self.vida += n

    def descer_vida(self):
        n = randint(1, 10)
        self.vida -= n

    # fome
    def set_fome(self):
        return f"Fome: {self.fome}"

    def subir_fome(self):
        n = randint(1, 10)
        self.fome += n

    def descer_fome(self):
        n = randint(1, 10)
        self.fome -= n

    # energia
    def set_energia(self):
        return f"Energia: {self.energia}"

    def subir_energia(self):
        n = randint(1, 10)
        self.energia += n

    def descer_energia(self):
        n = randint(1, 10)
        self.energia -= n

    # felicidade
    def set_felicidade(self):
        return f"Felicidade: {self.felicidade}"

    def subir_felicidade(self):
        n = randint(1, 10)
        self.felicidade += n
        if self.felicidade >= 0:
            self.felicidade = 100

    def descer_felicidade(self):
        n = randint(1, 10)
        self.felicidade -= n
        if self.felicidade <= 0:
            self.felicidade = 0
            print("Depressivo")

    # Profile e Status

    def mostrar_status(self):
        self.printar(f"Nivel: {self.nivel}")
        self.printar(f"Vida: {self.vida}")
        self.printar(f"Fome: {self.fome}")
        self.printar(f"Energia: {self.energia}")
        self.printar(f"Felicidade: {self.felicidade}")

    def mostrar_profile(self):
        self.printar(f"O nome do seu tamagochi é {self.nome}.")
        self.mostrar_status()

    # Ações

    def brincar(self):
        self.subir_felicidade()
        self.subir_fome()
        self.descer_energia()
        self.acoes_log("Brincar")

    def comer(self):
        self.descer_fome()
        self.subir_energia()
        self.acoes_log("comer")

    def dormir(self):
        self.subir_fome()
        self.subir_energia()
        self.acoes_log("Dormir")

# inicia o projeto
if __name__ == '__main__':
    tamagochi = Tamagochi()
    tamagochi.nome = "Jabe"
    tamagochi.verificar_nome(tamagochi.nome)
    tamagochi.mostrar_profile()
    tamagochi.brincar()
    tamagochi.mostrar_status()
    tamagochi.comer()
    tamagochi.mostrar_status()
    tamagochi.dormir()
    tamagochi.mostrar_status()
