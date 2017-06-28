import viz
import vizcam
import vizact
import viztracker #DESCOMENTAR ESTO PARA LA SALA DE RV
import hand
import vizproximity
import vizshape
import viztask
import cgi
import vizinfo
import vizhtml

#---------------------------------INICIALIZACIÓN-----------------------------------------------------

#viztracker.go() #DESCOMENTAR ESTO PARA LA SALA DE RV

viz.go()
viz.cam.setHandler(vizcam.KeyboardCamera())
#viz.cam.setHandler(vizcam.addWalkNavigate())
viz.phys.enable()

viz.collision(viz.ON) #real time collision detection

#Place the view point
viz.MainView.setPosition(1, 1.8, 3)
viz.MainView.setEuler(30, 0, 0)

viz.MainView.getHeadLight().intensity(0.5) #Para que se vea oscuro mientras no estén encendidas las luces ni las persianas abiertas

label = viz.addText('LifeSTech',parent=viz.SCREEN,pos=[0.005,0.947,0],scale=[0.5,0.5,1], color = viz.PURPLE)

caja = viz.add('mobile_cucina_Scene.obj')
puerta = caja.getChild('Cube_Cube_Aluminum')
puerta.setPosition(-3.5,1,0,viz.REL_LOCAL)
eule2 = [0,0,90]

puerta.setEuler(eule2, viz.REL_LOCAL)


caja.setPosition(3,1,9,viz.ABS_GLOBAL)
caja.setScale(0.1,0.1,0.1)


ground = viz.add('tut_ground.wrl') #ground
ground.disable(viz.INTERSECTION)
viz.clearcolor([.5, .6, 1])

lab = viz.add('Living_Lab_Blinds_V2.OSGB')#, scale=[0.002]*3)
lab.setScale(0.006,0.006,0.006)
lab.setPosition ([0,0.58,5])

#Importamos tracker de la mano
#rightHand = viztracker.get('righthand') #DESCOMENTAR ESTO PARA LA SALA DE RV

##PRUEBA DE PANTALLA PARA SALA RV
#pantalla = viz.add ('08 DA-LITE Cinema Contour.obj', scale=[0.002]*3)
#pantalla.setPosition([-1, 0.258, 1.5])

#INICIALIZACIÓN DE VARIABLES
state_doorbath = 1
state_doorkit = 0
state_doorsal= 0
state_rollupbed = 0
state_rollupsal = 0
state_rollupkit = 0
state_rollupsc = 0
state_doorSC = 0
state_doorHome = 0
state_KitLight = 0
state_BedroomLight = 0  ##NUEVO
state_BathroomLight = 0 ##NUEVO
state_SCLight = 0 ##NUEVO

sen = 0

global manager
global sensor_DoorSC
global sensor_DoorHome
global sensor_doorSuichbath
global sensor_Kitchen
global sensor_salon
global sensor_RollupBED
global sensor_RollupSal1
global sensor_RollupSal2
global sensor_RollupKit1
global sensor_RollupKit2
global sensor_RollupSC
global sensor_KitLight
global sensor_BedroomLight   ##NUEVO
global sensor_BathroomLight   ##NUEVO
global sensor_SCLight   ##NUEVO

#INICIALIZACIÓN TEXTO INFO
texto = viz.addText('',parent=viz.SCREEN, pos=[0.005,0.927,0], scale=[0.5,0.5,1], color = viz.PURPLE)


#INICIALIZACIÓN DE LOS PROXIMITY SENSORS    
# Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(True)

# Add the tracker (hand) as proximity target
#target =  vizproximity.Target(viz.MainView)
#Add the object that will do the grabbing   PARA CONTROL EN LA COMPU
hand = viz.addChild('marker.wrl')
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
item = viz.link(mouseTracker,hand)

target = vizproximity.Target(item)#PARA CONTROL EN LA COMPU
#target = vizproximity.Target(rightHand) #DESCOMENTAR ESTO PARA LA SALA DE RV
manager.addTarget(target)


#-------------------------------ABRIR Y CERRAR PUERTAS-------------------------------------------------------

#ABRIR Y CERRAR PUERTA SALA DE CONTROL

DoorSC_GEODE = lab.getChild('Door sala control').getChild ('Box010')
Chapa = lab.getChild ('Chapa')
Cilindro = lab.getChild('Cylinder001')
link_DoorSC = viz.link(DoorSC_GEODE, Chapa)
link2_DoorSC = viz.link(DoorSC_GEODE, Cilindro)

