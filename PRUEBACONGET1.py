import cgi
import viz
import vizinfo
import vizhtml
from urlparse import urlparse
viz.setMultiSample(4)
viz.go()
import vizcam
import vizact
import viztracker #DESCOMENTAR ESTO PARA LA SALA DE RV
import hand
import vizproximity
import vizshape
import viztask
import cgi
viz.cam.setHandler(vizcam.KeyboardCamera())
viz.phys.enable()
viz.collision(viz.ON)



########################CODIGO NORMAL #################################################################

viz.MainView.setPosition(1, 1.8, 3)
viz.MainView.setEuler(30, 0, 0)

viz.MainView.getHeadLight().intensity(0.5) #Para que se vea oscuro mientras no estén encendidas las luces ni las persianas abiertas

label = viz.addText('LifeSTech',parent=viz.SCREEN,pos=[0.005,0.947,0],scale=[0.5,0.5,1], color = viz.PURPLE)
alojeno = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')
alojeno2 = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')
alojeno3 = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')
alojeno4 = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')

alojeno2.setScale(0.05,0.05,0.05)
alojeno3.setScale(0.05,0.05,0.05)
alojeno4.setScale(0.1,0.05,0.05)

alojeno.setPosition(1,3.5,6,viz.ABS_GLOBAL)
alojeno4.setPosition(-6.660562515258789, 3.5, 8.53273868560791)
alojeno3.setPosition(1,3.5,6,viz.ABS_GLOBAL)
alojeno.setPosition(5,0,3,viz.REL_GLOBAL)
alojeno.setScale(0.05,0.05,0.05)
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
cabinavater = lab.getChild('Toilet_Tank-GEODE')
print cabinavater.getPosition(viz.ABS_GLOBAL)
alojeno2.setPosition(-2.8618810176849365, 3.5, 6,viz.ABS_GLOBAL)




#Importamos tracker de la mano
#rightHand = viztracker.get('righthand') #DESCOMENTAR ESTO PARA LA SALA DE RV

##PRUEBA DE PANTALLA PARA SALA RV
#pantalla = viz.add ('08 DA-LITE Cinema Contour.obj', scale=[0.002]*3)
#pantalla.setPosition([-1, 0.258, 1.5])

#INICIALIZACIÓN DE VARIABLES
state_doorHome = 0
state_doorHome_quiero = 1
state_doorbath = 1
state_doorbath_quiero = 0
state_doorkit = 0
state_doorkit_quiero = 1
state_doorsal= 0
state_doorsal_quiero = 1
state_rollupbed = 0
state_rollupbed_quiero = 1
state_rollupsal = 0
state_rollupsal_quiero = 1
state_rollupkit = 0
state_rollupkit_quiero = 1
state_rollupsc = 0
state_rollupsc_quiero = 1
state_doorSC = 0
state_doorSC_quiero = 1
state_KitLight = 0
state_KitLight_quiero = 1
state_BedroomLight = 0  ##NUEVO
state_BedroomLight_quiero = 1
state_BathroomLight = 0 ##NUEVO
state_BathroomLight_quiero = 1
state_SCLight = 0 ##NUEVO
state_SCLight_quiero = 1
state_SalaLight = 0 ##NUEVO
state_SalaLight_quiero = 1
state_RVLight = 0 ##NUEVO
state_RVLight_quiero = 1

sen = 0


#INICIALIZACIÓN TEXTO INFO
texto = viz.addText('',parent=viz.SCREEN, pos=[0.005,0.927,0], scale=[0.5,0.5,1], color = viz.PURPLE)




# Add the tracker (hand) as proximity target
#target =  vizproximity.Target(viz.MainView)
#Add the object that will do the grabbing   PARA CONTROL EN LA COMPU
hand = viz.addChild('marker.wrl')
mouseTracker = viztracker.MouseTracker()
mouseTracker.scroll(-8)
item = viz.link(mouseTracker,hand)

#-------------------------------ABRIR Y CERRAR PUERTAS-------------------------------------------------------

#ABRIR Y CERRAR PUERTA SALA DE CONTROL

DoorSC_GEODE = lab.getChild('Door sala control').getChild ('Box010')
Chapa = lab.getChild ('Chapa')
Cilindro = lab.getChild('Cylinder001')
link_DoorSC = viz.link(DoorSC_GEODE, Chapa)
link2_DoorSC = viz.link(DoorSC_GEODE, Cilindro)

print 'esto es lo que necesito:'
print lab.getChild('Socket005-GEODE').getPosition(viz.ABS_GLOBAL)




