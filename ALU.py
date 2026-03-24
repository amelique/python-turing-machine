class ALU :

    '''
    Fonctions de prérequis au calcul
    '''
    @staticmethod
    def lenmax(a,b): 
        if len(a)> len(b) : 
            return(len(a))
        else : 
            return(len(b))

    @staticmethod
    def harmoniser(a,b):
        liste_a= [0]*ALU.lenmax(a,b)
        liste_b= [0]*ALU.lenmax(a,b)

        for i in range(1,len(a)+1) : 
            liste_a[len(liste_a)-i] = a[len(a)-i]

        for i in range(1,len(b)+1) : 
            liste_b[len(liste_b)-i] = b[len(b)-i]
        return(liste_a, liste_b)




    '''
    Addition
    '''
    @staticmethod
    def add(a,b): 
        a,b = ALU.harmoniser(a,b)

        c= [0]*(ALU.lenmax(a,b)+1)
        retenue=0
        for cur in range(ALU.lenmax(a,b)-1, -1, -1):
            if retenue == 0 :
                if a[cur] == 0 : 
                    if b[cur] == 0 : 
                        c[cur+1] = 0
                    else : 
                        c[cur+1] = 1
                if a[cur] == 1 : 
                    if b[cur] ==0 : 
                        c[cur+1] = 1
                    else : 
                        c[cur+1] = 0 
                        retenue = 1
            else : #retenue ==1
                if a[cur] == 0 : 
                    if b[cur] == 0 : 
                        c[cur+1] = 1
                        retenue=0
                    else : 
                        c[cur+1] = 0
                        retenue=1
                if a[cur] == 1 : 
                    if b[cur] ==0 : 
                        c[cur+1] = 0
                        retenue =1
                    else : 
                        c[cur+1] = 1
                        retenue = 1
        if retenue ==1 : 
            c[0]=1
        else : 
            c[0]=0
        return(c)

#test : print(ALU.add([0,0,1], [0,0,1]))