sensor_DoorSC = vizproximity.addBoundingSphereSensor(DoorSC_GEODE, scale = .8)
manager.addSensor(sensor_DoorSC)

#def doorSC(e): #SALA RV
def doorSC():
	print 'estoy en doorSC'
	global state_doorSC
	
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_doorSC == 1: #CERRAR
		eule2 = [-90,0,0]
		DoorSC_GEODE.setEuler(eule2, viz.REL_LOCAL)
		state_doorSC = 0
	else: #ABRIR
		eule = [90,0,0]
		DoorSC_GEODE.setEuler(eule, viz.REL_LOCAL)
		state_doorSC = 1

#vizact.onpick(DoorSC_GEODE,  doorSC)


#ABRIR Y CERRAR PUERTA DE ENTRADA

DoorHome_GEODE = lab.getChild('Door Principal').getChild ('Box101-OFFSET')
Cham = lab.getChild ('ChamferBox002')
Cylinder = lab.getChild('Cylinder002')
Handle = lab.getChild('Door_Handle001')
Handle_base = lab.getChild('Door_handle_Base001')
Rectangle = lab.getChild('Rectangle014')


#Cham2 = Cham.setParent(DoorHome_GEODE)
#Cylinder2 = Cylinder.setParent(DoorHome_GEODE)
#Handle2 = Handle.setParent(DoorHome_GEODE)
#Handle_base2 = Handle_base.setParent(DoorHome_GEODE)
#Rectangle2 = Rectangle.setParent(DoorHome_GEODE)

link_DoorHome = viz.link(DoorHome_GEODE, Cham)
link2_DoorHome = viz.link(DoorHome_GEODE, Cylinder)
link3_DoorHome = viz.link(DoorHome_GEODE, Handle)
link4_DoorHome = viz.link(DoorHome_GEODE, Handle_base)
link5_DoorHome = viz.link(DoorHome_GEODE, Rectangle)

sensor_DoorHome = vizproximity.addBoundingSphereSensor(DoorHome_GEODE, scale = 1) 

manager.addSensor(sensor_DoorHome)

#def doorHome(e): #SALA RV
def doorHome():
	print 'estoy en doorHome'
	global state_doorHome
	
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_doorHome == 1: #CERRAR
		eule2 = [0,0,-90]
		DoorHome_GEODE.setEuler(eule2, viz.REL_LOCAL)
		state_doorHome = 0
	else: #ABRIR
		eule = [0,0,90]
		DoorHome_GEODE.setEuler(eule, viz.REL_LOCAL)
		state_doorHome = 1
		
#vizact.onpick(DoorHome_GEODE,  doorHome)


#ABRIR Y CERRAR LA PUERTA DEL BAÑO
Doorbath_GEODE = lab.getChild('Toilet_Door-GEODE')
Circle_GEODE = lab.getChild('Circle002-GEODE')

#def doorbath(e): #SALA RV
def doorbath():
	print 'estoy en doorbath'
	global state_doorbath
	
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_doorbath == 1: #CERRAR
		dpos = Doorbath_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1], dpos[2] + 0.8]
		Doorbath_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = Circle_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0], cpos[1], cpos[2] + 0.75]
		Circle_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
		state_doorbath = 0
	else: #ABRIR
		dpos = Doorbath_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1], dpos[2] - 0.8]
		Doorbath_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = Circle_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0], cpos[1], cpos[2] - 0.75]
		Circle_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
		state_doorbath = 1
	
doorSuich_bath = lab.getChild('Light_Switch out  bathroom')

sensor_doorSuichbath = vizproximity.addBoundingSphereSensor(doorSuich_bath, scale = 4)
manager.addSensor(sensor_doorSuichbath)

global sensor_planta
node = viz.addChild('plant.osgb',pos=(0,0.58,5))
sensor_planta = vizproximity.addBoundingBoxSensor(node, scale = (2,10,2))
manager.addSensor(sensor_planta)

#action = vizact.onpick(doorSuich_bath, doorbath)
#action2 = vizact.onpick(Doorbath_GEODE, doorbath)

#ABRIR Y CERRAR PUERTAS COCINA Y SALÓN
DoorKitchen_GEODE = lab.getChild('Glass002-GEODE')
DoorKit_frame_GEODE = lab.getChild('Door_Frame001-GEODE')

