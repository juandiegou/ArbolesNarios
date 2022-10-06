
from ArbolNArio import ArbolNArio
from Nodo import Nodo
import json

class Lector:
    data=""
    def __init__( self,ruta):
        with open (ruta) as file:
            self.data= json.load(file)
       
       
        


    def getData(self):
        return self.data


   




    






    





