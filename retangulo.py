class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def imprimir_atributos(self):
        print(f'A largura é: {self.largura}')
        print(f'A altura é: {self.altura}')