#def doorSCOpen(e): #SALA RV
def doorSCOpen():	
	print 'estoy en doorSCOpen'
	global state_doorSC
	global state_doorSC_quiero
	state_doorSC_quiero = 1
	print 'vista Door_SC', viz.MainView.getPosition()
	if state_doorSC == 0 and state_doorSC_quiero == 1 : #ABRIR
		eule = [90,0,0]
		DoorSC_GEODE.setEuler(eule, viz.REL_LOCAL)
		state_doorSC = 1

#vizact.onpick(DoorSC_GEODE,  doorSC)


#def doorSCClose(e): #SALA RV
def doorSCClose():	
	print 'estoy en doorSCClose'
	global state_doorSC
	global state_doorSC_quiero
	state_doorSC_quiero = 0
	if state_doorSC == 1 and state_doorSC_quiero == 0 : #CERRAR
		eule2 = [-90,0,0]
		DoorSC_GEODE.setEuler(eule2, viz.REL_LOCAL)
		state_doorSC = 0

#vizact.onpick(DoorSC_GEODE,  doorSC)


#ABRIR Y CERRAR PUERTA DE ENTRADA

DoorHome_GEODE = lab.getChild('Door Principal').getChild ('Box101-OFFSET')
Cham = lab.getChild ('ChamferBox002')
Cylinder = lab.getChild('Cylinder002')
Handle = lab.getChild('Door_Handle001')
Handle_base = lab.getChild('Door_handle_Base001')
Rectangle = lab.getChild('Rectangle014')



#link_DoorHome = viz.link(DoorHome_GEODE, Cham)
#link2_DoorHome = viz.link(DoorHome_GEODE, Cylinder,3)
#link3_DoorHome = viz.link(DoorHome_GEODE, Handle,2)
#link4_DoorHome = viz.link(DoorHome_GEODE, Handle_base,1)
#link5_DoorHome = viz.link(DoorHome_GEODE, Rectangle)

print 'posicionPuerta'
print DoorHome_GEODE.getPosition(viz.ABS_GLOBAL)


#def doorHome(e): 
def doorHomeOpen():
	print 'estoy en doorHomeOpen'
	global state_doorHome
	global state_doorHome_quiero
	state_doorHome_quiero = 1
	
	print 'vista Door_Home', viz.MainView.getPosition()
	print 'state_doorHome '
	print state_doorHome
	print 'state_doorHomequiero '
	print state_doorHome_quiero
	

	if ((state_doorHome == 0) and (state_doorHome_quiero == 1)) : #ABRIR

		eule = [0,0,90]
		DoorHome_GEODE.setEuler(eule, viz.REL_LOCAL)
		Handle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Handle.setEuler (0,0,90,viz.ABS_GLOBAL)
		Handle_base.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Cham.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Rectangle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		
		
		#Handle.setEuler (90,0,0,viz.ABS_GLOBAL)
		state_doorHome = 1
		print 'se ha metido en else'
		print 'state_doorHome2 '
		print state_doorHome
		print 'state_doorHomequiero2 '
		print state_doorHome_quiero
		
		print 'posicionPuerta'
		print DoorHome_GEODE.getPosition(viz.ABS_GLOBAL)

		print 'posicionHandle'
		print Handle.getPosition(viz.ABS_GLOBAL)

		print 'posicionCilindro'
		print Cylinder.getPosition(viz.ABS_GLOBAL)
		
		
		
#def doorHomeClose(e): 
def doorHomeClose():
	print 'estoy en doorHome'
	global state_doorHome
	global state_doorHome_quiero
	state_doorHome_quiero = 0
	
	print 'state_doorHomeC '
	print state_doorHome
	print 'state_doorHomequieroC '
	print state_doorHome_quiero
	
	
	if ((state_doorHome == 1) and (state_doorHome_quiero == 0)) : #CERRAR
		eule2 = [0,0,-90]
		DoorHome_GEODE.setEuler(eule2, viz.REL_LOCAL)
		Handle.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
		Handle.setEuler (0,0,-90,viz.REL_LOCAL)
		Handle_base.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
		Cham.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
		Rectangle.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
		
		
		
		state_doorHome = 0
		print 'se ha metido en if'
	
		
		
		
		
#vizact.onpick(DoorHome_GEODE,  doorHome)


#ABRIR Y CERRAR LA PUERTA DEL BAÑO
Doorbath_GEODE = lab.getChild('Toilet_Door-GEODE')
Circle_GEODE = lab.getChild('Circle002-GEODE')

#def doorbathOpen(e): #SALA RV
def doorbathOpen():
	print 'estoy en doorbathOpen'
	global state_doorbath
	global state_doorbath_quiero
	state_doorbath_quiero = 1
	print 'vista Door_Bath', viz.MainView.getPosition()

	if state_doorbath == 0 and state_doorbath_quiero == 1: #ABRIR
		dpos = Doorbath_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1], dpos[2] - 0.8]
		Doorbath_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = Circle_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0], cpos[1], cpos[2] - 0.75]
		Circle_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
		state_doorbath = 1
	