DoorSalon_GEODE = lab.getChild('Glass004-GEODE')
DoorSal_frame_GEODE = lab.getChild('Door_Frame003-GEODE')

#def doorKitchen (e): #SALA RV
def doorKitchen ():
	def openDoorKitchen ():
		dpos = DoorKitchen_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] + 0.6, dpos[1], dpos[2]]
		DoorKitchen_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorKit_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] + 0.6, cpos[1], cpos[2]]
		DoorKit_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	def closeDoorKitchen ():
		dpos = DoorKitchen_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] - 0.6, dpos[1], dpos[2]]
		DoorKitchen_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorKit_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] - 0.6, cpos[1], cpos[2]]
		DoorKit_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	global state_doorkit
	print 'estoy en doorkitchen'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_doorkit == 1: #CERRAR
		vizact.ontimer2(1,2,closeDoorKitchen)
		state_doorkit = 0
	else: #ABRIR
		vizact.ontimer2(1,2,openDoorKitchen)
		state_doorkit = 1

#def doorSalon (e): #SALA RV
def doorSalon ():
	def openDoorSalon ():
		dpos = DoorSalon_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] + 0.6, dpos[1], dpos[2]]
		DoorSalon_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorSal_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] + 0.6, cpos[1], cpos[2]]
		DoorSal_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	def closeDoorSalon ():
		dpos = DoorSalon_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] - 0.6, dpos[1], dpos[2]]
		DoorSalon_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorSal_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] - 0.6, cpos[1], cpos[2]]
		DoorSal_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	global state_doorsal
	print 'estoy en doorsalón'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_doorsal == 1: #CERRAR
		vizact.ontimer2(1, 2, closeDoorSalon)
		state_doorsal = 0
	else: #ABRIR
		vizact.ontimer2(1,2,openDoorSalon)
		state_doorsal = 1	


doorSuich_kitchen = lab.getChild('Light_Switch Kitchen')

sensor_Kitchen = vizproximity.addBoundingSphereSensor(doorSuich_kitchen, scale = 4)
manager.addSensor(sensor_Kitchen)

#action = vizact.onpick(doorSuich_kitchen, doorKitchen)

doorSuich_salon = lab.getChild('Light_Switch salon')

sensor_salon = vizproximity.addBoundingSphereSensor(doorSuich_salon, scale = 4)
manager.addSensor(sensor_salon)

#action = vizact.onpick(doorSuich_salon, doorSalon)

#--------------------------------------ABRIR Y CERRAR PERSIANAS-------------------------------------------------------
#LUZ AMBIENTE
luzAmbiente = viz.addLight()
luzAmbiente.disable()

#PERSIANAS DORMITORIO
Rollup_bed_GEODE = lab.getChild('Blind bedroom-GEODE')

#def RollupBed (e): #SALA RV
def RollupBed ():
	def open_bedblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_bed_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]+ 0.5, dpos[2]]
		Rollup_bed_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
		
	def close_bedblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_bed_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]- 0.5, dpos[2]]
		Rollup_bed_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#Rollup_bed_GEODE.alpha(1)
		#luzAmbiente.disable()
		
	global state_rollupbed
	print 'estoy en rollupbed'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_rollupbed == 1: #CERRAR
		vizact.ontimer2(1,6, close_bedblind)
		state_rollupbed = 0
	else: #ABRIR
		vizact.ontimer2(1,6, open_bedblind)
		state_rollupbed = 1
		
RollupSuich_bed = lab.getChild ('Light_Switch bedroom')
sensor_RollupBED = vizproximity.addBoundingSphereSensor(RollupSuich_bed, scale = 4)
manager.addSensor(sensor_RollupBED)
#action = vizact.onpick(RollupSuich_bed, RollupBed)

#PERSIANAS SALÓN
Rollup_sal1_GEODE = lab.getChild('Roll up door 3-GEODE')
Rollup_sal2_GEODE = lab.getChild('Roll up door 4-GEODE')

sensor_RollupSal1 = vizproximity.addBoundingSphereSensor(Rollup_sal1_GEODE, scale =.5)
manager.addSensor(sensor_RollupSal1)
sensor_RollupSal2 = vizproximity.addBoundingSphereSensor(Rollup_sal2_GEODE, scale =.5)
manager.addSensor(sensor_RollupSal2)

