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

<img width="1331" height="1157" alt="schéma drawio" src="https://github.com/user-attachments/assets/44eabb9b-f890-42a8-847e-c9a598b533c3" />