doorSuich_bath = lab.getChild('Light_Switch out  bathroom')
node = viz.addChild('plant.osgb',pos=(0,0.58,5))


#def doorbathClose(e): #SALA RV
def doorbathClose():
	print 'estoy en doorbath'
	global state_doorbath
	global state_doorbath_quiero 
	state_doorbath_quiero = 0

	if state_doorbath == 1 and state_doorbath_quiero == 0: #CERRAR
		dpos = Doorbath_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1], dpos[2] + 0.8]
		Doorbath_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = Circle_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0], cpos[1], cpos[2] + 0.75]
		Circle_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
		state_doorbath = 0

	
doorSuich_bath = lab.getChild('Light_Switch out  bathroom')
node = viz.addChild('plant.osgb',pos=(0,0.58,5))


#ABRIR Y CERRAR PUERTAS COCINA Y SALÓN
DoorKitchen_GEODE = lab.getChild('Glass002-GEODE')
DoorKit_frame_GEODE = lab.getChild('Door_Frame001-GEODE')

DoorSalon_GEODE = lab.getChild('Glass004-GEODE')
DoorSal_frame_GEODE = lab.getChild('Door_Frame003-GEODE')

#def doorKitchenOpen (e): #SALA RV
def doorKitchenOpen ():
	def openDoorKitchen ():
		#viz.MainView.setPosition(-0.46573784947395325, 2.407294273376465, 4.4074883460998535)
		print 'vista Door_Kitchen', viz.MainView.getPosition()
		print 'vista Door_Kitchen euler', viz.MainView.getEuler()
		dpos = DoorKitchen_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] + 0.6, dpos[1], dpos[2]]
		DoorKitchen_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorKit_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] + 0.6, cpos[1], cpos[2]]
		DoorKit_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	global state_doorkit
	global state_doorkit_quiero
	state_doorkit_quiero = 1
	print 'estoy en doorkitchen'
		
	if state_doorkit == 0 and state_doorkit_quiero == 1: #ABRIR
		vizact.ontimer2(1,2,openDoorKitchen)
		state_doorkit = 1


#def doorKitchenClose (e): #SALA RV
def doorKitchenClose ():
	def closeDoorKitchen ():
		dpos = DoorKitchen_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] - 0.6, dpos[1], dpos[2]]
		DoorKitchen_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorKit_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] - 0.6, cpos[1], cpos[2]]
		DoorKit_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	global state_doorkit
	global state_doorkit_quiero
	state_doorkit_quiero = 0
	print 'estoy en doorkitchen'
	
	if state_doorkit == 1 and state_doorkit_quiero == 0: #CERRAR
		vizact.ontimer2(1,2,closeDoorKitchen)
		state_doorkit = 0
	



#def doorSalonOpen (e): #SALA RV
def doorSalonOpen ():
	def openDoorSalon ():
		dpos = DoorSalon_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] + 0.6, dpos[1], dpos[2]]
		DoorSalon_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorSal_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] + 0.6, cpos[1], cpos[2]]
		DoorSal_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	global state_doorsal
	global state_doorsal_quiero
	state_doorsal_quiero = 1
	print 'estoy en doorsalónOpen'

	if state_doorsal == 0 and state_doorsal_quiero == 1: #ABRIR
		vizact.ontimer2(1,2,openDoorSalon)
		state_doorsal = 1	


doorSuich_kitchen = lab.getChild('Light_Switch Kitchen')

doorSuich_salon = lab.getChild('Light_Switch salon')



#def doorSalonClose (e): #SALA RV
def doorSalonClose ():
	def closeDoorSalon ():
		dpos = DoorSalon_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] - 0.6, dpos[1], dpos[2]]
		DoorSalon_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorSal_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] - 0.6, cpos[1], cpos[2]]
		DoorSal_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	global state_doorsal
	global state_doorsal_quiero
	state_doorsal_quiero = 0
	print 'estoy en doorsalónClose'
		
	if state_doorsal == 1 and state_doorsal_quiero == 0: #CERRAR
		vizact.ontimer2(1, 2, closeDoorSalon)
		state_doorsal = 0

doorSuich_kitchen = lab.getChild('Light_Switch Kitchen')

doorSuich_salon = lab.getChild('Light_Switch salon')






#--------------------------------------ABRIR Y CERRAR PERSIANAS-------------------------------------------------------
#LUZ AMBIENTE
luzAmbiente = viz.addLight()
luzAmbiente.disable()

#PERSIANAS DORMITORIO
Rollup_bed_GEODE = lab.getChild('Blind bedroom-GEODE')