#def RollupSal (e): #SALA RV
def RollupSal ():
	def open_Salblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_sal1_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]+ 0.5, dpos1[2]]
		Rollup_sal1_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_sal2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]+ 0.5, dpos2[2]]
		Rollup_sal2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
				
	def close_Salblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_sal1_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]- 0.5, dpos1[2]]
		Rollup_sal1_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_sal2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]- 0.5, dpos2[2]]
		Rollup_sal2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.disable()
	
	global state_rollupsal
	print 'estoy en rollupsalón'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_rollupsal == 1: #CERRAR
		vizact.ontimer2(1,4, close_Salblind)
		state_rollupsal = 0
	else: #ABRIR
		vizact.ontimer2(1,4, open_Salblind)
		state_rollupsal = 1
		
#action1 = vizact.onpick(Rollup_sal1_GEODE, RollupSal)
#action2 = vizact.onpick(Rollup_sal2_GEODE, RollupSal)

#PERSIANAS COCINA
Rollup_kit_GEODE = lab.getChild('Roll up door 1-GEODE')
Rollup_kit2_GEODE = lab.getChild('Roll up door 2-GEODE')

sensor_RollupKit1 = vizproximity.addBoundingSphereSensor(Rollup_kit_GEODE, scale =.5)
manager.addSensor(sensor_RollupKit1)
sensor_RollupKit2 = vizproximity.addBoundingSphereSensor(Rollup_kit2_GEODE, scale = .5)
manager.addSensor(sensor_RollupKit2)

#def RollupKit (e): #SALA RV
def RollupKit ():
	def open_Kitblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_kit_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]+ 0.5, dpos1[2]]
		Rollup_kit_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_kit2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]+ 0.5, dpos2[2]]
		Rollup_kit2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
		
	def close_Kitblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_kit_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]- 0.5, dpos1[2]]
		Rollup_kit_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_kit2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]- 0.5, dpos2[2]]
		Rollup_kit2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.disable()
	
	global state_rollupkit
	print 'estoy en rollupkitchen'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_rollupkit == 1: #CERRAR
		vizact.ontimer2(1,4, close_Kitblind)
		state_rollupkit = 0
	else: #ABRIR
		vizact.ontimer2(1,4, open_Kitblind)
		state_rollupkit = 1
		
#action1 = vizact.onpick(Rollup_kit_GEODE, RollupKit)
#action1 = vizact.onpick(Rollup_kit2_GEODE, RollupKit)


#PERSIANA SALA DE CONTROL
Rollup_SC_GEODE = lab.getChild('roll up-GEODE')

sensor_RollupSC = vizproximity.addBoundingSphereSensor(Rollup_SC_GEODE, scale = .5)
manager.addSensor(sensor_RollupSC)

#def rollupsc(e): #SALA RV
def RollupSC ():
	def open_SCblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_SC_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]+ 0.5, dpos[2]]
		Rollup_SC_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
		
	def close_SCblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_SC_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]- 0.5, dpos[2]]
		Rollup_SC_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#luzAmbiente.disable()
	
	global state_rollupsc
	print 'estoy en rollupsc'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_rollupsc == 1: #CERRAR
		vizact.ontimer2(1,3, close_SCblind)
		state_rollupsc = 0
	else: #ABRIR
		vizact.ontimer2(1,3, open_SCblind)
		state_rollupsc = 1
		
#action = vizact.onpick(Rollup_SC_GEODE, RollupSC) #FALTA ASIGNARLE UN SWITCH

#-------------------------ENCENDER Y APAGAR LUCES-----------------------------------------------------------------

#LUZ COCINA
luzcocina = lab.getChild('Extractor-GEODE')
lightKitSwitch = lab.getChild('Box132-GEODE')

#Añadimos una fuente de luz a la lámpara.
Kitchen_light = viz.addLight()
#Definimos la luz de la lámpara como una point light, 
#esto se hace colocando el último 1 en el comando siguiente.
Kitchen_light.position( 0,0,0,1 )
Kitchen_light.direction(0,1,0)
Kitchen_light.spread(90)
Kitchen_light.disable()

#Hacemos un link entre la lámpara y la fuente de luz.
viz.link( luzcocina, Kitchen_light )

#def Kitchen_lightONOFF (e): #SALA RV
def Kitchen_lightONOFF ():
	global state_KitLight
	print 'estoy en kitchen_lightONOFF'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_KitLight == 0: #ENCENDER
		state_KitLight = 1
		Kitchen_light.color(viz.YELLOW_ORANGE)
		Kitchen_light.intensity(8)
		Kitchen_light.quadraticAttenuation(1)
		Kitchen_light.enable()
				
	elif state_KitLight == 1: #APAGAR
		Kitchen_light.disable()
		state_KitLight = 0
			

