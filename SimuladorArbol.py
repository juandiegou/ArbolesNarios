import pygame,sys
from tkinter import messagebox
#import ctypes
import time
from tkinter import*
from PIL import Image, ImageTk

#from pygame.locals import *

class SimuladorArbol:

    arbol=None
    Congreso=[]
    pantalla=None
    aux=None
    cPrincipal=None
    e=None
    etry=None
    et=None
    entry=None
    et1=None
    ety=None
    ety2=None
    msg=""
    def __init__(self,a,congreso):
        '''its the constructor of Simulador arbol -a is the tree structure -congreso is a dictionary with all data Json'''
        self.arbol=a
        self.pantalla=Tk()
        self.run()
        self.Congreso=congreso['people']

        
      
    def verificar(self,d):
        if d==[]:
            return True
        elif len(d[0]['childrens'])>3:
            return False
        var=0
        for h in d[var]['childrens']:
            self.verificar(h['childrens'])
            var+=1

                
            
    def listando(self,m):
        for h in m:
            l=self.arbol.nodosNivel(self.arbol.raiz)
            cPrincipal=Canvas(self.pantalla,width=1040, height=700,bg="#E8FFEC")
            cPrincipal.place(x=309,y=0)
            w=1040
            ls=self.arbol.listaAnchura(self.arbol.raiz)
            x=w
            y=10
            
            ji=1
            v=True
            z=m.pop(0)
            print("valor de z= ",z.dato)
            for k in l:
                if v==True:
                    '''k is Integer'''
                    x=round(w/3)
                    n=ls[k-1]
                    if n.dato==z.dato:
                        cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="salmon3")
                        cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                        cPrincipal.update()
                        time.sleep(2)  
                        cPrincipal.update()
                        c=self.arbol.buscarById(self.arbol.raiz,ls[k-1].dato).getColor()
                        if c==1:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="red3")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()   
                        elif c==2:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="Blue")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(2) 
                             
                        elif c==3:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="green3")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()   

                        else:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="yellow")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()                     
                    else:
                        c=self.arbol.buscarById(self.arbol.raiz,ls[k-1].dato).getColor()
                        if c==1:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="red3")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()   
                        elif c==2:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="Blue")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()   
                        elif c==3:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="green3")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()   
                        else:
                            cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="yellow")
                            cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                            time.sleep(1) 
                            cPrincipal.update()   


                    v=False
                else:
                    y+=50
                    xx=round(w/k)       
                    for j in range(k):
                        if k==1:             
                            xx=round(xx/2)
                            if ls[ji].dato==zs.dato:
                                cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="salmon3")
                                cPrincipal.create_text(x+15,y+15,textls[k-1].dato)
                                cPrincipal.update()
                                time.sleep(1)
                                cPrincipal.update()
                                c=self.arbol.buscarById(self.arbol.raiz,ls[ji].dato).getColor()
                                if c==1:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="red3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==2:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="Blue")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==3:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="green3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                else:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="yellow")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                            else:                 
                                
                                c=self.arbol.buscarById(self.arbol.raiz,ls[ji].dato).getColor()

                                if c==1:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="red3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==2:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="Blue")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==3:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="green3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                else:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="yellow")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                            
                        else:
                            if ls[ji].dato==z.dato:
                                cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="salmon3")
                                cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                                cPrincipal.update()
                                time.sleep(1) 
                                cPrincipal.update()                               
                                c=self.arbol.buscarById(self.arbol.raiz,ls[ji].dato).getColor()
                                if c==1:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="red3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==2:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="Blue")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==3:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="green3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                else :
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="yellow")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                            else:
                                c=self.arbol.buscarById(self.arbol.raiz,ls[ji].dato).getColor()
                                if c==1:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="red3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==2:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="Blue")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                elif c==3:
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="green3")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   
                                else :
                                    cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="yellow")
                                    xx+=70
                                    cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                    ji+=1
                                    time.sleep(0.1) 
                                    cPrincipal.update()   














    def dibujar(self):
        '''it draw the tree'''
        #print("verificacion",self.verificar(self.Congreso))
        if  (self.verificar(self.Congreso)):
            l=self.arbol.nodosNivel(self.arbol.raiz)
            cPrincipal=Canvas(self.pantalla,width=1040, height=700,bg="#E8FFEC")
            cPrincipal.place(x=309,y=0)
            w=1040
            ls=self.arbol.listaAnchura(self.arbol.raiz)
            x=w
            y=10
            
            ji=1
            v=True
            for k in l:
                if v==True:
                    '''k is Integer'''
                    x=round(w/3)
                    c=self.arbol.buscarById(self.arbol.raiz,ls[k-1].dato).getColor()
                    if c==1:
                        cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="red3")
                        cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                    elif c==2:
                        cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="Blue")
                        cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                    elif c==3:
                        cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="green3")
                        cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)
                    else:
                        cPrincipal.create_oval(x,y,x+30,y+30,width=7,fill="yellow")
                        cPrincipal.create_text(x+15,y+15,text=ls[k-1].dato)


                    v=False
                else:
                    y+=50
                    xx=round(w/k)       
                    for j in range(k):
                        if k==1:             
                            xx=round(xx/2)
                            c=self.arbol.buscarById(self.arbol.raiz,ls[k-1].dato).getColor()
                            if c==1:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="red3")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            elif c==2:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="Blue")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            elif c==3:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="green3")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            else:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="yellow")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            
                        else:
                            c=self.arbol.buscarById(self.arbol.raiz,ls[ji].dato).getColor()
                            if c==1:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="red3")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            elif c==2:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="Blue")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            elif c==3:
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="green3")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                            else :
                                cPrincipal.create_oval(xx,y,xx+30,y+30,width=7,fill="yellow")
                                xx+=70
                                cPrincipal.create_text(xx-60,y+15,text=ls[ji].dato)
                                ji+=1
                 
        else:
            print(messagebox.showerror("Error", "El archivo No cumple las condiciones",parent=self.pantalla))
            if messagebox.askyesno("salir?", "Desea salir?..."):
                self.pantalla.destroy()
            

    def AddTeset(self,q):
        vn=self.entry.get()
        vp=self.et1.get()
        self.aux.destroy()
        self.arbol.agregar(self.arbol.raiz,int(vp),int(vn))
        self.dibujar()


    def agregar(self):
        '''it can addd new a senador'''
        self.aux=Tk()
        self.aux.geometry("300x120")
        self.aux.title("ingresar congresista")
        self.aux.wm_attributes("-topmost", 1) 
        self.aux.resizable(False,False)
        ####____________________________#############
        p=Canvas(self.aux,width=300, height=120)
        p.place(x=0,y=0)
        e=Label(p, text="ingrese id:")
        e.place(x=0,y=30)
        #############################################
        self.entry=Entry(p,textvariable=self.v1)
        self.entry.place(x=70,y=30)
        ###################################
        e1=Label(p, text="ingrese id del padre:")
        e1.place(x=0,y=60)
        ################################
        self.et1=Entry(p,textvariable=self.v2)
        self.et1.place(x=120,y=60)
        btn=Button(p,width=10,text="Agregar")
        btn.place(x=50,y=90)
        btn.bind("<Button-1>",self.AddTeset)
        self.aux.mainloop()


    def Deltest(self,q): 
        v=self.etry.get()
        vt=self.et.get()
        self.aux.destroy()
        self.arbol.eliminar(self.arbol.raiz,int(vt),int(v))
        self.dibujar()

    def eliminar(self):
        '''it can to delete a senador of the sesion'''
        self.aux=Tk()
        self.aux.geometry("300x200")
        self.aux.title("Sancionar congresista")
        self.aux.wm_attributes("-topmost", 1) 
        self.aux.resizable(False,False)
        ####____________________________#############
        p=Canvas(self.aux,width=300, height=100)
        p.place(x=0,y=0)
        e=Label(p, text="ingrese id:")
        e.place(x=0,y=30)
        #############################################
        self.etry=Entry(p,textvariable=self.v3)
        self.etry.place(x=70,y=30)
        ###################################
        e1=Label(p, text="ingrese id del padre:")
        e1.place(x=0,y=60)
        ################################
        self.et=Entry(p,textvariable=self.v4)
        self.et.place(x=120,y=60)
        ##################
        btn=Button(self.aux,width=10,text="Sacar")
        btn.place(x=50,y=90)
        btn.bind("<Button-1>",self.Deltest)
        aux.mainloop()


    def rempTest(self,q):
        vi=self.ety.get()
        vf=self.ety2.get()
        self.aux.destroy()
        self.arbol.buscarById(self.arbol.raiz,int(vi)).cambioId(int(vf))
        self.dibujar()
    def remplazar(self):
        '''it can to remplace a senador of the sesion '''
        self.aux=Tk()
        self.aux.geometry("300x120")
        self.aux.title("Cambio de congresista")
        self.aux.wm_attributes("-topmost", 1) 
        self.aux.resizable(False,False)
        ####____________________________#############
        p=Canvas(self.aux,width=300, height=120)
        p.place(x=0,y=0)
        e=Label(self.aux, text="ingrese id a cambiar:")
        e.place(x=0,y=30)
        #############################################
        self.ety=Entry(p,textvariable=self.v5)
        self.ety.place(x=120,y=30)
        ###################################
        e1=Label(self.aux, text="ingrese el nuevo id:")
        e1.place(x=0,y=60)
        ################################
        self.ety2=Entry(p,textvariable=self.v6)
        self.ety2.place(x=120,y=60)
        btn=Button(self.aux,width=10,text="Remplazar")
        btn.place(x=150,y=90)
        btn.bind("<Button-1>",self.rempTest)

        self.aux.mainloop()

    def eleccion(self,q):
        vt=self.e.get()
        self.aux.destroy()
        print(vt)
        if int(vt)==1:
            self.listando(self.arbol.listaAnchura(self.arbol.raiz))
        elif int(vt)==2:
            self.arbol.inOrder(self.arbol.raiz)
            self.listando(self.arbol.inOr)
        elif int(vt)==3:
            self.arbol.preOrder(self.arbol.raiz,0)
            self.listando(self.arbol.preOrd)
            
        elif int(vt)==4:
            self.arbol.postOrder(self.arbol.raiz,0)
            self.listando(self.arbol.postOr)



    def llamar_a_lista(self):
        '''it can to list the sesion'''
        self.aux =Tk()
        self.aux.geometry("180x180")
        self.aux.title("Llamados a lista")
        self.aux.wm_attributes("-topmost",1)
        self.aux.resizable(False,False)
        p=Canvas(self.aux,width=180,height=180)
        p.place(x=0,y=0)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
        l0=Label(p,text="Ingrese una Opción")
        l0.place(x=50,y=3)
        l=Label(p,text="1: Anchura\n2: InOrder\n 3:PreOrder\n 4:PostOder")
        l.place(x=10,y=20)
        self.e=Entry(p,textvariable=self.r)
        self.e.place(x=10,y=90)
        btn=Button(self.aux,width=10,text="llamar")
        btn.place(x=10,y=140)
        btn.bind("<Button-1>",self.eleccion)
        self.aux.mainloop()


       



    def reunion(self):
        '''it can o organize a meet by party'''
        pass


    def info(self,q):
        self.aux.destroy()


    def inf(self):
        self.aux=Tk()
        self.aux.geometry("300x300")
        self.aux.title("información")
        self.aux.wm_attributes("-topmost", 1) 
        self.aux.resizable(False,False)
        ####____________________________#############
        p=Canvas(self.aux,width=300, height=300)
        l=self.arbol.ramaLarga(self.arbol.raiz)
        self.msg=("El arbol es completo: ",self.arbol.esCompleto(self.arbol.raiz),
        "El arbol es Full: ",self.arbol.esFull(self.arbol.raiz),"El numero de niveles del Arbol es: ",self.arbol.numNodos(self.arbol.raiz),"\n",
        "El camino más largo es: ",self.arbol.textrama(l))
        print(self.msg)
        l=Label(p,text=("El arbol es completo: ",self.arbol.esCompleto(self.arbol.raiz),
        "El arbol es Full: ",self.arbol.esFull(self.arbol.raiz),"El numero de niveles del Arbol es: ",self.arbol.numNodos(self.arbol.raiz),
        "El camino más largo es: ",self.arbol.textrama(l)))
        l.place(x=0,y=0)
        ####################################
        btn=Button(self.aux,width=10,text="ok")
        btn.place(x=10,y=140)
        btn.bind("<Button-1>",self.info)
        self.aux.mainloop()

        self.aux.mainloop()
        
    
    def run(self):
        self.v1="" # para el id1
        self.v2="" # para el id2
        self.v3="" # para el id3
        self.v4=""# para el id4
        self.v5="" # para el id5
        self.v6="" # para el id6
        self.r="" # para el reco
        
        self.pantalla.geometry("1370x700")
        self.pantalla.title("Congreso Xp")
        self.pantalla.wm_attributes("-topmost", 1) 
        self.pantalla.resizable(False,False)
        panel=Canvas(self.pantalla,width=300, height=400,bg="#AAAEF0" )
        panel.place(x=0,y=0)
        '''here  add the canvas and place in the initial coords'''
        etiqueta=Label(panel, text="Menú Congreso", bg="#FFF691",width=35)
        etiqueta.place(x=15,y=0)
        '''here  add the tag and place in the initial coords'''
        btnCarge=Button(self.pantalla,width=40,text="Iniciar sesión",command=self.dibujar)
        btnCarge.place(x=5,y=80)
        '''here  add the button carge and place i the initial coords'''
        btnIngreso=Button(self.pantalla,width=40,text="Ingresar Senador",command=self.agregar)
        btnIngreso.place(x=5,y=120) 
        '''here  add the button btnadd and place i the initial coords'''
        btnDelete=Button(self.pantalla,width=40,text="Sancionar Senador",command=self.eliminar)
        btnDelete.place(x=5,y=160)   
        '''here  add the button delete and place i the initial coords'''     
        btnRemplace=Button(self.pantalla,width=40,text="Senador suplente",command=self.remplazar)
        btnRemplace.place(x=5,y=200)
        '''here  add the button remplace and place i the initial coords'''
        btnList=Button(self.pantalla,width=40,text="Llamar a lista",command=self.llamar_a_lista)
        btnList.place(x=5,y=240)
        '''here  add the button list and place i the initial coords'''
        btnmeet=Button(self.pantalla,width=40,text="Reunión Interna",command=self.reunion)
        btnmeet.place(x=5,y=280)   
        '''here  add the button meet and place i the initial coords'''    
        btninfo=Button(self.pantalla,width=40,text="Información",command=self.inf)
        btninfo.place(x=5,y=320)   
        '''here  add the button infoTree and place i the initial coords'''         

    
    
        self.pantalla.mainloop()
       

        
  