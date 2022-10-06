from Nodo import Nodo


class Arbol:

    def __init__(self , raiz):
        self.raiz=raiz

    def agregar(self,r,p,d):
        if  r is not None:
            if r.dato == p:
                r.agregarHijO(Nodo(d))
            else:
                for h in r.hijos:
                    self.agregar(h,p,d)


    def esHoja(self,r):
        