sensor_KitLight = vizproximity.addBoundingBoxSensor(lightKitSwitch, scale = (2,10,2))
manager.addSensor(sensor_KitLight)
action = vizact.onpick(lightKitSwitch, Kitchen_lightONOFF)

##LUZ SALA
#
luzsala = lab.getChild('Falso_techo-GEODE')
lightSalaSwitch = lab.getChild('Light_Switch TV')

def Sala_lightONOFF ():  #PEDIRLE A CAMILA DOS LÁMPARAS EN SALA Y DORMITORIO / PONER EL OFF
	#Añadimos una fuente de luz a la lámpara.
	Sala_light = viz.addLight()

	#Definimos la luz de la lámpara como una point light, 
	#esto se hace colocando el último 1 en el comando siguiente.
	Sala_light.position( 0,0,0,1 )
	Sala_light.direction(0,1,0)
	Sala_light.spread(90)
	

	#Hacemos un link entre la lámpara y la fuente de luz.
	viz.link( luzcocina, Sala_light )
	
	Sala_light.color(viz.YELLOW_ORANGE)
	Sala_light.intensity(8)
	Sala_light.quadraticAttenuation(1)
	
#action = vizact.onpick(lightSalaSwitch, Sala_lightONOFF)

#LUZ HABITACIÓN

luzhabitacion = lab.getChild('Inner_Back_wall-GEODE')
lightBedroomSwitch = lab.getChild('Light_Switch cama')

#Añadimos una fuente de luz a la lámpara.
Bedroom_light = viz.addLight()
#Definimos la luz de la lámpara como una point light, 
#esto se hace colocando el último 1 en el comando siguiente.
Bedroom_light.position( 0,0,0,1 )
Bedroom_light.direction(0,1,0)
Bedroom_light.spread(90)
Bedroom_light.disable()

#Hacemos un link entre la lámpara y la fuente de luz.
viz.link( luzhabitacion	, Bedroom_light )

#def Kitchen_lightONOFF (e): #SALA RV
def Bedroom_lightONOFF ():
	global state_BedroomLight
	print 'estoy en bedroom_lightONOFF'
	puerta.setEuler(0,0,-90,viz.REL_LOCAL)
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_BedroomLight == 0: #ENCENDER
		state_BedroomLight = 1
		Bedroom_light.color(viz.YELLOW)
		Bedroom_light.intensity(8)
		Bedroom_light.quadraticAttenuation(1)
		Bedroom_light.enable()
				
	elif state_BedroomLight == 1: #APAGAR
		Bedroom_light.disable()
		state_BedroomLight = 0
			

sensor_BedroomLight = vizproximity.addBoundingBoxSensor(lightBedroomSwitch, scale = (2,10,2))
manager.addSensor(sensor_BedroomLight)
#action = vizact.onpick(lightKitSwitch, Kitchen_lightONOFF)

#LUZ BAÑO



luzBathroom = lab.getChild('bATHROOM_mIRROR-GEODE')
lightBathroomSwitch = lab.getChild('Socket_single-GEODE')

#Añadimos una fuente de luz a la lámpara.
Bathroom_light = viz.addLight()
#Definimos la luz de la lámpara como una point light, 
#esto se hace colocando el último 1 en el comando siguiente.
Bathroom_light.position( 0,0,0,1 )
Bathroom_light.direction(0,1,0)
Bathroom_light.spread(90)
Bathroom_light.disable()

#Hacemos un link entre la lámpara y la fuente de luz.
viz.link( luzBathroom	, Bathroom_light )

#def Bathroom_lightONOFF (e): #SALA RV
def Bathroom_lightONOFF ():
	global state_BathroomLight
	print 'estoy en Bathroom_lightONOFF'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_BathroomLight == 0: #ENCENDER
		state_BathroomLight = 1
		Bathroom_light.color(viz.YELLOW)
		Bathroom_light.intensity(8)
		Bathroom_light.quadraticAttenuation(1)
		Bathroom_light.enable()
				
	elif state_BathroomLight == 1: #APAGAR
		Bathroom_light.disable()
		state_BathroomLight = 0
			

sensor_BathroomLight = vizproximity.addBoundingBoxSensor(lightBathroomSwitch, scale = (2,10,2))
manager.addSensor(sensor_BathroomLight)
#action = vizact.onpick(lightBathroomSwitch, Bathroom_lightONOFF)



