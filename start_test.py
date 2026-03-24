from assembleur import Assembleur
from ALU import ALU
from CPU import CPU

program = [
    "LDA 4",   # charger la valeur en case 4
    "ADD 5",   # additionner la valeur en case 5
    "STA 6",   # stocker le résultat en case 6
    "HALT",
    "DATA 3",  # case 4 : valeur 3
    "DATA 5",  # case 5 : valeur 5
    "DATA 0",  # case 6 : résultat attendu = 8
]

memory = Assembleur.assemble(program)     
cpu_test = CPU(memory) # création d'un processeur avec ses conditions initiales par défaut et memory issue du program              

while cpu_test.running:              
    cpu_test.step()
#Tant que le processeur n’a pas reçu HALT, il exécute des cycles.

memory = Assembleur.assemble(program)
print("Mémoire brute :", len(memory), "cases")
for i, case in enumerate(memory):
    print(f"  [{i}] {case}")


 
print("Mémoire après avoir caluclé :", cpu_test.memoire)