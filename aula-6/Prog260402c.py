class Calculadora:
    # Simulando sobrecarga usando parâmetros com valor padrão (None)
    def calcular_area(self, lado_a, lado_b=None):
        if lado_b is not None:
            # Se recebeu dois argumentos, calcula a área de um retângulo
            area = lado_a * lado_b
            print(f"Calculando Retângulo: {lado_a} x {lado_b} = {area}")
        else:
            # Se recebeu apenas um, calcula a área de um quadrado
            area = lado_a ** 2
            print(f"Calculando Quadrado: {lado_a}² = {area}")
        return area

# --- Programa Principal ---
if __name__ == "__main__":
    calc = Calculadora()

    # Chamada 1: "Sobrecarga" com 1 parâmetro
    calc.calcular_area(10)

    # Chamada 2: "Sobrecarga" com 2 parâmetros
    calc.calcular_area(10, 5)