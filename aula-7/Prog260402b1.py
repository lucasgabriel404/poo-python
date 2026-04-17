from abc import ABC, abstractmethod

# --- TIPO 1: POLIMORFISMO DE SOBRESCRITA (HERANÇA) ---
class MetodosDosBichos(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
    @abstractmethod
    def locomover(self):
        pass
    @abstractmethod
    def dormir(self):
        pass

class Cachorro(MetodosDosBichos):
    def emitir_som(self):
        return "Au Au!"
    def locomover(self, locomover="andar"):
        return locomover
    def dormir(self, nivel=8):
        if nivel==8 or nivel==12 or nivel==18: return nivel
        else: return 0

class Gato(MetodosDosBichos):
    def emitir_som(self):
        return "Miau!"
    def locomover(self, locomover="andar"):
        return locomover
    def dormir(self, nivel=8):
        if nivel==8 or nivel==12 or nivel==18: return nivel
        else: return 0

# --- TIPO 2: POLIMORFISMO DE INTERFACE (DUCK TYPING) ---
# Esta classe NÃO herda de EmissorSom, mas tem o MESMO método
class Radio:
    def emitir_som(self):
        return "Tocando música... 🎶"

# --- FUNÇÃO POLIMÓRFICA ---
def iniciar_barulho(objeto):
    # O Python não pergunta "quem é você?", mas sim "você sabe emitir_som()?"
    print(f"O som emitido é: {objeto.emitir_som()}")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando uma lista com objetos de diferentes tipos
    dispositivos_sonoros = [Cachorro(), Gato(), Radio()]
    Dog=Cachorro(); Cat=Gato()
    print("--- Executando Polimorfismo para Dispositivos Sonoros ---")
    for item in dispositivos_sonoros:
        iniciar_barulho(item)
    print("--- Executando Sobrecarga para Locomover e Dormir ---")
    print("CACHORRO")
    print("Eu vou", Dog.locomover())
    print("Eu vou", Dog.locomover("correr"))
    print("Eu vou", Dog.locomover("voar"))
    print("GATO")
    print("Eu vou dormir", Cat.dormir(), "horas")
    print("Eu vou dormir", Cat.dormir(12), "horas")
    print("Eu vou dormir", Cat.dormir(18), "horas")
    print("Eu vou dormir", Cat.dormir(20), "horas")
