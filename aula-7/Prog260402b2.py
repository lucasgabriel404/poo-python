from abc import ABC, abstractmethod

# --- TIPO 1: POLIMORFISMO DE SOBRESCRITA (HERANÇA) ---
class MetodosDosBichos(ABC):
    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def locomover(self):
        pass


class Cachorro(MetodosDosBichos):
    def emitir_som(self):
        return "Au Au!"
    
    def caminhar(self):
        return "toc toc toc the dog is on the walk!"

class Gato(MetodosDosBichos):
    def emitir_som(self):
        return "Miau!"
    
    def caminhar(self):
        return "pic pic pic the cat is on the walk!"

# --- TIPO 2: POLIMORFISMO DE INTERFACE (DUCK TYPING) ---
# Esta classe NÃO herda de MetodosDosBichos, mas tem o MESMO método
class Radio:
    def emitir_som(self):
        return "Tocando música... 🎶"

# --- FUNÇÃO POLIMÓRFICA ---
def iniciar_barulho(objeto):
    # O Python não pergunta "quem é você?", mas sim "você sabe emitir_som()?"
    print(f"O som emitido é: {objeto.emitir_som()}")

def iniciar_caminhada(objeto):
    # O Python não pergunta "quem é você?", mas sim "você sabe caminhar()?"
    print(f"A caminhada é mais ou menos assim: {objeto.caminhar()}")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Criando uma lista com objetos de diferentes tipos
    dispositivos_sonoros = [Cachorro(), Gato()]

    print("--- Executando Polimorfismo ---")
    for item in dispositivos_sonoros:
        iniciar_barulho(item)
        iniciar_caminhada(item)