#def RollupBedOpen (e): #SALA RV
def RollupBedOpen ():
	print 'se mete en RollUpBedOpen'
	def open_bedblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_bed_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]+ 0.5, dpos[2]]
		Rollup_bed_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
		
	global state_rollupbed
	global state_rollupbed_quiero
	state_rollupbed_quiero = 1
	print 'estoy en rollupbed'
		
	if state_rollupbed == 0 and state_rollupbed_quiero == 1: #ABRIR
		print 'se mete en ABRIR'
		vizact.ontimer2(1,6, open_bedblind)
		state_rollupbed = 1
		
RollupSuich_bed = lab.getChild ('Light_Switch bedroom')



#def RollupBedClose (e): #SALA RV
def RollupBedClose ():
	
	def close_bedblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_bed_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]- 0.5, dpos[2]]
		Rollup_bed_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#Rollup_bed_GEODE.alpha(1)
		#luzAmbiente.disable()
		
	global state_rollupbed
	global state_rollupbed_quiero
	state_rollupbed_quiero = 0
	print 'estoy en rollupbed'
		

	if state_rollupbed == 1 and state_rollupbed_quiero == 0: #CERRAR
		vizact.ontimer2(1,6, close_bedblind)
		state_rollupbed = 0
		
RollupSuich_bed = lab.getChild ('Light_Switch bedroom')



#PERSIANAS SALÓN
Rollup_sal1_GEODE = lab.getChild('Roll up door 3-GEODE')
Rollup_sal2_GEODE = lab.getChild('Roll up door 4-GEODE')



#def RollupSalOpen (e): #SALA RV
def RollupSalOpen ():
	
	def open_Salblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		print 'se mete en RollUpSalonOpen'
		dpos1 = Rollup_sal1_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]+ 0.5, dpos1[2]]
		Rollup_sal1_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_sal2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]+ 0.5, dpos2[2]]
		Rollup_sal2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
	
	global state_rollupsal
	global state_rollupsal_quiero
	state_rollupsal_quiero = 1
	print 'estoy en rollupsalón'
	print 'state_roll_up_sal'
	print state_rollupsal
	print 'state_rollupsal_quiero'
	print state_rollupsal_quiero
	if state_rollupsal == 0 and state_rollupsal_quiero == 1: #ABRIR
		print 'se mete en ABRIR Salon'
		vizact.ontimer2(1,4, open_Salblind)
		state_rollupsal = 1

#def RollupSalClose (e): #SALA RV
def RollupSalClose ():
				
	def close_Salblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_sal1_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]- 0.5, dpos1[2]]
		Rollup_sal1_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_sal2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]- 0.5, dpos2[2]]
		Rollup_sal2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.disable()
	
	global state_rollupsal
	global state_rollupsal_quiero
	state_rollupsal_quiero = 0
	print 'estoy en rollupsalón'

	if state_rollupsal == 1 and state_rollupsal_quiero == 0 : #CERRAR
		vizact.ontimer2(1,4, close_Salblind)
		state_rollupsal = 0


#PERSIANAS COCINA
Rollup_kit_GEODE = lab.getChild('Roll up door 1-GEODE')
Rollup_kit2_GEODE = lab.getChild('Roll up door 2-GEODE')


#def RollupKitOpen (e): #SALA RV
def RollupKitOpen ():
	def open_Kitblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_kit_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]+ 0.5, dpos1[2]]
		Rollup_kit_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_kit2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]+ 0.5, dpos2[2]]
		Rollup_kit2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
	
	global state_rollupkit
	global state_rollupkit_quiero
	state_rollupkit_quiero = 1
	print 'estoy en rollupkitchen'
		
	if state_rollupkit == 0 and state_rollupkit_quiero == 1: #ABRIR
		vizact.ontimer2(1,4, open_Kitblind)
		state_rollupkit = 1


#def RollupKitClose (e): #SALA RV
def RollupKitClose ():
	
	def close_Kitblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos1 = Rollup_kit_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]- 0.5, dpos1[2]]
		Rollup_kit_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_kit2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]- 0.5, dpos2[2]]
		Rollup_kit2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		#luzAmbiente.disable()
	
	global state_rollupkit
	global state_rollupkit_quiero
	state_rollupkit_quiero = 0
	print 'estoy en rollupkitchen'
		
	if state_rollupkit == 1 and state_rollupkit_quiero == 0: #CERRAR
		vizact.ontimer2(1,4, close_Kitblind)
		state_rollupkit = 0
	


#PERSIANA SALA DE CONTROL
Rollup_SC_GEODE = lab.getChild('roll up-GEODE')


