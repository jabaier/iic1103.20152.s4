class color:
    def __init__(self,r,g,b):
        self.red=r
        self.green=g
        self.blue=b

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,v):
        return vector(self.x+v.x,self.y+v.y)

    def __sub__(self,v):
        return vector(self.x-v.x,self.y-v.y)

    def mostrar(self):
        print("este es el vector ("+str(self.x)+","+str(self.y)+")")

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class cuadrado:
    def __init__(self,x,y,lado):
        self.x=x
        self.y=y
        self.lado=lado
        self.color=color(0,0,0)
        self.r="undef"

    def pintar(self,color):
        self.color=color

    def cambiar_tamano(self,tamano):
        self.lado=tamano

    def escalar(self,escala):
        self.lado = self.lado*escala

    def mostrar(self):
        print("este cuadrado está en ("+str(self.x)+","+str(self.y)+") y tiene lado "+str(self.lado)+"y tiene color RGB ("+str(self.color.red)+","+str(self.color.green)+","+str(self.color.blue)+")")

    def desplazar(self,v):
        self.x=self.x+v.x
        self.y=self.y+v.y

    def __str__(self):
        return "[]"+str(vector(self.x,self.y))+":"+str(self.lado)

    def dibujar(self,window):
        if self.r != "undef":
            self.r.undraw()

        self.r=Rectangle(Point(self.x,self.y),Point(self.x+self.lado,self.y+self.lado))
        self.r.setOutline(color_rgb(self.color.red,self.color.green,self.color.blue))
        self.r.draw(window)

class circulo:
    def __init__(self,x,y,radio):
        self.x=x
        self.y=y
        self.radio=radio

from graphics import *

def parte_grafica(color):
    c=cuadrado(10,10,100)
    w = GraphWin("Mi pantalla", 500, 500)
    c.dibujar(w)
    w.getMouse() # pause to view result
    c.escalar(2)
    c.dibujar(w)
    w.getMouse() # pause to view result
    c.pintar(color)
    c.dibujar(w)
    w.getMouse() # pause to view result
    w.close()

import time

def animacion():
    c=cuadrado(10,10,100)
    w = GraphWin("Mi pantalla", 500, 500)

    while c.x<200:
        c.dibujar(w)
        c.desplazar(vector(1,1))
        c.escalar(1.005)
#        time.sleep(0.04)
    w.getMouse() # pause to view result


color_rojo=color(255,0,0)
color_azul=color(0,0,255)
color_bonito=color(0,153,153)

#parte_grafica(color_bonito)
animacion()





v=vector(1,1)
c1=cuadrado(1,2,10)
c1.pintar(color_rojo)
c2=cuadrado(0,0,100)
c2.pintar(color_bonito)
c1.mostrar()
c2.mostrar()
v.mostrar()


#c.desplazar(vector(10,10))
#print(vector(4,5)+vector(1,1))
#print(c)
