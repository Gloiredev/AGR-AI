import sympy as sp
import numpy as np
import re
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor



def AGR(text):
    try:
        # 1. PRÉPARATION
        q = text.lower().strip()
        t = standard_transformations + (implicit_multiplication_application, convert_xor)
        
        # 2. CONSTANTES
        cst = {
            'pi': sp.pi, 'e': sp.exp(1), 'i': sp.I,
            'c': 299792458, 'g': 9.81, 'G': 6.67e-11,
            'h': 6.626e-34, 'r': 8.314, 'na': 6.022e23, 'kb': 1.38e-23
        }

        # 3. STATISTIQUES (Si l'utilisateur met des crochets [ ])
        if "[" in q and "]" in q:
            data = np.array(eval(q[q.find("["):q.rfind("]")+1]))
            return f"Résultat Ruphia : Moyenne {np.mean(data):.2f}, Médiane {np.median(data)}, Écart-type {np.std(data):.2f}"

        # 4. NETTOYAGE DES MOTS-CLÉS
        clean = q
        for v in ["calcule", "résous", "dérive", "intègre", "limite", "simplifie", "valeur de"]:
            if v in clean: clean = clean.split(v)[-1].strip()
        
        # 5. FIX TRIGO : Remplacer "sin5" par "sin(5)" et gérer les degrés
        clean = re.sub(r'(sin|cos|tan)(\d+)', r'\1(\2)', clean)
        if "deg" in clean:
            clean = re.sub(r'(\d+)\s*deg', r'(\1*pi/180)', clean)

        # 6. ANALYSE MATHÉMATIQUE
        expr = parse_expr(clean.replace('=', '-'), transformations=t, local_dict=cst)
        syms = list(expr.free_symbols)
        var = syms[0] if syms else sp.Symbol('x')

        # 7. MOTEUR DE DÉCISION (CORRIGÉ)
        if any(w in q for w in ["dérive", "diff"]):
            res = sp.diff(expr, var)
            sig = "Dérivation"
        elif any(w in q for w in ["intègre", "intégrale"]):
            res = sp.integrate(expr, var)
            sig = "Intégration"
        elif any(w in q for w in ["résous", "solution"]):
            res = sp.solve(expr, var)
            sig = "Solution"
        else:
            res = sp.simplify(expr)
            sig = "Résultat"

        # 8. LE FIX DÉCIMAL (Pour sin(5), cos(4), etc.)
        # Si le résultat est un nombre ou une expression sans variable (comme sin(5))
        if not res.free_symbols:
            val_dec = float(res.evalf())
            if val_dec == int(val_dec):
                res_final = int(val_dec)
            else:
                res_final = f"{res} ≈ {val_dec:.6f}"
        else:
            res_final = res

        return f"✨ Ruphia Astral : {sig} -> {res_final}"

    except Exception as e:
        return f"❌ Erreur Ruphia : Expression mal calculée."

# --- INTERFACE UTILISATEUR SIMPLE ---
if __name__ == "__main__":
    print("--- MOTEUR Agr Sumath CONNECTÉ ---")
    while True:
        
        user_input = input( "entrez votre commande et agr l'execute(que les maths) ou tapez 'quitter': ")
        if user_input.lower() == 'quitter': 
            print(AGR())
            break