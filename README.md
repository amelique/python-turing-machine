Ce projet est un simulateur pédagogique d'une architecture CPU 4-bits simplifiée. Il comprend un Assembleur pour convertir des instructions mnémotechniques en binaire, une ALU (Unité Arithmétique et Logique) pour les calculs, et une unité CPU pour gérer le cycle d'exécution (Fetch/Decode/Execute).

# Structure du projet 
Le simulateur est divisé en trois modules principaux :
- assembleur.py : Convertit le langage assembleur (texte) en listes de bits (machine code).
- ALU.py : Gère les opérations logiques et arithmétiques (notamment l'addition binaire avec gestion de retenue).
- CPU.py : Le cœur du système. Il contient les registres (PC, Accumulateur), la mémoire et gère le cycle de traitement.
- start_test.py : script Python pour instancier l'assembleur et le CPU 

# Architecture 
Registres :
- ACC (Accumulateur) : 4 bits.
- PC (Program Counter) : Index de l'instruction courante.
- Mémoire : Liste de mots de 8 bits (4 bits d'Opcode + 4 bits d'Opérande).
- Bus de données : 4 bits.

Mnémonique,Opcode,Description
HALT,0000,Arrête l'exécution du programme.
LDA,0001,Load : Charge la valeur située à l'adresse mémoire dans l'accumulateur.
STA,0010,Store : Stocke la valeur de l'accumulateur à l'adresse mémoire spécifiée.
ADD,0011,Add : Additionne la valeur à l'adresse mémoire à l'accumulateur.
DATA,----,Directive assembleur pour stocker une valeur brute en mémoire.