#LUZ SC



luzSC = lab.getChild('Mirror_Frame-GEODE')
lightSCSwitch = lab.getChild('Socket005-GEODE')

#Añadimos una fuente de luz a la lámpara.
SC_light = viz.addLight()
#Definimos la luz de la lámpara como una point light, 
#esto se hace colocando el último 1 en el comando siguiente.
SC_light.position( 0,0,0,1 )
SC_light.direction(0,1,0)
SC_light.spread(90)
SC_light.disable()

#Hacemos un link entre la lámpara y la fuente de luz.
viz.link( luzSC	, SC_light )

#def SC_lightONOFF (e): #SALA RV
def SC_lightONOFF ():
	global state_SCLight
	print 'estoy en SC_lightONOFF'
		
#	if e.gesture == rightHand.getSensor().returnOpen[0]:
#		print 'nada'
#	else:
	if state_SCLight == 0: #ENCENDER
		state_SCLight = 1
		SC_light.color(viz.YELLOW)
		SC_light.intensity(8)
		SC_light.quadraticAttenuation(1)
		SC_light.enable()
				
	elif state_SCLight == 1: #APAGAR
		SC_light.disable()
		state_SCLight = 0
			

sensor_SCLight = vizproximity.addBoundingBoxSensor(lightSCSwitch, scale = (2,10,2))
manager.addSensor(sensor_SCLight)
#action = vizact.onpick(lightBathroomSwitch, Bathroom_lightONOFF)

#LUZ RV
#-------------------------------------------------------------------------------------------------------------------
# ESPEJOS SC Y BAÑO

REFLECT_MASK = viz.addNodeMask()

def addMirror(mirror,mat=None,eye=viz.BOTH_EYE):

#If mirror matrix is not specifed, get matrix of mirror object
	if mat is None:
		mat = mirror.getMatrix()

        #Position of mirror
        pos = viz.Vector(mat.getPosition())

        #Direction mirror is pointing
        dir = viz.Vector(mat.getForward())
        dir.normalize()

        #Quaternion rotation of mirror
        quat = mat.getQuat()

        #Create render texture
        tex = viz.addRenderTexture()

        #Create render node for rendering reflection
        lens = viz.addRenderNode(size=[512,512])
        lens.attachTexture(tex)
        lens.setInheritView(True,viz.POST_MULT)
        lens.disable(viz.CULL_FACE,op=viz.OP_OVERRIDE)
        lens.setCullMask(REFLECT_MASK)
        if eye == viz.LEFT_EYE:
            lens.disable(viz.RENDER_RIGHT)
            mirror.setMask(REFLECT_MASK|viz.RIGHT_MASK,mode=viz.MASK_REMOVE)
        elif eye == viz.RIGHT_EYE:
            lens.disable(viz.RENDER_LEFT)
            mirror.setMask(REFLECT_MASK|viz.LEFT_MASK,mode=viz.MASK_REMOVE)
        else:
            mirror.setMask(REFLECT_MASK,mode=viz.MASK_REMOVE)

        #Setup reflection matrix
        rot = viz.Matrix.quat(quat)
        invRot = rot.inverse()
        lens.setMatrix(viz.Matrix.translate(-pos)*invRot*viz.Matrix.scale(1,1,-1)*rot*viz.Matrix.translate(pos))

        #Setup reflection clip plane
        s = viz.sign(viz.Vector(dir) * viz.Vector(pos))
        plane = vizmat.Plane(pos=pos,normal=dir)
        dist = plane.distance([0,0,0])
        lens.clipPlane([dir[0],dir[1],dir[2],s*dist-0.01])

        #Project reflection texture onto mirror
        mirror.texture(tex)
        mirror.texGen(viz.TEXGEN_PROJECT_EYE)

#ESPEJO SC
mirror = lab.getChild ('Mirror_Glass-GEODE')
m = viz.Matrix()
m.setPosition(mirror.getPosition(viz.ABS_GLOBAL))
m.setEuler(90,0,0)
    
#Apply mirror settings to mirror object
addMirror(mirror,m)

#ESPEJO BAÑO
mirror = lab.getChild ('bATHROOM_mIRROR')
m = viz.Matrix()
m.setPosition(mirror.getPosition(viz.ABS_GLOBAL))
m.setEuler(90,0,0)

