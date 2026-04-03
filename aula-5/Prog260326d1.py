from datetime import datetime

# 1. Primeira Superclasse
class Relogio:
    def mostrar_hora(self):
        agora = datetime.now()
        hora = agora.strftime("%H:%M:%S")
        return hora

# 2. Segunda Superclasse
class Calendario:
    def mostrar_data(self):
        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y")
        return data

# 3. Subclasse que herda de AMBAS (Herança Múltipla)
class Smartwatch(Relogio, Calendario):
    def mostrar_tudo(self):
        # Ela tem acesso aos métodos de ambas as "mães"
        hora = self.mostrar_hora()
        data = self.mostrar_data()
        print(f"Smartwatch - Data: {data} | Hora: {hora}")

# 4. Programa Principal
if __name__ == "__main__":
    meu_relogio = Smartwatch()
    meu_relogio.mostrar_tudo()
