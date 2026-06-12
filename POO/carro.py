# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos
class Carro:

    # Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

        # Métodos
        # Método acelerar
        # Aumento será o valor recebido para aumentar a velocidade

    def acelerar(self, aumento):
        # self.velocidade = self.velocidade + aumento 
        self.velocidade += aumento

        print(f"O carro acelerou para {self.velocidade} km/h")

    # Método frear
    def frear(self, redução):
        # self.velocidade = self.velocidade - redução
        if self.velocidade - redução < 0:
            self.velocidade = 0
        else:
            self.velocidade -= redução

        print(f"O carro reduziu para {self.velocidade} km/h")

    # Metodo para existir informações
    def exibir_info (self):
        print("=== Informações do Carro ===")

        # Exibir os atributos do carro
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade} km/h")

# Criando um objeto da Classe Carro

# "carro1" é uma variável que recebe um objeto
carro1 = Carro("Chevrolet", "S10", 2013)

#  Chamando os métodos

#  o valor 50 será enviado para o parâmetro "aumento"
carro1.acelerar(50)

#  o valor 20 será enviado para o parâmetro "redução"
#  carro1.frear(redução)
carro1.frear(20)

# o valor as informacões da carro
carro1.exibir_info()

# # "carro2" é uma variável que recebe um objeto
# carro2 = Carro("BYD", "Dolphin Mini", 2025)

# # # Exibir informações do carro 2
# print(f"Marca: {carro2.marca}")
# print(f"Modelo: {carro2.modelo}")
# print(f"Ano: {carro2.ano}")