#Apply mirror settings to mirror object
addMirror(mirror,m)

#--------------------------ENTER AND EXIT PROXIMITY--------------------------------------------------

#ENTER PROXIMITY SENSORS
def EnterProximity(e):
	print 'Entered'
	global texto
	global sen
	if e.sensor == sensor_DoorHome:
		print 'está entrando en sensor puerta home'
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la puerta de la casa',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 1
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, doorHome)
		#viz.callback(hand.HAND_GESTURE_EVENT, doorHome(e))
		
	if e.sensor == sensor_DoorSC:
		print 'está entrando en sensor puerta SC'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la puerta de la Sala de Control',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 2
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, doorSC)
		#viz.callback(hand.HAND_GESTURE_EVENT, doorSC(e))
	if e.sensor == sensor_doorSuichbath:
		print 'está entrando en sensor puerta baño'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la puerta del baño',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 3
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, doorbath)
		#viz.callback(hand.HAND_GESTURE_EVENT, doorbath(e))
	if e.sensor == sensor_planta:
		print 'prueba planta'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Planta',parent=viz.SCREEN, pos=[0.5,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 4
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, doorbath)
	if e.sensor == sensor_Kitchen:
		print 'está entrando en sensor puerta cocina'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar el ventanal de la cocina',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 5
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, doorKitchen)
		#viz.callback(hand.HAND_GESTURE_EVENT, doorKitchen(e))
	if e.sensor == sensor_salon:
		print 'está entrando en sensor puerta salón'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar el ventanal del salón',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 6
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, doorSalon)
		#viz.callback(hand.HAND_GESTURE_EVENT, doorSalon(e))
	if e.sensor == sensor_RollupBED:
		print 'está entrando en sensor Rollup bed'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la persiana de la habitación',parent=viz.SCREEN,pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 7
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, RollupBed)
		#viz.callback(hand.HAND_GESTURE_EVENT, RollupBed(e))
	if e.sensor == sensor_RollupSal1:
		print 'está entrando en sensor persianas salón'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la persiana del salón',parent=viz.SCREEN,pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 8
	if e.sensor == sensor_RollupSal2:
		print 'está entrando en sensor persianas salón'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la persiana del salón',parent=viz.SCREEN,pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 8
		#viz.callback(hand.HAND_GESTURE_EVENT, RollupSal)
	if e.sensor == sensor_RollupKit1:
		print 'está entrando en sensor persianas cocina'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la persiana de la cocina',parent=viz.SCREEN,pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 9
	if e.sensor == sensor_RollupKit2:
		print 'está entrando en sensor persianas cocina'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la persiana de la cocina',parent=viz.SCREEN,pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 9
		#viz.callback(hand.HAND_GESTURE_EVENT, RollupKit)
	if e.sensor == sensor_RollupSC:
		print 'está entrando en sensor persiana SC'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para abrir/cerrar la persiana de la SC',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 10
		#viz.callback(hand.HAND_GESTURE_EVENT, RollupSC)
	if e.sensor == sensor_KitLight:
		print 'está entrando en sensor Luz Cocina'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para encender/apagar la luz de la cocina',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 11
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, Kitchen_lightONOFF)
		#viz.callback(hand.HAND_GESTURE_EVENT, Kitchen_lightONOFF(e))
		
	if e.sensor == sensor_BedroomLight:
		print 'está entrando en sensor Luz Habitacion'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para encender/apagar la luz de la habitacion',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 12
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, Kitchen_lightONOFF)
		#viz.callback(hand.HAND_GESTURE_EVENT, Kitchen_lightONOFF(e))	
		
	if e.sensor == sensor_BathroomLight:
		print 'está entrando en sensor Luz Baño'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para encender/apagar la luz del baño',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 13
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, Kitchen_lightONOFF)
		#viz.callback(hand.HAND_GESTURE_EVENT, Kitchen_lightONOFF(e))	
			
			
	if e.sensor == sensor_SCLight:
		print 'está entrando en sensor Luz SC'
		
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Click para encender/apagar la luz del SC',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		sen = 14
		#vizact.onmousedown(viz.MOUSEBUTTON_LEFT, Kitchen_lightONOFF)
		#viz.callback(hand.HAND_GESTURE_EVENT, Kitchen_lightONOFF(e))			
def ExitProximity(e):
	global sen
	print 'Exited'
	texto.visible(viz.OFF)
	sen = 0
	#e.sensor = []