#def rollupscOpen(e): #SALA RV
def RollupSCOpen ():
	def open_SCblind(): #ABRE LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_SC_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]+ 0.5, dpos[2]]
		Rollup_SC_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#luzAmbiente.enable()
	
	global state_rollupsc
	global state_rollupsc_quiero
	state_rollupsc_quiero = 1
	print 'estoy en rollupsc'
		
	if state_rollupsc == 0 and state_rollupsc_quiero == 1: #ABRIR
		vizact.ontimer2(1,3, open_SCblind)
		state_rollupsc = 1


#def rollupscClose(e): #SALA RV
def RollupSCClose ():

	def close_SCblind(): #CIERRA LA PERSIANA DE FORMA CORRIDA
		dpos = Rollup_SC_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]- 0.5, dpos[2]]
		Rollup_SC_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		#luzAmbiente.disable()
	
	global state_rollupsc
	global state_rollupsc_quiero
	state_rollupsc_quiero = 0
	print 'estoy en rollupsc'

	if state_rollupsc == 1 and state_rollupsc_quiero == 0: #CERRAR
		vizact.ontimer2(1,3, close_SCblind)
		state_rollupsc = 0
		

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

#def Kitchen_lightONOFFOpen (e): #SALA RV
def Kitchen_lightONOFFOpen ():
	global state_KitLight
	global state_KitLight_quiero
	state_KitLight_quiero = 1
	print 'estoy en kitchen_lightONOFF'
		
	if state_KitLight == 0 and state_KitLight_quiero == 1: #ENCENDER
		state_KitLight = 1
		Kitchen_light.color(viz.YELLOW)
		Kitchen_light.intensity(8)
		Kitchen_light.quadraticAttenuation(1)
		Kitchen_light.enable()
				


#def Kitchen_lightONOFFClose (e): #SALA RV
def Kitchen_lightONOFFClose ():
	global state_KitLight
	global state_KitLight_quiero
	state_KitLight_quiero = 0
	print 'estoy en kitchen_lightONOFF'
						
	if state_KitLight == 1 and state_KitLight_quiero == 0: #APAGAR
		Kitchen_light.disable()
		state_KitLight = 0
			






##LUZ SALA
#
luzsala = alojeno3
lightSalaSwitch = lab.getChild('Light_Switch TV')


#Añadimos una fuente de luz a la lámpara.
Sala_light = viz.addLight()
#Definimos la luz de la lámpara como una point light, 
#esto se hace colocando el último 1 en el comando siguiente.
Sala_light.position( 0,0,0,1 )
Sala_light.direction(0,1,0)
Sala_light.spread(90)
Sala_light.disable()

#Hacemos un link entre la lámpara y la fuente de luz.
viz.link( luzsala	, Sala_light )

#def Kitchen_lightONOFFOpen (e): #SALA RV
def Sala_lightONOFFOpen ():
	global state_SalaLight
	global state_SalaLight_quiero
	state_SalaLight_quiero = 1
	print 'estoy en Sala_lightONOFF'

	if state_SalaLight == 0 and state_SalaLight_quiero == 1 : #ENCENDER
		state_SalaLight = 1
		Sala_light.color(viz.YELLOW)
		Sala_light.intensity(8)
		Sala_light.quadraticAttenuation(1)
		Sala_light.enable()

			
#def Kitchen_lightONOFFClose (e): #SALA RV
def Sala_lightONOFFClose ():
	global state_SalaLight
	global state_SalaLight_quiero
	state_SalaLight_quiero = 0
	print 'estoy en Sala_lightONOFF'
				
	if state_SalaLight == 1 and state_SalaLight_quiero == 0 : #APAGAR
		Sala_light.disable()
		state_SalaLight = 0



#LUZ HABITACIÓN

luzhabitacion = alojeno
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

#def Bedroom_lightONOFFOpen (e): #SALA RV
def Bedroom_lightONOFFOpen ():
	global state_BedroomLight
	global state_BedroomLight_quiero
	state_BedroomLight_quiero = 1
	print 'estoy en bedroom_lightONOFF'
	puerta.setEuler(0,0,-90,viz.REL_LOCAL) #--------------------------------------------------------------

	if state_BedroomLight == 0 and state_BedroomLight_quiero == 1 : #ENCENDER
		state_BedroomLight = 1
		Bedroom_light.color(viz.YELLOW)
		Bedroom_light.intensity(8)
		Bedroom_light.quadraticAttenuation(1)
		Bedroom_light.enable()
				
#def Bedroom_lightONOFFOpen (e): #SALA RV
def Bedroom_lightONOFFClose ():
	global state_BedroomLight
	global state_BedroomLight_quiero
	state_BedroomLight_quiero = 0 
	print 'estoy en bedroom_lightONOFF'

	if state_BedroomLight == 1 and state_BedroomLight_quiero == 0 : #APAGAR
		Bedroom_light.disable()
		state_BedroomLight = 0


#LUZ BAÑO



