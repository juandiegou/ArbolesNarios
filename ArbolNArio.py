from Nodo import Nodo

class ArbolNArio:
	raiz= None
	ramas=[]
	preOrd=[]
	inOr=[]
	postOr=[]
	hojas=[]
	def __init__(self,dato):
		''''dato is the id of root Node.constructor of class ArboNario'''
		self.raiz = Nodo (dato)

	def agregar(self,n,padre,dato):
		'''n is the root -padre is the father -dato is id of new Node.its can  to add a new Node to the tree'''
		
		if  not n is None:
			#print("raiz", n.dato, " padre",padre," dato",dato)
			if n.dato== padre:
				#print("encontrado")
				if len(n.hijos)<3:
					n.agregarHijo(dato)
					#print("padre :",n.dato," hijo",dato)
				else:
					print("NO se pude agregar ya tiene 3 hijos")
			else:
				for h in n.hijos:
					self.agregar(h,padre,dato)

			
	def mostrar (self,n):
		'''its show one by one the Node and their childrens'''
		
		if not n is None:			
			print("Nodo: ",n.dato,"\n")
			for h in n.hijos:
				print("Hijos de ",n.dato,":",h.dato,end="\n")
           
			for hh in n.hijos:
				self.mostrar(hh)


	def profundidad(self,r,d,n):
		if r is not None:
			if r.dato==d:
				print(n)
			else:
				for h in r.hijos:
					self.profundidad(h,d,n+1)
				n-=1
		
	def anchura(self,n):
		'''n- is the root. its show the breadth path'''
		if n is not None:
			cola=[]
			temp=None
			cola.append(n)

			while len(cola)>0:
				temp=cola.pop(0)
				print(temp.dato,end=" ")
				for h in temp.hijos:
					cola.append(h)
				
            

	def altura(self,n):
		'''its show largest tree size'''
		if n is None:
			return 0
		else:
			return 1+max((self.altura(h)for h in n.hijos),default=0)



	
	def obtenerRamas(self,n,lst):
		''' n is the root -lst is temporal list ways . it can to obtain all ways. Please include the root tree in the lst'''
		if n is not None:
			if n.hijos==[]:								
				lt=[]				
				for l in lst:
					lt.append(l)	
				self.ramas.append(lt)
				return lst
			for h in n.hijos:
				lst.append(h)
				self.obtenerRamas(h,lst)

				lst.pop()
				
				


	def nivelNodo(self,r,d,l):
		'''r is the root -d is data. it can to obtain the level of data'''
		if r is not None:
			if r.dato == d:
				return l
			for h in r.Hijos:
				self.nivelNodo(h,d,l+1)


	def preOrder(self,r,n):
		'''r is root -n is flag. it can show the inOrder path'''
		if r is not None:
			preOrd.append(r)
			for h in r.hijos:
				self.preOrder(h,n+1)
				n-=1



	def postOrder(self,r):
		if r is not None:
			if r.hijos==[]:
				postOr.append(r)
				return
			
			for x in r.hijos:
				self.postOrder(x)
			postOr.append(r)	

	def inOrder(self,r):
		if r is not None:
			if r.hijos==[]:
				self.inOr.append(r)
				return
			for h in r.hijos:
				self.inOrder(h)
				if r not in self.inOr:
					self.inOr.append(r)


	def EncuentraHojas(self,r):
		if r is not None:
			if r.hijos==[]:
				hojas.append(r)
			for x in r.hijos:
				self.inOrder(x)


	
	def nodosNivel(self,r):
		'''r is the root of tree. it can to obtain all node by level'''
		if r is not None:
			colaNodos=[]
			colaNodos.append(r)
			contadorNodos=0
			listaNNodos=[]
			contadorNodostemp=0
			listaNNodos.append(1)
			
			temp=colaNodos.pop(0)
			for h in temp.hijos:
				colaNodos.append(h)			
				contadorNodos+=1
			listaNNodos.append(contadorNodos)

			while colaNodos:
				
				if contadorNodos!=0:
					temp=colaNodos.pop(0)
					for h in temp.hijos:
						colaNodos.append(h)
						contadorNodostemp+=1
					contadorNodos-=1
				else:
					listaNNodos.append(contadorNodostemp)
					contadorNodos=contadorNodostemp
					contadorNodostemp=0
			return listaNNodos


	def nodoById(self,r,d):
		'''r is the tree root -d is the id of search Node. it make a search  in the tree by Id'''
		'''este metodo no funciona mejor usar buscarById'''
		if r is not None:
			if r.dato==d:
				return r
			for h in r.hijos:
				self.nodoById(h,d)
			
		
	def listaAnchura(self,r):
		'''r is the tree root . it make list in breadth '''
		if r is not None:
			list=[]
			cola=[]
			temp=None
			cola.append(r)
			while cola:
				temp=cola.pop(0)
				list.append(temp)
				for h in  temp.hijos:
					cola.append(h)
			return list

	def eliminar(self,r,f,d):
		'''it delete a Node'''
		l=[]
		if r is not None:
			if r.dato==f:
				i=0
				for h in r.hijos:
					if h.dato==d:
						if h.hijos==[]:	
							print("dato",h.dato)						
							r.hijos.remove(self.buscarById(self.raiz,d))
						else:
							l=self.nodosNivel(self.raiz)
							if l[i]<=(3**i):
								hh=h.hijos
								r.hijos.remove(h)
								for j in hh:
									print(j.dato)
									print("valor r",r.dato)
									self.agregarAdoptado(r,self.buscarById(self.raiz,r.dato),j.dato)
									


					i+=0
			for child in r.hijos:
				self.eliminar(child,f,d)


	def agregarAdoptado(self,r,p,d):
		'''it add child to anyone'''
		if r is not None:
			if r.dato==p.dato:
				print("encontrado...")
				if r.hijos==[]:
					self.agregar(r,r.dato,d)
					return
				for hp in p.hijos:
					if hp.tieneEspacio():
						self.agregar(self.raiz,hp.dato,d)
						print("se agrego ",d)
						return					
					else:
						for hph in hp.hijos:
							self.agregarAdoptado(self.raiz,hph,d)
							return

			for h in r.hijos:
				print("bscando...",h.dato)
				self.agregarAdoptado(h,p,d)	




	''''
	if p.tieneEspacio():
					print("agregando ",d, " a",p.dato)
					self.agregar(self.raiz,r,d,"blue")
					
				else:
					for ad in p.hijos:
						self.agregarAdoptado(r,ad,d)
	'''



		
				
	def buscarById(self,r,id):
		'''r is the tree root -id is the data of Node. it can to obtain a Node By id'''
		if r is not None:
			l= self.listaAnchura(self.raiz)
			for child in l:
				if child.dato==id:
					return child

			
		
	def cambioId(self,idI,idF):
		''' idI: it will change -idF it well be new id. it can to change id's'''
		nodo=self.buscarById(self.raiz,idI)
		nodo.cambioId(idF)


	def esCompleto(self,r):
		'''the tree is complete '''
		if r is not None:
			l=self.nodosNivel(r)			
			r=True		
			for k in range(0,len(l)):
				if 3**k!=l[k]:
					r=False
					break
			return r

	def esFull(self,r):

		if r is not None:
			l=self.nodosNivel(r)
			r=True
			for m in range(0,len(l)-1):
				if 3**m !=l[m]:
					r=False

			return r
					
	
	def ramaLarga(self,r):
		''''the way largest'''
		if r is not None :
			self.obtenerRamas(r,[r])
			r=self.ramas
			lg=r[0]
			for l in r:
				if len(l)>len(lg):
					lg=l
			return lg


	def numNodos(self,r):
		if r is not None:
			l=self.nodosNivel(r)
			nnodos=0
			for  i in l:
				nnodos+=i
			return nnodos
			

	def textrama(self,l):
		v =""
		for x in l:
			v+=str(x.dato)+" "

		return v