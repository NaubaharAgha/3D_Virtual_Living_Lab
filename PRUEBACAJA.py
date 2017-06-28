import viz
import vizact
viz.go()

ground = viz.add('tut_ground.wrl') #ground
ground.disable(viz.INTERSECTION)
viz.clearcolor([.5, .6, 1])
CAJA = viz.add('Caja_final_cerrada.obj')
CAJA.setScale(0.005,0.005,0.005)
Tapa = CAJA.getChild('Tapa')
Tapa1 =CAJA.getChild('Agrupar#2')
Tapa2 = CAJA.getChild('Tapa palanca')
Tornillo1 = CAJA.getChild('Hinge barrel#1_1')
Tornillo2 = CAJA.getChild('Hinge leaf B')
Tornillo3 = CAJA.getChild('Hinge leaf B_1')
Tornillo4 = CAJA.getChild('Hinge barrel#1')
Tornillo5 = CAJA.getChild('Hinge pin end')
Tornillo6 = CAJA.getChild('Hinge pin end_1')
Tornillo7 = CAJA.getChild('Hole detail#3')
Tornillo8 = CAJA.getChild('Hole detail#3_1')
Tornillo9 = CAJA.getChild('Hole detail#3')
Tornillo10 = CAJA.getChild('Hole detail#3_1')
Tornillo11 = CAJA.getChild('Hinge leaf A')
Tornillo12 = CAJA.getChild('Hinge leaf A_1')

viz.link(Tornillo1,Tornillo2)
viz.link(Tornillo1,Tornillo3)
viz.link(Tornillo1,Tornillo4)
viz.link(Tornillo1,Tornillo5)
viz.link(Tornillo1,Tornillo6)
viz.link(Tornillo1,Tornillo7)
viz.link(Tornillo1,Tornillo8)
viz.link(Tornillo1,Tornillo9)
viz.link(Tornillo1,Tornillo10)
viz.link(Tornillo1,Tornillo11)
viz.link(Tornillo1,Tornillo12)



CAJA.setEuler([0,90,0],viz.ABS_GLOBAL)

print "POSICION Tapa1" ,Tapa1.getPosition(viz.ABS_GLOBAL)
print "EULER Tapa1" ,Tapa1.getEuler(viz.ABS_GLOBAL)
print "POSICION Tapa2" ,Tapa2.getPosition(viz.ABS_GLOBAL)
print "EULER Tapa2" ,Tapa2.getEuler(viz.ABS_GLOBAL)
print "POSICION Tapa" ,Tapa.getPosition(viz.ABS_GLOBAL)
print "EULER Tapa" ,Tapa.getEuler(viz.ABS_GLOBAL)




#metodo para abrir la caja abriendo las 2 puertas
def abrirModo1() :
	
	Tapa1.setEuler([-180,0,240],viz.ABS_GLOBAL)
	Tapa1.setPosition([-0.5,1.7,0],viz.ABS_GLOBAL)

	Tapa2.setEuler([-180,0,120],viz.ABS_GLOBAL)
	Tapa2.setPosition([1.05,0.6,0],viz.ABS_GLOBAL)
	
def cerrarModo1() :	

	Tapa1.setEuler([-180.0,0, 180.0],viz.ABS_GLOBAL)
	Tapa1.setPosition([0,0,0],viz.ABS_GLOBAL)

	Tapa2.setEuler([-180.0, 0, 180.0],viz.ABS_GLOBAL)
	Tapa2.setPosition([0,0,0],viz.ABS_GLOBAL)


#-------------------------------------------------MOVIMIENTO TAPA

def abrirModo2() :

	Tapa.setEuler([-180,-25,180],viz.ABS_GLOBAL)
	Tapa.setPosition([0,0.625,-0.4],viz.ABS_GLOBAL)

	Tapa1.setEuler([-180,-25,180],viz.ABS_GLOBAL)
	Tapa1.setPosition([0,0.625,-0.4],viz.ABS_GLOBAL)
	Tapa2.setEuler([-180,-25,180],viz.ABS_GLOBAL)
	Tapa2.setPosition([0,0.625,-0.4],viz.ABS_GLOBAL)

	#movimiento tornillo

	Tornillo1.setEuler([-180,-25,180],viz.ABS_GLOBAL)
	Tornillo1.setPosition([0,0.625,-0.4],viz.ABS_GLOBAL)

def cerrarModo2() :

    Tapa1.setEuler([-180.0,0, 180.0],viz.ABS_GLOBAL)
    Tapa1.setPosition([0,0,0],viz.ABS_GLOBAL)
    Tapa.setEuler([-180.0, 0, 180.0],viz.ABS_GLOBAL)
    Tapa.setPosition([0,0,0],viz.ABS_GLOBAL)
    Tapa2.setEuler([-180.0, 0, 180.0],viz.ABS_GLOBAL)
    Tapa2.setPosition([0,0,0],viz.ABS_GLOBAL)

    Tornillo1.setEuler([-180,0,180],viz.ABS_GLOBAL)
    Tornillo1.setPosition([0,0,0],viz.ABS_GLOBAL)