luzBathroom = alojeno2
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

#def Bathroom_lightONOFFOpen (e): #SALA RV
def Bathroom_lightONOFFOpen ():
	global state_BathroomLight
	global state_BathroomLight_quiero
	state_BathroomLight_quiero = 1
	print 'estoy en Bathroom_lightONOFF'

	if state_BathroomLight == 0 and state_BathroomLight_quiero == 1: #ENCENDER
		state_BathroomLight = 1
		Bathroom_light.color(viz.YELLOW)
		Bathroom_light.intensity(8)
		Bathroom_light.quadraticAttenuation(1)
		Bathroom_light.enable()
			


#def Bathroom_lightONOFFClose (e): #SALA RV
def Bathroom_lightONOFFClose ():
	global state_BathroomLight
	global state_BathroomLight_quiero
	state_BathroomLight_quiero = 0
	print 'estoy en Bathroom_lightONOFF'
				
	if state_BathroomLight == 1 and state_BathroomLight_quiero == 0: #APAGAR
		Bathroom_light.disable()
		state_BathroomLight = 0
			


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

#def SC_lightONOFFOpen (e): #SALA RV
def SC_lightONOFFOpen ():
	global state_SCLight
	global state_SCLight_quiero
	state_SCLight_quiero = 1
	print 'estoy en SC_lightONOFF'
		
	if state_SCLight == 0 and state_SCLight_quiero == 1 : #ENCENDER
		state_SCLight = 1
		SC_light.color(viz.YELLOW)
		SC_light.intensity(8)
		SC_light.quadraticAttenuation(1)
		SC_light.enable()
			


#def SC_lightONOFF (e): #SALA RV
def SC_lightONOFFClose ():
	global state_SCLight
	global state_SCLight_quiero
	state_SCLight_quiero = 0
	print 'estoy en SC_lightONOFF'

				
	if state_SCLight == 1 and state_SCLight_quiero == 0 : #APAGAR
		SC_light.disable()
		state_SCLight = 0
			

#action = vizact.onpick(lightBathroomSwitch, Bathroom_lightONOFF)





#LUZ RV


luzRV = alojeno4
#lightBathroomSwitch = lab.getChild('Socket_single-GEODE')

#Añadimos una fuente de luz a la lámpara.
RV_light = viz.addLight()
#Definimos la luz de la lámpara como una point light, 
#esto se hace colocando el último 1 en el comando siguiente.
RV_light.position( 0,0,0,1 )
RV_light.direction(0,1,0)
RV_light.spread(90)
RV_light.disable()

#Hacemos un link entre la lámpara y la fuente de luz.
viz.link( luzRV	, RV_light )

#def RV_lightONOFFOpen (e): #SALA RV
def RV_lightONOFFOpen ():
	global state_RVLight
	global state_RVLight_quiero
	state_RVLight_quiero = 1
	print 'estoy en RV_lightONOFF'

	if state_RVLight == 0 and state_RVLight_quiero == 1: #ENCENDER
		print 'estoy en RV_light opeeeeeen'
		RV_light.color(viz.YELLOW)
		RV_light.intensity(8)
		RV_light.quadraticAttenuation(1)
		RV_light.enable()
		state_RVLight = 1	


#def RV_lightONOFFClose (e): #SALA RV
def RV_lightONOFFClose ():
	global state_RVLight
	global state_RVLight_quiero
	state_RVLight_quiero = 0
	print 'estoy en RV_lightONOFF'
	print 'luz'
	print state_RVLight
	print 'quiero'
				
	if state_RVLight == 1 and state_RVLight_quiero == 0: #APAGAR
		print 'estoy en RV_light clooose'
		RV_light.disable()
		state_RVLight = 0
			








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



########################FIN CODIGO NORMAL###################################################################

#########################################CODIGO HTML ###################################################################################

# test url: http://localhost:8080/vizhtml/custom_handler/device/name/value/value2/valuen?command=set&device=door&value=2

