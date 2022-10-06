import pygame,sys
from ArbolNArio import ArbolNArio
from Nodo import Nodo
from Lector import Lector
from SimuladorArbol import SimuladorArbol




class main:
    congreso=None
    simulador=None
    arbol=None
    azul= (0,128,128)
    amarillo= (255,255,0)
    rojo =(255,0,0)
    verde=(0,255,0)
    nNodo=0
    def __init__(self):
        '''this is the main constructor'''
        #party=[]
        l = Lector("F:/2019-1/congreso-20191012T231339Z-001/congreso/format.json")
        self.congreso=l.getData()
        datoR=self.congreso['people'][0]['id']
        #print(self.congreso['people'][0]['party'])
        c=self.congreso['people'][0]['party']
        self.arbol= ArbolNArio(datoR)
        #print(c)
        self.arbol.raiz.setColor(c)
        #print("raiz: ",self.arbol.raiz.dato)
        #print(self.congreso['people'][0]['childrens'][0]['id'])
        for h in self.congreso['people'][0]['childrens']:
            self.arbol.agregar(self.arbol.raiz,self.arbol.raiz.dato,h['id']) 
            self.arbol.buscarById(self.arbol.raiz,h['id']).setColor(h['party'])
            
        self.llenado(self.arbol.raiz,self.congreso['people'][0]['childrens'])
       # self.arbol.anchura(self.arbol.raiz)
        #print(self.arbol.nodosNivel(self.arbol.raiz))
       # self.arbol.eliminar(self.arbol.raiz,13,1)
        #print("\n")
       # self.arbol.obtenerRamas(self.arbol.raiz,[])
       # r=self.arbol.ramas
       # for x in r:
       #     for y in x:
       #         print(y.dato, end=" ")
       #     print("\n")
        
        #print(self.arbol.nodosNivel(self.arbol.raiz))
        #print(self.arbol.buscarById(self.arbol.raiz,18).cambioId(55) )
        #self.arbol.anchura(self.arbol.raiz)
        #print("Espacio : ",self.arbol.raiz.tieneEspacio())
        #self.arbol.mostrar(self.arbol.raiz)     
        l=self.arbol.ramaLarga(self.arbol.raiz)
        
        #print(l)
        for x in l:
            print(x.dato)
            
        
        print(self.arbol.numNodos(self.arbol.raiz))
        print("altura",self.arbol.altura(self.arbol.raiz))


        self.simulador=SimuladorArbol(self.arbol,self.congreso)        
        self.simulador.dibujar()
        #self.arbol.inOrder(self.arbol.raiz,0)

        
    


    def llenado(self,d,l):
        '''d is Nodo -l is the list of childs.
           its can to full the treee'''
        if l==[]:
            return
        var=0
        for h in d.hijos:
            if len(l[var]['childrens'])<=3:
                for k in l[var]['childrens']:
                    self.arbol.agregar(self.arbol.raiz,h.dato,k['id'])
                    self.arbol.buscarById(self.arbol.raiz,k['id']).setColor(k['party'])
                self.llenado(h,l[var]['childrens'])
                var+=1
            else:
                print("error en el archivo en", l[var].id)
      
        

                    
if __name__ == "__main__":
   main()