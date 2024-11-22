from collections import defaultdict

class Grammar:
    """
    Clase que representa una gramática formal y proporciona métodos para calcular
    los conjuntos FIRST y FOLLOW para cada símbolo no terminal.
    """

    def __init__(self, productions, start_symbol):
        """
        Inicializa la gramática con las producciones y el símbolo inicial.

        :param productions: Diccionario donde las claves son símbolos no terminales y los valores son listas de producciones.
        :param start_symbol: El símbolo no terminal inicial de la gramática.
        """
        self.productions = productions  # Diccionario con producciones
        self.start_symbol = start_symbol
        self.non_terminals = set(productions.keys())  # Conjunto de símbolos no terminales
        self.terminals = set()  # Conjunto de símbolos terminales
        self.first_sets = defaultdict(set)  # Diccionario para conjuntos FIRST
        self.follow_sets = defaultdict(set)  # Diccionario para conjuntos FOLLOW
        self._compute_terminals()  # Identifica y almacena los símbolos terminales

    def _compute_terminals(self):
        """
        Identifica y almacena todos los símbolos terminales de la gramática.
        Un símbolo es terminal si no es un no terminal y no es la cadena vacía 'ε'.
        """
        for rhs_list in self.productions.values():
            for rhs in rhs_list:
                for symbol in rhs:
                    if symbol not in self.non_terminals and symbol != 'ε':
                        self.terminals.add(symbol)
        # Añadimos 'ε' a los terminales para facilitar el manejo
        self.terminals.add('ε')

    def compute_first_sets(self):
        """
        Calcula los conjuntos FIRST para todos los símbolos de la gramática.
        """
        # Inicializar los conjuntos FIRST para terminales
        for terminal in self.terminals:
            self.first_sets[terminal].add(terminal)

        # Iterar hasta que no haya cambios en los conjuntos FIRST
        changed = True
        while changed:
            changed = False
            for non_terminal in self.non_terminals:
                for production in self.productions[non_terminal]:
                    before = len(self.first_sets[non_terminal])
                    if not production:
                        # Producción que deriva en 'ε' (representada como una lista vacía)
                        self.first_sets[non_terminal].add('ε')
                    else:
                        i = 0
                        while True:
                            sym = production[i]
                            # Añadir FIRST(sym) menos 'ε' al FIRST del no terminal
                            self.first_sets[non_terminal].update(self.first_sets[sym] - {'ε'})
                            if 'ε' in self.first_sets[sym]:
                                i += 1
                                if i >= len(production):
                                    # Si todos los símbolos de la producción pueden derivar en 'ε'
                                    self.first_sets[non_terminal].add('ε')
                                    break
                            else:
                                break
                    after = len(self.first_sets[non_terminal])
                    if after > before:
                        # Se ha modificado el conjunto FIRST del no terminal
                        changed = True

    def compute_follow_sets(self):
        """
        Calcula los conjuntos FOLLOW para todos los símbolos no terminales de la gramática.
        """
        # Añadir '$' al conjunto FOLLOW del símbolo inicial
        self.follow_sets[self.start_symbol].add('$')

        # Iterar hasta que no haya cambios en los conjuntos FOLLOW
        changed = True
        while changed:
            changed = False
            for lhs in self.productions:
                for production in self.productions[lhs]:
                    # Inicializar follow_temp con FOLLOW(lhs)
                    follow_temp = self.follow_sets[lhs].copy()
                    # Recorrer la producción de derecha a izquierda
                    for symbol in reversed(production):
                        if symbol in self.non_terminals:
                            before = len(self.follow_sets[symbol])
                            # Añadir follow_temp al conjunto FOLLOW del símbolo actual
                            self.follow_sets[symbol].update(follow_temp)
                            after = len(self.follow_sets[symbol])
                            if after > before:
                                # Se ha modificado el conjunto FOLLOW del símbolo
                                changed = True
                            if 'ε' in self.first_sets[symbol]:
                                # Si 'ε' está en FIRST(symbol), actualizar follow_temp
                                follow_temp.update(self.first_sets[symbol] - {'ε'})
                            else:
                                # Si 'ε' no está en FIRST(symbol), establecer follow_temp a FIRST(symbol)
                                follow_temp = self.first_sets[symbol].copy()
                        else:
                            # Si el símbolo es terminal, actualizar follow_temp a FIRST(symbol)
                            follow_temp = self.first_sets[symbol].copy()

    def display_first_sets(self):
        """
        Muestra los conjuntos FIRST de todos los símbolos no terminales de la gramática.
        """
        print("\nConjuntos FIRST:")
        for non_terminal in sorted(self.non_terminals):
            first = ', '.join(sorted(self.first_sets[non_terminal]))
            print(f"FIRST({non_terminal}) = {{ {first} }}")

    def display_follow_sets(self):
        """
        Muestra los conjuntos FOLLOW de todos los símbolos no terminales de la gramática.
        """
        print("\nConjuntos FOLLOW:")
        for non_terminal in sorted(self.non_terminals):
            follow = ', '.join(sorted(self.follow_sets[non_terminal]))
            print(f"FOLLOW({non_terminal}) = {{ {follow} }}")

def parse_grammar():
    """
    Solicita al usuario que introduzca las producciones de la gramática y las procesa.

    :return: Una tupla que contiene el diccionario de producciones y el símbolo inicial.
    """
    productions = defaultdict(list)
    # Solicitar el símbolo inicial
    start_symbol = input("Introduce el símbolo inicial: ").strip()
    
    # Solicitar el número de producciones con validación
    while True:
        try:
            n = int(input("Introduce el número de producciones: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el número de producciones.")
    
    print("Introduce las producciones en el formato A -> α | β, usa 'ε' para la cadena vacía:")
    
    # Leer cada producción
    for _ in range(n):
        while True:
            line = input().strip()
            if '->' not in line:
                print("Formato incorrecto, por favor usa '->' para separar el lado izquierdo y derecho.")
                continue
            lhs, rhs = line.split('->')
            lhs = lhs.strip()
            # Dividir las alternativas de producción usando '|'
            alternatives = rhs.strip().split('|')
            for alternative in alternatives:
                # Dividir cada alternativa en símbolos
                production = alternative.strip().split()
                if production == ['ε']:
                    # Representar 'ε' como una lista vacía
                    productions[lhs].append([])
                else:
                    productions[lhs].append(production)
            break  # Salir del bucle interno una vez que la producción ha sido procesada correctamente
    return productions, start_symbol

def main():
    """
    Función principal que ejecuta el programa.
    """
    # Parsear las producciones y el símbolo inicial introducidos por el usuario
    productions, start_symbol = parse_grammar()
    
    # Crear una instancia de Grammar con las producciones y el símbolo inicial
    grammar = Grammar(productions, start_symbol)
    
    # Calcular los conjuntos FIRST y FOLLOW
    grammar.compute_first_sets()
    grammar.compute_follow_sets()

    # Mostrar los resultados
    grammar.display_first_sets()
    grammar.display_follow_sets()

if __name__ == "__main__":
    main()
