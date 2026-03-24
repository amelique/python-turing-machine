class Assembleur:
    @staticmethod
    def conversion_binaire(chiffre):
        n = int(chiffre)
        binaire = [0, 0, 0, 0]
        for i in range(4):
            binaire[3-i] = n % 2
            n = n // 2
        return binaire

    @staticmethod
    def assemble(program):
        memoire = []
        for elem in program:

            if elem == "HALT":
                memoire.append([0,0,0,0, 0,0,0,0])
                continue

            instr_mnemo, operande = elem.split(" ", 1)

            if instr_mnemo == "DATA":
                valeur_bits = Assembleur.conversion_binaire(operande)
                memoire.append([0,0,0,0] + valeur_bits)
                continue

            if instr_mnemo == "LDA":
                opcode = [0,0,0,1]
            elif instr_mnemo == "ADD":
                opcode = [0,0,1,1]
            elif instr_mnemo == "STA":
                opcode = [0,0,1,0]
            else:
                opcode = [0,0,0,0]

            operand_bits = Assembleur.conversion_binaire(operande)
            memoire.append(opcode + operand_bits)  

        return memoire