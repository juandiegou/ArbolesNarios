

class Nodo:
	def __init__(self,dato):
		self.dato=dato
		self.hijos = []
		self.color=None

	def agregarHijo(self,dato):
		self.hijos.append(Nodo(dato))
	

	def esHoja(self):
		return self.hijos==[]	




	def gradoNodo(self):
		return len(self.hijos)
	'''
	def agregarhijos(self,list):
		for h in list:
			self.agregarHijo(h)
	'''

	def cambioId (self,dato ):
		self.dato=dato

	def setColor(self,color):
		self.color=color

	def tieneEspacio(self):
		return len(self.hijos)<3

	def setColor(self,c):
		self.color=c

	def getColor(self):
		return self.color