#Enable full screen anti-aliasing (FSAA) to smooth edges



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
    <table>
        <tr>
            <td>MESSAGE OPTIONS:</td>
        </tr>
        <tr>
            <td>-Open main door : doorHomeOpen</td>
		<tr>	
            <td>-Open Livingroom door : doorSalonOpen</td>
		</tr>
		<tr>
		    <td>-Open bathroom door : doorBathOpen</td>
		</tr>
		<tr>
			<td>-Open kitchen door : doorKitchenOpen<td>
		</tr>
		<tr>
		    <td>-Open SC door : doorSCOpen</td>
		</tr>
		<tr>
		    <td>-Up bedroom blind : RollupBedOpen</td>
		</tr>    
		<tr>
		    <td>-Up kitchen blind : RollupKitOpen</td>
		</tr>   
		<tr>
			<td>-Up Living room blind : RollupSalOpen</td>
		</tr>   
		<tr>
			<td>-Up SC blind : RollupSCOpen</td>
		</tr>   
		<tr>
			<td>-Turn on Kitchen light : KitchenLightOpen</td>
		</tr>   
		<tr>
			<td>-Turn on Living room light : SalaLightOpen</td>
		</tr>   
		<tr>
			<td>-Turn on Bedroom light: BedroomLightOpen</td>
		</tr>          
		<tr>
			<td>-Turn on Bath light : BathroomLightOpen</td>
		</tr> 
		<tr>
			<td>-Turn on SC light : SCLightOpen</td>
		</tr>  
		<tr>
			<td>-Turn on RV light : RVLightOpen</td>
		</tr> 
		<tr>
            <td>-Close main door : doorHomeClose</td>
		</tr>	
            <td>-Close Livingroom door : doorSalonClose</td>
		</tr>
		<tr>
		    <td>-Close bathroom door : doorBathClose</td>
		</tr>
		<tr>
			<td>-Close kitchen door : doorKitchenClose<td>
		</tr>
		<tr>
		    <td>-Close SC door : doorSCClose</td>
		</tr>
		<tr>
		    <td>-Turn Down bedroom blind : RollupBedClose</td>
		</tr>    
		<tr>
		    <td>-Turn Down kitchen blind : RollupKitClose</td>
		</tr>   
		<tr>
			<td>-Turn Down Living room blind : RollupSalClose</td>
		</tr>   
		<tr>
			<td>-Turn Down SC blind : RollupSCClose</td>
		</tr>   
		<tr>
			<td>-Turn off Kitchen light : KitchenLightClose</td>
		</tr>   
		<tr>
			<td>-Turn off Living room light : SalaLightClose</td>
		</tr>   
		<tr>
			<td>-Turn off Bedroom light: BedroomLightClose</td>
		</tr>          
		<tr>
			<td>-Turn off Bath light : BathroomLightClose</td>
		</tr> 
		<tr>
			<td>-Turn off SC light : SCLightClose</td>
		</tr> 
		<tr>
			<td>-Turn off RV light : RVLightClose</td>
		</tr> 
      </tr>
    </table>
</body>
</html>

