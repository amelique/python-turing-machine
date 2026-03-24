from ALU import ALU
from assembleur import Assembleur 


class CPU: 

    #définition des registres
    
    def __init__(self,memoire):
        """
        Constructeur de la classe CPU.
        :param memoire
        """
        self.memoire = memoire          # liste d'instructions de 8 bits
        self.PC = 0                     # index d'instruction
        self.ACC = [0,0,0,0]            # accumulateur 4 bits
        self.running = True


    '''
    Lire l'instruction et actualiser le PC pour suivre le cours des instructions
    '''

    #aller chercher l'instruction dans la mémoire de l'objet CPU 
    def fetch(self):
        instr = self.memoire[self.PC]   # 8 bits
        self.PC += 1

        return instr


    def decode(self, bits):
        opcode = bits[:4]      # les 4 premiers bits
        operand = bits[4:]     # les 4 derniers bits
        return opcode, operand


    # ADDRESSE BINAIRE → INDEX BINAIRE : troubver les bts de l'instruction
    def adresse_binaire(self, operand):
        # operand = [0,0,1,0]
        # on retourne l'index correspondant dans la mémoire
        # en comparant binaire à binaire
        for index, instr in enumerate(self.memoire):
            # index en binaire sur 4 bits
            b = [
                (index >> 3) & 1,
                (index >> 2) & 1,
                (index >> 1) & 1,
                (index >> 0) & 1
            ]
            if b == operand:
                return index
        return 0   # fallback 


    # EXECUTE : exécuter l'instruction
    def execute(self, opcode, operand):

        # convertir operand binaire → index binaire
        adresse = self.adresse_binaire(operand)

        if opcode == [0,0,0,0]:   # HALT
            self.running = False
            return

        elif opcode == [0,0,0,1]: # LDA
            # charger les 4 bits de l'adresse
            self.ACC = self.memoire[adresse][4:]   # les 4 bits de droite

        elif opcode == [0,0,1,0]: # STA
            # stocker ACC dans les 4 bits de droite
            self.memoire[adresse][4:] = self.ACC[:]

        elif opcode == [0,0,1,1]: # ADD
            a = self.ACC
            b = self.memoire[adresse][4:]
            result = ALU.add(a, b)
            self.ACC = result[-4:]  # garder 4 bits

        else:
            print("Instruction inconnue :", opcode)
            self.running = False

    def step(self):
        instr = self.fetch()
        opcode, operand = self.decode(instr)
        self.execute(opcode, operand)