vizact.onkeydown(' ',manager.setDebug,viz.TOGGLE)  #Para esconder las áreas de sensores

manager.onEnter(None, EnterProximity)
manager.onExit(None, ExitProximity)

#------------------------------CLICK MOUSE / WAND ----------------------------------------------------

#def click_mouse(e): #SALA RV
def click_mouse(): #CONTROL COMPU
	global sen
	if sen == 0:
		global texto
		texto.visible(viz.OFF) #Borra el texto que hubiera
		texto = viz.addText('Elija un elemento para realizar la acción',parent=viz.SCREEN, pos=[0.1,0.900,0],scale=[0.5,0.5,1], color = viz.BLUE) #Añade el texto del objeto
		texto.visible(viz.ON)
		#vizact.ontimer2(5, 0, texto.visible(viz.OFF))
	if sen == 1:
		#doorHome(e) #SALA RV
		doorHome()
	if sen == 2:
		#doorSC(e) #SALA RV
		doorSC()
	if sen == 3:
		#doorbath(e) #SALA RV
		doorbath()
	if sen == 4:
		print 'planta'
	if sen == 5:
		#doorKitchen(e) #SALA RV
		doorKitchen()
	if sen == 6:
		#doorSalon(e) #SALA RV
		doorSalon()
	if sen == 7:
		#RollupBed(e)  #SALA RV
		RollupBed()
	if sen == 8:
		#RollupSal(e)  #SALA RV
		RollupSal()
	if sen == 9:
		#RollupKit(e) #SALA RV
		RollupKit()
	if sen == 10:
		#RollupSC(e) #SALA RV
		RollupSC()
	if sen == 11:
		#Kitchen_lightONOFF(e) #SALA RV
		Kitchen_lightONOFF()
	if sen == 12:
		#Bedroom_lightONOFF(e) #SALA RV
		Bedroom_lightONOFF()	
	if sen == 13:
		#Bathroom_lightONOFF(e) #SALA RV
		Bathroom_lightONOFF()
	if sen == 14:
		#SC_lightONOFF(e) #SALA RV
		SC_lightONOFF()		
		
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, click_mouse) #CONTROL COMPU



####--------------------------------------------------- CODIGO HTML-------------------------------------------------------------

#Pagina de test: http://localhost:8080/vizhtml/custom_handler/
# Display form submitted message on screen
info = vizinfo.InfoPanel('')

code = """
<html>
<head>
    <title>vizhtml Custom Handler Example</title>
</head>
<body onload="document.the_form.message.focus();">
<img src='ball.jpg'>
<form name="the_form" method="post">
    <table>
        <tr>
            <td>Frame Number:</td>
            <td>{frame}</td>
        </tr>
        <tr>
            <td>Message:</td>
            <td><input type="text" name="message" value="{message}"></td>
        </tr>
        <tr>
            <td></td>
            <td><input type="submit" value="Submit"></td>
        </tr>
    </table>
</form>
</body>
</html>
"""
class ExampleRequestHandler(vizhtml.PageRequestHandler):

    def handle_request(self,request):
        """@args vizhtml.VizardHTTPRequestHandler()"""
        #viz.clearcolor(viz.SKYBLUE)
        #viz.addChild('ground_grass.osgb')
        #viz.MainView.setPosition([0,1.8,-10])
        #carousel = viz.addChild('carousel.wrl')
        #carousel.addAction(vizact.spin(0,1,0,20))
         
     #   print request.log_request                                                                          QUITADO
        

        # If request is for a resource (e.g. image), then let vizhtml handle it
        if request.resource_path:
            return

        # If form was submitted, put message back into page
        if request.form_event:
            message = cgi.escape(request.form_event.message,True)
            if message ==doorBath:
                doorbath()
                print 'sale' 
        else:
            message = ''

        # Send html code with dynamic content
        # Envía el código HTML especificado en el navegador.
        request.send_html_code(code.format(frame=viz.getFrameNumber(),message=message))

#Registra una clase controlador personalizado con el servidor vizhtml.
vizhtml.registerHandlerClass('custom_handler',ExampleRequestHandler,directory='.')

def HandleForm(e):
    info.setText(e.message)
vizhtml.onFormSubmit(HandleForm)

###-------------------------------------------FIN PARTE HTML-----------------------------------------------------------------


#viz.callback(hand.HAND_GESTURE_EVENT, click_mouse)  #DESCOMENTAR ESTO PARA SALA RV