"""



class ExampleRequestHandler(vizhtml.PageRequestHandler):



    def handle_request(self,request):

        """@args vizhtml.VizardHTTPRequestHandler()"""

        print "handle_request task command" , request.command       

        if request.command=="GET": 

            print "handle_request query string:" , request.query_string

            print "handle request resource path: ", request.resource_path 

            query = request.query_string
            
            if(len(request.query_string)!=0 and request.command!="POST"):

				print 'dentroooo :', request.command

				try:

					if query is not None: 

						query_components = dict(qc.split("=") for qc in query.split("&"))

						print "query string data:" , query_components
						
					#Posibles estados:
						if(query_components['device']=='doorHome' and query_components['state']=='open'):
							doorHomeOpen()
						if(query_components['device']=='doorHome' and query_components['state']=='close'):
							doorHomeClose()	
						if(query_components['device']=='doorSalon' and query_components['state']=='open'):
							doorSalonOpen()	
						if(query_components['device']=='doorSalon' and query_components['state']=='close'):
							doorSalonClose()
						if(query_components['device']=='doorBath' and query_components['state']=='open'):
							doorbathOpen()	
						if(query_components['device']=='doorBath' and query_components['state']=='close'):
							doorbathClose()	
						if(query_components['device']=='doorKitchen' and query_components['state']=='open'):
							doorKitchenOpen()		
						if(query_components['device']=='doorKitchen' and query_components['state']=='close'):
							doorKitchenClose()		
						if(query_components['device']=='doorSC' and query_components['state']=='open'):
							doorSCOpen()	
						if(query_components['device']=='doorSC' and query_components['state']=='close'):
							doorSCClose()	
						if(query_components['device']=='RollupBed' and query_components['state']=='open'):
							RollupBedOpen()	
						if(query_components['device']=='RollupBed' and query_components['state']=='close'):
							RollupBedClose()
						if(query_components['device']=='RollupKit' and query_components['state']=='open'):
							RollupKitOpen()	
						if(query_components['device']=='RollupKit' and query_components['state']=='close'):
							RollupKitClose()
						if(query_components['device']=='RollupSal' and query_components['state']=='open'):
							RollupKitOpen()	
						if(query_components['device']=='RollupSal' and query_components['state']=='close'):
							RollupSalClose()	
						if(query_components['device']=='RollupSC' and query_components['state']=='open'):
							RollupSCOpen()	
						if(query_components['device']=='KitchenLight' and query_components['state']=='open'):
							Kitchen_lightONOFFOpen()	
						if(query_components['device']=='KitchenLight' and query_components['state']=='close'):
							Kitchen_lightONOFFClose()	
						if(query_components['device']=='SalaLight' and query_components['state']=='open'):
							Sala_lightONOFFOpen()	
						if(query_components['device']=='SalaLight' and query_components['state']=='close'):
							Sala_lightONOFFClose()	
						if(query_components['device']=='BedroomLight' and query_components['state']=='open'):
							Bedroom_lightONOFFOpen()	
						if(query_components['device']=='BedroomLight' and query_components['state']=='close'):
							Bedroom_lightONOFFClose()
						if(query_components['device']=='BathroomLight' and query_components['state']=='open'):
							Bathroom_lightONOFFOpen()	
						if(query_components['device']=='BathroomLight' and query_components['state']=='close'):
							Bathroom_lightONOFFClose()	
						if(query_components['device']=='SCLight' and query_components['state']=='open'):
							SC_lightONOFFOpen()	
						if(query_components['device']=='SCLight' and query_components['state']=='close'):
							SC_lightONOFFClose()
						if(query_components['device']=='RVLight' and query_components['state']=='open'):
							RV_lightONOFFOpen()
						if(query_components['device']=='RVLight' and query_components['state']=='close'):
							RV_lightONOFFClose()	
						

				except ValueError:

					print "Oops!  That was an error on the query string.  Try again..."

				path = request.resource_path 

				try:

					if path is not None: 

						path_components = path.split("/") 

						print "path string array:" , path_components

				except ValueError:

					print "Oops!  That was an error on the path string.  Try again..."

        if request.command=="POST":    
            
            print 'SE HA METIDO EN POST'


        # If form was submitted, put message back into page
            if request.form_event:
             message = cgi.escape(request.form_event.message,True)
            if message == 'doorBathOpen':
             doorbathOpen()
            if message == 'doorHomeOpen':
             doorHomeOpen()
            if message == 'doorKitchenOpen':
               
             doorKitchenOpen()
            if message == 'doorSalonOpen':
             
             doorSalonOpen()
            if message == 'doorSCOpen':
              
             doorSCOpen()                
            if message == 'RollupBedOpen':
           
             RollupBedOpen()
            if message == 'RollupSalOpen':
              
             RollupSalOpen()
            if message == 'RollupKitOpen':  
           
             RollupKitOpen()
            if message == 'RollupSCOpen': 
             
             RollupSCOpen()
            if message == 'KitchenLightOpen': 
           
             Kitchen_lightONOFFOpen()
            if message == 'SalaLightOpen':
              
             Sala_lightONOFFOpen()
            if message == 'BedroomLightOpen':
           
             Bedroom_lightONOFFOpen()
            if message == 'BathroomLightOpen':
          
             Bathroom_lightONOFFOpen()
            if message == 'SCLightOpen':
            
             SC_lightONOFFOpen()
           
            if message == 'RVLightOpen':
            
             RV_lightONOFFOpen()
            if message == 'doorBathClose':
            
             doorbathClose()
            if message == 'doorHomeClose':
           
             doorHomeClose()
            if message == 'doorKitchenClose':
             
             doorKitchenClose()
            if message == 'doorSalonClose':
          
             doorSalonClose()
            if message == 'doorSCClose':
           
             doorSCClose()                
            if message == 'RollupBedClose':
           
             RollupBedClose()
            if message == 'RollupSalClose':
         
             RollupSalClose()
            if message == 'RollupKitClose':  
             
             RollupKitClose()
            if message == 'RollupSCClose': 
        
             RollupSCClose()
            if message == 'KitchenLightClose': 
               
             Kitchen_lightONOFFClose()
            if message == 'SalaLightClose':
              
             Sala_lightONOFFClose()
            if message == 'BedroomLightClose':
            
             Bedroom_lightONOFFClose()
            if message == 'BathroomLightClose':
       
             Bathroom_lightONOFFClose()
            if message == 'SCLightClose':
            
             SC_lightONOFFClose()
          
            if message == 'RVLightClose':
            
             RV_lightONOFFClose()

          

            

        # If request is for a resource (e.g. image), then let vizhtml handle it

        #if request.resource_path:

            #print "Request is for a resource (e.g. image), then let vizhtml handle it",request.resource_path

            #return



        # If form was submitted, put message back into page

        if request.form_event:

            message = cgi.escape(request.form_event.message,True)

        else:

            message = ''

			

        # Send html code with dynamic content

        request.send_html_code(code.format(frame=viz.getFrameNumber(),message=message))





vizhtml.registerHandlerClass('custom_handler',ExampleRequestHandler,directory='a/b/c')



def HandleForm(e):

    info.setText(e.message)

vizhtml.onFormSubmit(HandleForm)