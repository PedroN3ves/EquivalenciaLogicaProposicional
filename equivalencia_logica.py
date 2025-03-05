#Necessário a biblioteca simpy do python
from sympy import symbols, simplify_logic
from sympy.logic.boolalg import Or, And, Not, Implies, Equivalent

def verificar_equivalencia(expr1: str, expr2: str):
    #definindo os termos
    P, Q, R = symbols("P Q R")
    
    contexto = {"P": P, "Q": Q, "R": R, "Or": Or, "And": And, "Not": Not, "Implies": Implies, "Equivalent": Equivalent}
    exp1 = eval(expr1, contexto)
    exp2 = eval(expr2, contexto)
    
    return simplify_logic(exp1) == simplify_logic(exp2)

if __name__ == "__main__":
    try:
        s1 = input("Digite a primeira expressao (use 'P','Q' ou 'R' e 'And', 'Or', 'Not', 'Implies', 'Equivalent'): ")
        s2 = input("Digite a segunda expressao (use 'P','Q' ou 'R' e 'And', 'Or', 'Not', 'Implies', 'Equivalent'): ")
        
        if verificar_equivalencia(s1, s2):
            print("As expressoes sao logicamente equivalentes.")
        else:
            print("As expressoes NAO sao logicamente equivalentes.")
    except Exception as e:
        print(f"Erro ao processar as expressoes: {e}")
