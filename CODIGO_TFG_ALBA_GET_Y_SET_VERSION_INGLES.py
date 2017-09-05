import viz
import viznet
import vizinfo
import vizhtml
viz.setMultiSample(4)
viz.go()
import vizcam
import vizact
import viztracker 
import hand
import vizproximity
import vizshape
import viztask
import cgi
import socket
import vizpopup
viz.cam.setHandler(vizcam.KeyboardCamera())
viz.phys.enable()
viz.collision(viz.OFF)




########################CODIGO NORMAL #################################################################


#BOX TO SHOW IP DIRECTION

IP = ''
IP_Antigua = ''

checkbox = viz.addCheckbox(pos=(0.75,0.96,1)) 
checkbox.color(viz.WHITE)
checkbox.color(viz.PURPLE,viz.TEXTBOX_BORDER) 
checkbox.setScale(0.9,0.8,1)
example = viz.addTextbox()
example.visible(viz.OFF)
example.setPosition([0.865,0.9,1])
example.setScale([1.1,1,1])
example.color(viz.BLACK,viz.TEXTBOX_TEXT)
example.color(viz.PURPLE,viz.TEXTBOX_BORDER) 
example.color(viz.WHITE,viz.TEXTBOX_BACK) 

def onButton(obj,state): 
    if obj == checkbox: 
        if state == viz.DOWN: 
            example.visible(viz.ON)
        else: 
            example.visible(viz.OFF)

viz.callback(viz.BUTTON_EVENT,onButton)

def Nueva():
	global IP_Antigua
	global IP
	IP = socket.gethostbyname_ex(socket.gethostname())
	if (IP_Antigua!=IP[2][1]):
		example.message("Dir IP :"+IP[2][1])
		IP_Antigua = IP[2][1]

vizact.ontimer2(5,99999999999999999999999999999999999999999999999999999999999999,Nueva)

viz.res.addPublishFile('resource.dat')

viz.MainView.setPosition([12.967599868774414, 1.7999999523162842, 2.2560689449310303])
viz.MainView.setEuler([-91.71162414550781, 0.0, 0.0])

viz.MainView.getHeadLight().intensity(0.5) #To make it look dark while the lights and blinds are not on

label = viz.addText('Click to show IP Direction',parent=viz.SCREEN,pos=[0.77,0.947,0],scale=[0.25,0.4,1], color = viz.WHITE)
label1 = viz.addText('LifeSTech',parent=viz.SCREEN,pos=[0.8,0.05,0],scale=[0.5,0.5,1], color = viz.PURPLE)
alojeno = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')
alojeno2 = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')
alojeno3 = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')
alojeno4 = viz.add('Led/AM152_063_Lugstar_Premium_LED.obj')

alojeno2.setScale(0.05,0.05,0.05)
alojeno3.setScale(0.05,0.05,0.05)
alojeno4.setScale(0.05,0.05,0.05)

alojeno.setPosition(1,3.5,6,viz.ABS_GLOBAL)
alojeno4.setPosition(-6.660562515258789, 3.5, 8.53273868560791)
alojeno3.setPosition(1,3.5,6,viz.ABS_GLOBAL)
alojeno.setPosition(5,0,3,viz.REL_GLOBAL)
alojeno.setScale(0.05,0.05,0.05)
eule2 = [0,0,90]

#code for smart box
CAJA = viz.add('Caja_final_cerrada.obj')
CAJA.setScale(0.003,0.003,0.003)
CAJA.setPosition(3,0.5,9,viz.ABS_GLOBAL)
CAJA.setEuler([0,90,0],viz.ABS_GLOBAL)


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
#End code for smart box



ground = viz.add('tut_ground.wrl') #ground
ground.disable(viz.INTERSECTION)
viz.clearcolor([.5, .6, 1])

lab = viz.add('Living_Lab_Blinds_V2.OSGB')
lab.setScale(0.006,0.006,0.006)
lab.setPosition ([0,0.58,5])
cabinavater = lab.getChild('Toilet_Tank-GEODE')
print cabinavater.getPosition(viz.ABS_GLOBAL)
alojeno2.setPosition(-2.8618810176849365, 3.5, 6,viz.ABS_GLOBAL)



#INITIALIZATION OF VARIABLES
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
state_BedroomLight = 0  
state_BedroomLight_quiero = 1
state_BathroomLight = 0 
state_BathroomLight_quiero = 1
state_SCLight = 0 
state_SCLight_quiero = 1
state_SalaLight = 0 
state_SalaLight_quiero = 1
state_RVLight = 0 
state_RVLight_quiero = 1
state_SV = 0 # To know if it is inside or outside the house, 0 is that it is inside
state_CajaModo1 = 0
state_CajaModo1_quiero = 1
state_CajaModo2 = 0
state_CajaModo2_quiero = 1
status = "failure"
Fuera = 1 #Variable used to know whether it is inside or outside the house for the view to open and close
code_ = "404"

#Inicialization info text
texto = viz.addText('',parent=viz.SCREEN, pos=[0.005,0.927,0], scale=[0.5,0.5,1], color = viz.PURPLE)



#-------------------------------OPENING AND CLOSING DOORS-------------------------------------------------------

#OPENING AND CLOSING CONTROL ROOM DOOR 

DoorSC_GEODE = lab.getChild('Door sala control').getChild ('Box010')
Chapa = lab.getChild ('Chapa')
Cilindro = lab.getChild('Cylinder001')
link_DoorSC = viz.link(DoorSC_GEODE, Chapa)
link2_DoorSC = viz.link(DoorSC_GEODE, Cilindro)


#def doorSCOpen(e): #SALA RV
def doorSCOpen():	
	print 'estoy en doorSCOpen'
	def doorSCOpen_bis():
		global state_doorSC
		global state_doorSC_quiero
		global state_SV
		state_doorSC_quiero = 1
		if state_doorSC == 0 and state_doorSC_quiero == 1 : #Open
			eule = [90,0,0]
			DoorSC_GEODE.setEuler(eule, viz.REL_LOCAL)
			state_doorSC = 1
			
	if(state_SV==0):
		Casa_SC()
		viz.waitTime(2)
		doorSCOpen_bis()
		
	else:
		
		viz.MainView.addAction(vizact.spinTo(euler=[-68.700439453125, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-3.5732383728027344, 2.407294273376465, -1.3862537145614624],speed=12))
		viz.waitTime(2)
		doorSCOpen_bis()


#def doorSCClose(e): #SALA RV
def doorSCClose():	
	
	print 'estoy en doorSCClose'

	def doorSCClose_bis():
		global state_doorSC
		global state_doorSC_quiero
		global state_SV 
		state_doorSC_quiero = 0
		if state_doorSC == 1 and state_doorSC_quiero == 0 : #Close
			eule2 = [-90,0,0]
			DoorSC_GEODE.setEuler(eule2, viz.REL_LOCAL)
			state_doorSC = 0
	if(state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[-68.700439453125, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-3.5732383728027344, 2.407294273376465, -1.3862537145614624],speed=12))
		viz.waitTime(2)
		doorSCClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-68.700439453125, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-3.5732383728027344, 2.407294273376465, -1.3862537145614624],speed=12))
		viz.waitTime(2)
		doorSCClose_bis()
		
		



##OPENING AND CLOSING MAIN DOOR

DoorHome_GEODE = lab.getChild('Door Principal').getChild ('Box101-OFFSET')
Cham = lab.getChild ('ChamferBox002')
Cylinder = lab.getChild('Cylinder002')
Handle = lab.getChild('Door_Handle001')
Handle_base = lab.getChild('Door_handle_Base001')
Rectangle = lab.getChild('Rectangle014')



#def doorHome(e): 
def doorHomeOpen():
	
	global Fuera
	print 'POSICION :',viz.MainView.getPosition(viz.ABS_GLOBAL)
	print 'EULER :', viz.MainView.getEuler(viz.ABS_GLOBAL)
	def doorHomeOpen_bis():

		print 'estoy en doorHomeOpen'
		global state_doorHome
		global state_doorHome_quiero
		global state_SV 
		state_doorHome_quiero = 1
		if ((state_doorHome == 0) and (state_doorHome_quiero == 1)) : #OPEN

			eule = [0,0,90]
			DoorHome_GEODE.setEuler(eule, viz.REL_LOCAL)
			Handle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
			Handle.setEuler (0,0,90,viz.ABS_GLOBAL)
			Handle_base.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
			Cham.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
			Rectangle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
			state_doorHome = 1
			
	if(state_SV==1):   #When you want to open being in Virtual Room
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[88.15464782714844, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.7735934257507324, 2.407294273376465, 2.2873051166534424],speed=5))
		viz.waitTime(2)
		doorHomeOpen_bis()
		
	if(state_SV==0 and Fuera==0): #When you want to open being inside home  
		viz.MainView.addAction(vizact.spinTo(euler=[88.15464782714844, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.7735934257507324, 2.407294273376465, 2.2873051166534424],speed=5))	
		viz.waitTime(1)
		doorHomeOpen_bis()	
		
	if(state_SV==0 and Fuera==1): #When you want to open being out home
		Fuera=0; 
		doorHomeOpen_bis()
		viz.waitTime(1)
		viz.MainView.addAction(vizact.spinTo(euler=[-91.71162414550781, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([4.85840368270874, 1.7999999523162842, 2.013747215270996],speed=5))	

#def doorHomeClose(e): 
def doorHomeClose():
	

	print 'estoy en doorHome'	
	global Fuera
	def doorHomeClose_bis():
		global state_doorHome
		global state_doorHome_quiero
		global state_SV 
		state_doorHome_quiero = 0
		if ((state_doorHome == 1) and (state_doorHome_quiero == 0)) : #CLOSE
			eule2 = [0,0,-90]
			DoorHome_GEODE.setEuler(eule2, viz.REL_LOCAL)
			Handle.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
			Handle.setEuler (0,0,-90,viz.REL_LOCAL)
			Handle_base.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
			Cham.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
			Rectangle.setPosition(8.701148986816406, 1.8045035600662231, 2.7014875411987305,viz.ABS_GLOBAL)
			state_doorHome = 0
	if(state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[88.15464782714844, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.7735934257507324, 2.407294273376465, 2.2873051166534424],speed=5))
		viz.waitTime(2)
		doorHomeClose_bis()
		
	if(state_SV==0 and Fuera==0):
		viz.MainView.addAction(vizact.spinTo(euler=[88.15464782714844, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.7735934257507324, 2.407294273376465, 2.2873051166534424],speed=5))
		viz.waitTime(2)
		doorHomeClose_bis()
		
	if(state_SV and Fuera==1):
		doorHomeClose_bis()
		viz.waitTime(1)
		viz.MainView.addAction(vizact.spinTo(euler=[-91.71162414550781, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([4.85840368270874, 1.7999999523162842, 2.013747215270996],speed=5))
		
		



#OPENING AND CLOSING BATHROOM DOOR
Doorbath_GEODE = lab.getChild('Toilet_Door-GEODE')
Circle_GEODE = lab.getChild('Circle002-GEODE')

#def doorbathOpen(e): #SALA RV
def doorbathOpen():
		
	print 'estoy en doorbathOpen'


	def doorbathOpen_bis():
		global state_doorbath
		global state_doorbath_quiero
		global state_SV 
		state_doorbath_quiero = 1
		if state_doorbath == 0 and state_doorbath_quiero == 1: #OPEN
			dpos = Doorbath_GEODE.getPosition(viz.ABS_GLOBAL)
			new_dpos = [dpos[0], dpos[1], dpos[2] - 0.8]
			Doorbath_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
			cpos = Circle_GEODE.getPosition(viz.ABS_GLOBAL)
			new_cpos = [cpos[0], cpos[1], cpos[2] - 0.75]
			Circle_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
			state_doorbath = 1
	
	if(state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-93.51321411132812, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.714972734451294, 2.407294273376465, 7.522972106933594],speed=5))
		viz.waitTime(2)
		doorbathOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-93.51321411132812, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.714972734451294, 2.407294273376465, 7.522972106933594],speed=5))
		viz.waitTime(2)
		doorbathOpen_bis()
	
doorSuich_bath = lab.getChild('Light_Switch out  bathroom')
node = viz.addChild('plant.osgb',pos=(0,0.58,5))


#def doorbathClose(e): #SALA RV
def doorbathClose():
	
	print 'estoy en doorbath'
	
	def doorbathClose_bis():
		global state_doorbath
		global state_doorbath_quiero 
		global state_SV 
		state_doorbath_quiero = 0
		if state_doorbath == 1 and state_doorbath_quiero == 0: #CLOSE
			dpos = Doorbath_GEODE.getPosition(viz.ABS_GLOBAL)
			new_dpos = [dpos[0], dpos[1], dpos[2] + 0.8]
			Doorbath_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
			cpos = Circle_GEODE.getPosition(viz.ABS_GLOBAL)
			new_cpos = [cpos[0], cpos[1], cpos[2] + 0.75]
			Circle_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
			state_doorbath = 0
	if(state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-93.51321411132812, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.714972734451294, 2.407294273376465, 7.522972106933594],speed=5))
		viz.waitTime(2)
		doorbathClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-93.51321411132812, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.714972734451294, 2.407294273376465, 7.522972106933594],speed=5))
		viz.waitTime(2)
		doorbathClose_bis()
	
doorSuich_bath = lab.getChild('Light_Switch out  bathroom')
node = viz.addChild('plant.osgb',pos=(0,0.58,5))


#OPENING AND CLOSING LIVINGROOM AND KITCHEN DOORS
DoorKitchen_GEODE = lab.getChild('Glass002-GEODE')
DoorKit_frame_GEODE = lab.getChild('Door_Frame001-GEODE')

DoorSalon_GEODE = lab.getChild('Glass004-GEODE')
DoorSal_frame_GEODE = lab.getChild('Door_Frame003-GEODE')

#def doorKitchenOpen (e): #SALA RV
def doorKitchenOpen ():
	global state_SV 
	
	def openDoorKitchen ():
	
		dpos = DoorKitchen_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] + 0.6, dpos[1], dpos[2]]
		DoorKitchen_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorKit_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] + 0.6, cpos[1], cpos[2]]
		DoorKit_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	
	
	def doorKitchenOpen_bis():
		global state_doorkit
		global state_doorkit_quiero
		state_doorkit_quiero = 1
		if state_doorkit == 0 and state_doorkit_quiero == 1: #OPEN
			vizact.ontimer2(1,2,openDoorKitchen)
			state_doorkit = 1
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		doorKitchenOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		doorKitchenOpen_bis()
		
#def doorKitchenClose (e): #SALA RV
def doorKitchenClose ():
	
	def closeDoorKitchen ():
		
		dpos = DoorKitchen_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] - 0.6, dpos[1], dpos[2]]
		DoorKitchen_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorKit_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] - 0.6, cpos[1], cpos[2]]
		DoorKit_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	
	def doorKitchenClose_bis():
		global state_SV 
		global state_doorkit
		global state_doorkit_quiero
	
		state_doorkit_quiero = 0
		
		if state_doorkit == 1 and state_doorkit_quiero == 0: #CLOSE
			vizact.ontimer2(1,2,closeDoorKitchen)
			state_doorkit = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		doorKitchenClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		doorKitchenClose_bis()		



#def doorSalonOpen (e)
def doorSalonOpen ():
	
	
	def openDoorSalon ():
		

		dpos = DoorSalon_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] + 0.6, dpos[1], dpos[2]]
		DoorSalon_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorSal_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] + 0.6, cpos[1], cpos[2]]
		DoorSal_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	
	def doorSalonOpen_bis():
		global state_SV 
		global state_doorsal
		global state_doorsal_quiero
		state_doorsal_quiero = 1
		if state_doorsal == 0 and state_doorsal_quiero == 1: #OPEN
			vizact.ontimer2(1,2,openDoorSalon)
			state_doorsal = 1	
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		doorSalonOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		doorSalonOpen_bis()	

doorSuich_kitchen = lab.getChild('Light_Switch Kitchen')
doorSuich_salon = lab.getChild('Light_Switch salon')



#def doorSalonClose (e): 
def doorSalonClose ():
	
	def closeDoorSalon ():
		
		
		dpos = DoorSalon_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0] - 0.6, dpos[1], dpos[2]]
		DoorSalon_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		cpos = DoorSal_frame_GEODE.getPosition(viz.ABS_GLOBAL)
		new_cpos = [cpos[0] - 0.6, cpos[1], cpos[2]]
		DoorSal_frame_GEODE.setPosition(new_cpos, viz.ABS_GLOBAL)
	
	
	
	def doorSalonClose_bis():
		global state_SV
		global state_doorsal
		global state_doorsal_quiero
		state_doorsal_quiero = 0
		if state_doorsal == 1 and state_doorsal_quiero == 0: #CLOSE
			vizact.ontimer2(1, 2, closeDoorSalon)
			state_doorsal = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		doorSalonClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		doorSalonClose_bis()	
doorSuich_kitchen = lab.getChild('Light_Switch Kitchen')
doorSuich_salon = lab.getChild('Light_Switch salon')






#--------------------------------------OPENING AND CLOSING BLINDS-------------------------------------------------------
#LUZ AMBIENTE
luzAmbiente = viz.addLight()
luzAmbiente.disable()

#BEDROOM BLIND
Rollup_bed_GEODE = lab.getChild('Blind bedroom-GEODE')

#def RollupBedOpen (e): 
def RollupBedOpen ():
	

	
	print 'se mete en RollUpBedOpen'
	def open_bedblind(): #OPEN BLIND
		dpos = Rollup_bed_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]+ 0.5, dpos[2]]
		Rollup_bed_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		
		
	
	
	def open_bedblind_bis():
		global state_SV
		global state_rollupbed
		global state_rollupbed_quiero
		state_rollupbed_quiero = 1
		if state_rollupbed == 0 and state_rollupbed_quiero == 1: #OPEN
			vizact.ontimer2(1,6, open_bedblind)
			state_rollupbed = 1
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(2)
		open_bedblind_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(2)
		open_bedblind_bis()			
RollupSuich_bed = lab.getChild ('Light_Switch bedroom')



#def RollupBedClose (e): #SALA RV
def RollupBedClose ():
	
	def close_bedblind(): #CLOSE BLIND

		dpos = Rollup_bed_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]- 0.5, dpos[2]]
		Rollup_bed_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)

		
		
	def close_bedblind_bis():
		global state_SV
		global state_rollupbed
		global state_rollupbed_quiero
		state_rollupbed_quiero = 0
		
		if state_rollupbed == 1 and state_rollupbed_quiero == 0: #CLOSE
			vizact.ontimer2(1,6, close_bedblind)
			state_rollupbed = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(2)
		close_bedblind_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.00],speed=50))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(2)
		close_bedblind_bis()				
RollupSuich_bed = lab.getChild ('Light_Switch bedroom')



#LIVINGROOM BLIND
Rollup_sal1_GEODE = lab.getChild('Roll up door 3-GEODE')
Rollup_sal2_GEODE = lab.getChild('Roll up door 4-GEODE')



#def RollupSalOpen (e): 
def RollupSalOpen ():
	


	def open_Salblind(): #OPEN BLIND
		
		
		print 'se mete en RollUpSalonOpen'
		
		
		dpos1 = Rollup_sal1_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]+ 0.5, dpos1[2]]
		Rollup_sal1_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_sal2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]+ 0.5, dpos2[2]]
		Rollup_sal2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
	
	
	
	
	
	def open_Salblind_bis():
		global state_SV 
		global state_rollupsal
		global state_rollupsal_quiero
		state_rollupsal_quiero = 1
		if state_rollupsal == 0 and state_rollupsal_quiero == 1: #OPEN
			print 'se mete en ABRIR Salon'
			vizact.ontimer2(1,4, open_Salblind)
			state_rollupsal = 1
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		open_Salblind_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		open_Salblind_bis()
#def RollupSalClose (e): #SALA RV
def RollupSalClose ():
	

	def close_Salblind(): #CLOSE BLIND
	
		dpos1 = Rollup_sal1_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]- 0.5, dpos1[2]]
		Rollup_sal1_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_sal2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]- 0.5, dpos2[2]]
		Rollup_sal2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		
	
	
	 
	
	
	def close_Salblind_bis():
		global state_SV
		global state_rollupsal
		global state_rollupsal_quiero
		state_rollupsal_quiero = 0
		if state_rollupsal == 1 and state_rollupsal_quiero == 0 : #CLOSE
			vizact.ontimer2(1,4, close_Salblind)
			state_rollupsal = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		close_Salblind_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[168.10745239257812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([4.092425346374512, 2.407294273376465, 4.741787910461426],speed=5))
		viz.waitTime(2)
		close_Salblind_bis()

#KITCHEN BLIND
Rollup_kit_GEODE = lab.getChild('Roll up door 1-GEODE')
Rollup_kit2_GEODE = lab.getChild('Roll up door 2-GEODE')


#def RollupKitOpen (e): #SALA RV
def RollupKitOpen ():
	
	def open_Kitblind(): #OPEN BLIND
			
		dpos1 = Rollup_kit_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]+ 0.5, dpos1[2]]
		Rollup_kit_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_kit2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]+ 0.5, dpos2[2]]
		Rollup_kit2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		
	
	
	def RollupKitOpen():
		global state_SV
		global state_rollupkit
		global state_rollupkit_quiero
		state_rollupkit_quiero = 1
		if state_rollupkit == 0 and state_rollupkit_quiero == 1: #OPEN
			vizact.ontimer2(1,4, open_Kitblind)
			state_rollupkit = 1
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		RollupKitOpen()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		RollupKitOpen()

#def RollupKitClose (e): #SALA RV
def RollupKitClose ():
	
	
	def close_Kitblind(): #CLOSE BLIND
		
		dpos1 = Rollup_kit_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos1 = [dpos1[0], dpos1[1]- 0.5, dpos1[2]]
		Rollup_kit_GEODE.setPosition(new_dpos1, viz.ABS_GLOBAL)
		dpos2 = Rollup_kit2_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos2 = [dpos2[0], dpos2[1]- 0.5, dpos2[2]]
		Rollup_kit2_GEODE.setPosition(new_dpos2, viz.ABS_GLOBAL)
		
	
	
	
	def RollupKitClose_bis():
		global state_SV
		global state_rollupkit
		global state_rollupkit_quiero
		state_rollupkit_quiero = 0
		if state_rollupkit == 1 and state_rollupkit_quiero == 0: #CLOSE
			vizact.ontimer2(1,4, close_Kitblind)
			state_rollupkit = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		RollupKitClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-171.30130004882812, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([0.8414586186408997, 2.407294273376465, 5.400276184082031],speed=5))
		viz.waitTime(2)
		RollupKitClose_bis()


#CONTROL ROOM BLIND
Rollup_SC_GEODE = lab.getChild('roll up-GEODE')


#def rollupscOpen(e): #SALA RV
def RollupSCOpen ():
	
	def open_SCblind(): #OPEN BLIND
		
		
		dpos = Rollup_SC_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]+ 0.5, dpos[2]]
		Rollup_SC_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
		
	
	
	def RollupSCOpen_bis():
		global state_SV
		global state_rollupsc
		global state_rollupsc_quiero
		state_rollupsc_quiero = 1
		if state_rollupsc == 0 and state_rollupsc_quiero == 1: #OPEN
			vizact.ontimer2(1,3, open_SCblind)
			state_rollupsc = 1
	if (state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[-74.78972625732422, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([-4.8969316482543945, 2.407294273376465, 3.1122682094573975],speed=5))
		viz.waitTime(2)
		RollupSCOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-74.78972625732422, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([-4.8969316482543945, 2.407294273376465, 3.1122682094573975],speed=5))
		viz.waitTime(2)
		RollupSCOpen_bis()

#def rollupscClose(e): #SALA RV
def RollupSCClose ():
	

	
	def close_SCblind(): #CLOSE BLIND
		
		dpos = Rollup_SC_GEODE.getPosition(viz.ABS_GLOBAL)
		new_dpos = [dpos[0], dpos[1]- 0.5, dpos[2]]
		Rollup_SC_GEODE.setPosition(new_dpos, viz.ABS_GLOBAL)
	
	
	print 'estoy en rollupsc'
	
	def RollupSCClose_bis():
		global state_SV
		global state_rollupsc
		global state_rollupsc_quiero
		state_rollupsc_quiero = 0
		if state_rollupsc == 1 and state_rollupsc_quiero == 0: #CLOSE
			vizact.ontimer2(1,3, close_SCblind)
			state_rollupsc = 0
	if (state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[-74.78972625732422, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([-4.8969316482543945, 2.407294273376465, 3.1122682094573975],speed=5))
		viz.waitTime(2)
		RollupSCClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-74.78972625732422, 0.0, 0.0],speed=50))
		viz.MainView.addAction(vizact.moveTo([-4.8969316482543945, 2.407294273376465, 3.1122682094573975],speed=5))
		viz.waitTime(2)
		RollupSCClose_bis()		

#-------------------------TURN ON AND TURN OFF LIGHTS-----------------------------------------------------------------

#KITCHEN LIGHT
luzcocina = lab.getChild('Extractor-GEODE')
lightKitSwitch = lab.getChild('Box132-GEODE')

#We add a light source to the lamp.
Kitchen_light = viz.addLight()
#We defined the light of the lamp as a point light,
#This is done by placing the last 1 in the following command.
Kitchen_light.position( 0,0,0,1 )
Kitchen_light.direction(0,1,0)
Kitchen_light.spread(90)
Kitchen_light.disable()

#We make a link between the lamp and the light source.
viz.link( luzcocina, Kitchen_light )

#def Kitchen_lightONOFFOpen (e): #SALA RV
def Kitchen_lightONOFFOpen ():
	
	
	def Kitchen_lightONOFFOpen_bis():
		global state_SV
		global state_KitLight
		global state_KitLight_quiero
		state_KitLight_quiero = 1
		if state_KitLight == 0 and state_KitLight_quiero == 1: #TURN ON
			state_KitLight = 1
			Kitchen_light.color(viz.YELLOW)
			Kitchen_light.intensity(8)
			Kitchen_light.quadraticAttenuation(1)
			Kitchen_light.enable()
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-109.53791809082031, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.603083610534668, 2.407294273376465, 4.1396026611328125],speed=5))
		viz.waitTime(3)
		Kitchen_lightONOFFOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-109.53791809082031, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.603083610534668, 2.407294273376465, 4.1396026611328125],speed=5))
		viz.waitTime(3)
		Kitchen_lightONOFFOpen_bis()				


#def Kitchen_lightONOFFClose (e): #SALA RV
def Kitchen_lightONOFFClose ():
	
	
	def Kitchen_lightONOFFClose_bis():
		global state_SV
		global state_KitLight
		global state_KitLight_quiero
		state_KitLight_quiero = 0
		if state_KitLight == 1 and state_KitLight_quiero == 0: #TURN OFF
			Kitchen_light.disable()
			state_KitLight = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-109.53791809082031, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.603083610534668, 2.407294273376465, 4.1396026611328125],speed=5))
		viz.waitTime(3)
		Kitchen_lightONOFFClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-109.53791809082031, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([3.603083610534668, 2.407294273376465, 4.1396026611328125],speed=5))
		viz.waitTime(3)
		Kitchen_lightONOFFClose_bis()			






##LIVING ROOM LIGHT
#
luzsala = alojeno3
lightSalaSwitch = lab.getChild('Light_Switch TV')


#We add a light source to the lamp.
Sala_light = viz.addLight()
# We set the lamp light as a point light,
#This is done by placing the last 1 in the next command.
Sala_light.position( 0,0,0,1 )
Sala_light.direction(0,1,0)
Sala_light.spread(90)
Sala_light.disable()

#We make a link between the lamp and the light source.
viz.link( luzsala	, Sala_light )

#def Sala_lightONOFFOpen (e): #SALA RV
def Sala_lightONOFFOpen ():
	
	
	
	def Sala_lightONOFFOpen_bis():
		global state_SV
		global state_SalaLight
		global state_SalaLight_quiero
		state_SalaLight_quiero = 1
		if state_SalaLight == 0 and state_SalaLight_quiero == 1 : #TURN ON
			state_SalaLight = 1
			Sala_light.color(viz.YELLOW)
			Sala_light.intensity(8)
			Sala_light.quadraticAttenuation(1)
			Sala_light.enable()
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-66.82832336425781, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([6.390945911407471, 2.407294273376465, 4.5051164627075195],speed=5))
		viz.waitTime(3)
		Sala_lightONOFFOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-66.82832336425781, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([6.390945911407471, 2.407294273376465, 4.5051164627075195],speed=5))
		viz.waitTime(3)
		Sala_lightONOFFOpen_bis()
			
#def Sala_lightONOFFClose (e): #SALA RV
def Sala_lightONOFFClose ():
	
	print 'estoy en Sala_lightONOFF'
	def Sala_lightONOFFClose_bis():
		global state_SV
		global state_SalaLight
		global state_SalaLight_quiero
		state_SalaLight_quiero = 0
		if state_SalaLight == 1 and state_SalaLight_quiero == 0 : #TURN OFF
			Sala_light.disable()
			state_SalaLight = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-66.82832336425781, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([6.390945911407471, 2.407294273376465, 4.5051164627075195],speed=5))
		viz.waitTime(3)
		Sala_lightONOFFClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-66.82832336425781, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([6.390945911407471, 2.407294273376465, 4.5051164627075195],speed=5))
		viz.waitTime(3)
		Sala_lightONOFFClose_bis()


#LUZ HABITACIÓN

luzhabitacion = alojeno
lightBedroomSwitch = lab.getChild('Light_Switch cama')

#We add a light source to the lamp.
Bedroom_light = viz.addLight()
# We set the lamp light as a point light,
#This is done by placing the last 1 in the next command.
Bedroom_light.position( 0,0,0,1 )
Bedroom_light.direction(0,1,0)
Bedroom_light.spread(90)
Bedroom_light.disable()

#We make a link between the lamp and the light source
viz.link( luzhabitacion	, Bedroom_light )

#def Bedroom_lightONOFFOpen (e): #SALA RV
def Bedroom_lightONOFFOpen ():
	

	
	def Bedroom_lightONOFFOpen_bis():
		global state_SV
		global state_BedroomLight
		global state_BedroomLight_quiero
		state_BedroomLight_quiero = 1
		if state_BedroomLight == 0 and state_BedroomLight_quiero == 1 : #TURN ON
			state_BedroomLight = 1
			Bedroom_light.color(viz.YELLOW)
			Bedroom_light.intensity(8)
			Bedroom_light.quadraticAttenuation(1)
			Bedroom_light.enable()
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(3)
		Bedroom_lightONOFFOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(3)
		Bedroom_lightONOFFOpen_bis()			
#def Bedroom_lightONOFFClose (e): #SALA RV
def Bedroom_lightONOFFClose ():
	
	def Bedroom_lightONOFFClose_bis():
		global state_SV
		global state_BedroomLight
		global state_BedroomLight_quiero
		state_BedroomLight_quiero = 0 
		if state_BedroomLight == 1 and state_BedroomLight_quiero == 0 : #TURN OFF
			Bedroom_light.disable()
			state_BedroomLight = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(3)
		Bedroom_lightONOFFClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[60.40805435180664, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([2.807915687561035, 2.407294273376465, 6.183692455291748],speed=5))
		viz.waitTime(3)
		Bedroom_lightONOFFClose_bis()

#BATHROOM LIGHT



luzBathroom = alojeno2
lightBathroomSwitch = lab.getChild('Socket_single-GEODE')

#We add a light source to the lamp.
Bathroom_light = viz.addLight()
# We set the lamp light as a point light,
#This is done by placing the last 1 in the next command.
Bathroom_light.position( 0,0,0,1 )
Bathroom_light.direction(0,1,0)
Bathroom_light.spread(90)
Bathroom_light.disable()

#We make a link between the lamp and the light source.
viz.link( luzBathroom	, Bathroom_light )

#def Bathroom_lightONOFFOpen (e): #SALA RV
def Bathroom_lightONOFFOpen ():
	
	
	
	
	def Bathroom_lightONOFFOpen_bis():
		global state_SV
		global state_BathroomLight
		global state_BathroomLight_quiero
		state_BathroomLight_quiero = 1
		if state_BathroomLight == 0 and state_BathroomLight_quiero == 1: #TURN ON
			state_BathroomLight = 1
			Bathroom_light.color(viz.YELLOW)
			Bathroom_light.intensity(8)
			Bathroom_light.quadraticAttenuation(1)
			Bathroom_light.enable()
			
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-92.50753021240234, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-2.0080931186676025, 2.407294273376465, 7.663171291351318],speed=5))
		viz.waitTime(3)
		Bathroom_lightONOFFOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-92.50753021240234, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-2.0080931186676025, 2.407294273376465, 7.663171291351318],speed=5))
		viz.waitTime(3)
		Bathroom_lightONOFFOpen_bis()


#def Bathroom_lightONOFFClose (e): #SALA RV
def Bathroom_lightONOFFClose ():

	
	
	def Bathroom_lightONOFFClose_bis():
		global state_SV
		global state_BathroomLight
		global state_BathroomLight_quiero	
		state_BathroomLight_quiero = 0
		if state_BathroomLight == 1 and state_BathroomLight_quiero == 0: #TURN OFF
			Bathroom_light.disable()
			state_BathroomLight = 0
	if (state_SV==1):
		SC_Casa()
		viz.MainView.addAction(vizact.spinTo(euler=[-92.50753021240234, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-2.0080931186676025, 2.407294273376465, 7.663171291351318],speed=5))
		viz.waitTime(3)
		Bathroom_lightONOFFClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-92.50753021240234, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-2.0080931186676025, 2.407294273376465, 7.663171291351318],speed=5))
		viz.waitTime(3)
		Bathroom_lightONOFFClose_bis()			


#LUZ SC



luzSC = lab.getChild('Mirror_Frame-GEODE')
lightSCSwitch = lab.getChild('Socket005-GEODE')

#We add a light source to the lamp.
SC_light = viz.addLight()
# We set the lamp light as a point light,
#This is done by placing the last 1 in the next command.
SC_light.position( 0,0,0,1 )
SC_light.direction(0,1,0)
SC_light.spread(90)
SC_light.disable()

#We make a link between the lamp and the light source.
viz.link( luzSC	, SC_light )

#def SC_lightONOFFOpen (e): #SALA RV
def SC_lightONOFFOpen ():
	
	
	def SC_lightONOFFOpen_bis():
		global state_SV
		global state_SCLight
		global state_SCLight_quiero
		state_SCLight_quiero = 1
		if state_SCLight == 0 and state_SCLight_quiero == 1 : #TURN ON
			state_SCLight = 1
			SC_light.color(viz.YELLOW)
			SC_light.intensity(8)
			SC_light.quadraticAttenuation(1)
			SC_light.enable()
	if (state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[-19.274208068847656, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-5.601597309112549, 2.407294273376465, 1],speed=5))
		viz.waitTime(3)
		SC_lightONOFFOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-19.274208068847656, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-5.601597309112549, 2.407294273376465, 1],speed=5))
		viz.waitTime(3)
		SC_lightONOFFOpen_bis()		


#def SC_lightONOFF (e): #SALA RV
def SC_lightONOFFClose ():
	

	def SC_lightONOFFClose_bis():	
		global state_SV
		global state_SCLight
		global state_SCLight_quiero 
		state_SCLight_quiero = 0
		if state_SCLight == 1 and state_SCLight_quiero == 0 : #TURN OFF
			SC_light.disable()
			state_SCLight = 0
	if (state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[-19.274208068847656, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-5.601597309112549, 2.407294273376465, 1],speed=5))
		viz.waitTime(3)
		SC_lightONOFFClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[-19.274208068847656, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-5.601597309112549, 2.407294273376465, 1],speed=5))
		viz.waitTime(3)
		SC_lightONOFFClose_bis()			







#LUZ RV


luzRV = alojeno4

#We add a light source to the lamp.
RV_light = viz.addLight()
# We set the lamp light as a point light,
#This is done by placing the last 1 in the next command.

RV_light.position( 0,0,0,1 )
RV_light.direction(0,1,0)
RV_light.spread(90)
RV_light.disable()

#We make a link between the lamp and the light source.
viz.link( luzRV	, RV_light )

#def RV_lightONOFFOpen (e): #SALA RV
def RV_lightONOFFOpen ():
	
	

	def RV_lightONOFFOpen_bis():
		global state_SV
		global state_RVLight
		global state_RVLight_quiero
		state_RVLight_quiero = 1
		if state_RVLight == 0 and state_RVLight_quiero == 1: #TURN ON
			
			RV_light.color(viz.YELLOW)
			RV_light.intensity(8)
			RV_light.quadraticAttenuation(1)
			RV_light.enable()
			state_RVLight = 1	
	if (state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[30.27346420288086, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-8.30616283416748, 2.407294273376465, 4.816455841064453],speed=5))
		viz.waitTime(3)
		RV_lightONOFFOpen_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[30.27346420288086, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-8.30616283416748, 2.407294273376465, 4.816455841064453],speed=5))
		viz.waitTime(3)
		RV_lightONOFFOpen_bis()	

#def RV_lightONOFFClose (e): #SALA RV
def RV_lightONOFFClose ():
	
	
	
	def RV_lightONOFFClose_bis():
		global state_SV
		global state_RVLight
		global state_RVLight_quiero
		state_RVLight_quiero = 0
		if state_RVLight == 1 and state_RVLight_quiero == 0: #TURN OFF
			RV_light.disable()
			state_RVLight = 0
	if (state_SV==0):
		Casa_SC()
		viz.MainView.addAction(vizact.spinTo(euler=[30.27346420288086, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-8.30616283416748, 2.407294273376465, 4.816455841064453],speed=5))
		viz.waitTime(3)
		RV_lightONOFFClose_bis()
	else:
		viz.MainView.addAction(vizact.spinTo(euler=[30.27346420288086, 0.0, 0.0],speed=100))
		viz.MainView.addAction(vizact.moveTo([-8.30616283416748, 2.407294273376465, 4.816455841064453],speed=5))
		viz.waitTime(3)
		RV_lightONOFFClose_bis()			








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

#-----------------------------METHODS TO GO FROM HOME TO CONTROL ROOM AND FROM CONTROL ROOM TO HOME -----------------------------------
def Casa_SC():
	
	global state_SV
	global state_doorSC
	global state_doorSC_quiero
	global state_doorHome
	global state_doorHome_quiero
	
	#doorHomeOpen()
	print "1"
	state_doorHome_quiero = 1
	if ((state_doorHome == 0) and (state_doorHome_quiero == 1)) : #OPEN

		eule = [0,0,90]
		DoorHome_GEODE.setEuler(eule, viz.REL_LOCAL)
		Handle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Handle.setEuler (0,0,90,viz.ABS_GLOBAL)
		Handle_base.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Cham.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Rectangle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		state_doorHome = 1
	viz.waitTime(1.5)	
	viz.MainView.setEuler([91.56495666503906, 0.0, 0.0],viz.ABS_GLOBAL)
	viz.MainView.addAction(vizact.moveTo([8.994839668273926, 1.7999999523162842, 2.4486372470855713],speed=5))
	viz.waitTime(1.5)	
	viz.MainView.addAction(vizact.moveTo([9.266807556152344, 1.7999999523162842, 1.976346492767334],speed=5))
	viz.waitTime(1)
	viz.MainView.addAction(vizact.spinTo(euler=[132.5137939453125, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[161.66908264160156, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-174.32640075683594, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)	
	viz.MainView.addAction(vizact.moveTo( [9.00948715209961, 1.7999999523162842, -0.6137414574623108],speed=5))	
	viz.waitTime(1)
	viz.MainView.addAction(vizact.spinTo(euler=[-146.51657104492188, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-106.26224517822266, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-90.9167709350586, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.moveTo([-5.999731063842773, 1.7999999523162842, -1.218673586845398],speed=5))
	viz.waitTime(4.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-69.83829498291016, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[2.3058013916015625, 0.0, 0.0],speed=50))
	viz.waitTime(1.5)
	#doorSCOpen()
	state_doorSC_quiero = 1
	if state_doorSC == 0 and state_doorSC_quiero == 1 : #OPEN
			eule = [90,0,0]
			DoorSC_GEODE.setEuler(eule, viz.REL_LOCAL)
			state_doorSC = 1
	viz.waitTime(1.5)
	viz.MainView.addAction(vizact.moveTo([-5.458252429962158, 2.407294273376465, 1.1546337604522705],speed=5))
	viz.waitTime(1.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-23.51756477355957, 0.0, 0.0],speed=50))
	state_SV = 1
	
def SC_Casa():	
	global state_SV
	global state_doorSC
	global state_doorSC_quiero
	global state_doorHome
	global state_doorHome_quiero
	
	print "1"
	viz.MainView.addAction(vizact.moveTo([-5.9869184494018555, 1.7999999523162842, 3.805668592453003],speed=5))
	viz.MainView.addAction(vizact.spinTo(euler=[176.89329528808594, 0.0, 0.0],speed=50))
	
	
	viz.waitTime(1)
	
	#doorSCOpen()
	state_doorSC_quiero = 1
	if state_doorSC == 0 and state_doorSC_quiero == 1 : #OPEN
			eule = [90,0,0]
			DoorSC_GEODE.setEuler(eule, viz.REL_LOCAL)
			state_doorSC = 1
			
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.moveTo( [-5.757943153381348, 1.7999999523162842, -0.41311126947402954],speed=5))
	viz.MainView.addAction(vizact.spinTo(euler=[176.89329528808594, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[143.13424682617188, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[105.25570678710938, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[91.30744934082031, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.moveTo( [8.486791610717773, 1.7999999523162842, -0.6876856684684753],speed=5))
	viz.waitTime(1.5)
	viz.MainView.addAction(vizact.spinTo(euler=[54.74753189086914, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.moveTo( [9.370192527770996, 1.7999999523162842, -0.06330294907093048],speed=5))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[3.778843641281128, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[6.889291763305664, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.moveTo([9.843838691711426, 1.7999999523162842, 2.079324960708618],speed=5))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-29.747770309448242, 0.0, 0.0],speed=50))
	viz.waitTime(0.5)
	viz.MainView.addAction(vizact.spinTo(euler=[-64.44267272949219, 0.0, 0.0],speed=50))
	viz.waitTime(1)
	#DEBERIA PONERSE DELANTE DE LA PUERTA
	viz.MainView.addAction(vizact.spinTo(euler=[-89.92498779296875, 0.0, 0.0],speed=50))
	viz.waitTime(1.5)
	#doorHomeOpen
	state_doorHome_quiero = 1
	if ((state_doorHome == 0) and (state_doorHome_quiero == 1)) : #OPEN

		eule = [0,0,90]
		DoorHome_GEODE.setEuler(eule, viz.REL_LOCAL)
		Handle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Handle.setEuler (0,0,90,viz.ABS_GLOBAL)
		Handle_base.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Cham.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		Rectangle.setPosition(7.501148986816406, 1.8045035600662231, 3.7214875411987305,viz.ABS_GLOBAL)
		state_doorHome = 1
	
	print "4"
	viz.MainView.addAction(vizact.moveTo( [5.69581937789917, 1.7999999523162842, 2.0847556591033936],speed=5))
	viz.waitTime(2.5)
	state_SV = 0
	
#-------------------------------ABRIR Y CERRAR CAJA-------------------------------------------------------

def abrirModo1() :
	global state_SV
	global state_CajaModo1
	global state_CajaModo1_quiero
	state_CajaModo1_quiero = 1
	
	
	viz.MainView.addAction(vizact.spinTo(euler=[-1.5391184091567993, 0.0, 0.0],speed=50))
	viz.waitTime(1)
	viz.MainView.addAction(vizact.moveTo([3.5816447734832764, 1.1920483112335205, 6.965365886688232],speed=5))
	viz.waitTime(3)
	
	if ((state_CajaModo1 == 0) and (state_CajaModo1_quiero == 1)) :
		
		
		Tapa1.setEuler([-180,0,-130],viz.ABS_GLOBAL)
		Tapa1.setPosition([2.67,1.32,9],viz.ABS_GLOBAL)

		Tapa2.setEuler([-180,0,-230],viz.ABS_GLOBAL)
		Tapa2.setPosition([3.6,0.75,9],viz.ABS_GLOBAL)
		
		state_CajaModo1 = 1    #Decimos que la caja esta abierta en modo1
	
def cerrarModo1() :	
    global state_SV
    global state_CajaModo1
    global state_CajaModo1_quiero
    state_CajaModo1_quiero = 0 
    
    viz.MainView.addAction(vizact.spinTo(euler=[-1.5391184091567993, 0.0, 0.0],speed=50))
    viz.waitTime(1)
    viz.MainView.addAction(vizact.moveTo([3.5816447734832764, 1.1920483112335205, 6.965365886688232],speed=5))
    viz.waitTime(3)

    if ((state_CajaModo1 == 1) and (state_CajaModo1_quiero == 0)) :

	 
	 Tapa1.setEuler([-180.0, 1.2722218874358041e-14, -180.0],viz.ABS_GLOBAL)
	 Tapa1.setPosition([3.0, 0.5, 9.0],viz.ABS_GLOBAL)
	 
	 Tapa2.setEuler([-180.0, 1.2722218874358041e-14, -180.0],viz.ABS_GLOBAL)
	 Tapa2.setPosition([3.0, 0.5, 9.0],viz.ABS_GLOBAL)
	 
	 state_CajaModo1 = 0  #Decimos que la caja esta cerrada en modo1

def abrirModo2() :
    global state_SV
    global state_CajaModo2
    global state_CajaModo2_quiero
    state_CajaModo2_quiero = 1


    viz.MainView.addAction(vizact.spinTo(euler=[-1.5391184091567993, 0.0, 0.0],speed=50))
    viz.waitTime(1)
    viz.MainView.addAction(vizact.moveTo([3.5816447734832764, 1.1920483112335205, 6.965365886688232],speed=5))
    viz.waitTime(3)



    if ((state_CajaModo2 == 0) and (state_CajaModo2_quiero == 1)) :

     state_CajaModo2 = 1    #Decimos que la caja esta abierta en modo2

     Tapa.setEuler([-180,-30,-180],viz.ABS_GLOBAL)
     Tapa.setPosition([3,0.95,8.75],viz.ABS_GLOBAL)

     Tapa1.setEuler([-180,-30,-180],viz.ABS_GLOBAL)
     Tapa1.setPosition([3,0.95,8.75],viz.ABS_GLOBAL)

     Tapa2.setEuler([-180,-30,-180],viz.ABS_GLOBAL)
     Tapa2.setPosition([3,0.95,8.75],viz.ABS_GLOBAL)

	 #movimiento tornillo

     Tornillo1.setEuler([-180,-30,-180],viz.ABS_GLOBAL)
     Tornillo1.setPosition([3,0.95,8.75],viz.ABS_GLOBAL)

def cerrarModo2() :
	global state_SV
	global state_CajaModo2
	global state_CajaModo2_quiero
	state_CajaModo2_quiero = 0
	
	viz.MainView.addAction(vizact.spinTo(euler=[-1.5391184091567993, 0.0, 0.0],speed=50))
	viz.waitTime(1)
	viz.MainView.addAction(vizact.moveTo([3.5816447734832764, 1.1920483112335205, 6.965365886688232],speed=5))
	viz.waitTime(3)
	
	if ((state_CajaModo2 == 1) and (state_CajaModo2_quiero == 0)) :
		
		state_CajaModo2 = 0 #Decimos que la caja esta cerrada en modo2

		Tapa1.setEuler([-180.0, 1.2722218874358041e-14, -180.0],viz.ABS_GLOBAL)
		Tapa1.setPosition([3.0, 0.5, 9.0],viz.ABS_GLOBAL)
		
		Tapa.setEuler([-180.0, 1.2722218874358041e-14, -180.0],viz.ABS_GLOBAL)
		Tapa.setPosition([3.0, 0.5, 9.0],viz.ABS_GLOBAL)
		
		Tapa2.setEuler([-180.0, 1.2722218874358041e-14, -180.0],viz.ABS_GLOBAL)
		Tapa2.setPosition([3.0, 0.5, 9.0],viz.ABS_GLOBAL)

		Tornillo1.setEuler([-180.0, 1.2722218874358041e-14, -180.0],viz.ABS_GLOBAL)
		Tornillo1.setPosition([3.0, 0.5, 9.0],viz.ABS_GLOBAL)




########################FIN CODIGO NORMAL###################################################################

######################################### HTML CODE ###################################################################################

# test url: http://localhost:8080/vizhtml/custom_handler/device/name/value/value2/valuen?command=set&device=door&value=2

#Enable full screen anti-aliasing (FSAA) to smooth edges
# Display form submitted message on screen


nombre_equipo = socket.gethostname()
IP = socket.gethostbyname_ex(nombre_equipo)
info = vizinfo.InfoPanel(IP[2][1])

code = """

<html>
<head>
    <title>vizhtml Custom Handler Example</title>
</head>
<body onload="document.the_form.message.focus();">
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

class MyCORSHandler(vizhtml.PageRequestHandler):
    def handle_request(self,request):
        request.send_response(200)
        request.send_header("Content-type", "application/json")
        request.send_header("Access-Control-Allow-Origin", "*")
        request.end_headers()
        request.wfile.write('{"device":"doorHome", "state":"open","status":"OK"}')
        request.wfile.close()

class RequestHandler(vizhtml.PageRequestHandler):
    
    def handle_request(self,request):
        global status
        global state
        global device
        global cmd
        global device_id
        global code_
        print "handle_request task command" , request.command       

        if request.command=="GET": 

            print "handle_request query string:" , request.query_string

            print "handle request resource path: ", request.resource_path 
            
            code_ = "404"
            status = "FAILURE"

            query = request.query_string
            message = ""

            if(len(request.query_string)!=0 and request.command!="POST"):

				print 'dentroooo :', request.command

				try:

					if query is not None: 

						query_components = dict(qc.split("=") for qc in query.split("&"))
						print query_components['state'].replace("/","")
						query_components['state']=query_components['state'].replace("/","")
						print "query string data:" , query_components
						state = query_components['state'].replace("/","")
						device = query_components['device'].replace("/","")
						cmd = query_components['cmd'].replace("/","")
						device_id = query_components['device_id'].replace("/","")
						
					#Posibles estados:
						
						if(query_components['cmd']=='get_status'):
						 
						 if(device == 'doorHome' or device == 'doorSalon' or device == 'doorKitchen' or device == 'doorBath' 
						 or device == 'doorSC' or device == 'RollupBed' or device == 'RollupKit' or device == 'RollupSal'
						 or device == 'RollupSC' or device == 'KitchenLight' or device == 'SalaLight' 
						 or device == 'BedroomLight' or device == 'BathroomLight'
						 or device == 'SCLight' or device == 'RVLight' ):
						  code_ = "201"
						  status = "OK"
		
						if(query_components['device']=='doorHome'):
							state = state_doorHome
							device_id = "1"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									doorHomeOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									doorHomeClose()	
									state = query_components['state']
									status = "OK"
									code_ = "201"

						if(query_components['device']=='doorSalon'):
							state = state_doorsal
							device_id = "2"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									doorSalonOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									doorSalonClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
							
						if(query_components['device']=='doorKitchen'):
							state = state_doorkit
							device_id = "3"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									doorKitchenOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									doorKitchenClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						
						if(query_components['device']=='doorBath'):
							state = state_doorbath
							device_id = "4"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									doorbathOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									doorbathClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						if(query_components['device']=='doorSC'):
							state = state_doorSC
							device_id = "13"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									doorSCOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									doorSCClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
									
						if(query_components['device']=='RollupBed'):
							state = state_rollupbed
							device_id = "5"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									RollupBedOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									RollupBedClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								
						if(query_components['device']=='RollupKit'):
							state = state_rollupkit
							device_id = "6"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									RollupKitOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									RollupKitClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						if(query_components['device']=='RollupSal'):
							state = state_rollupsal
							device_id = "7"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									RollupSalOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									RollupSalClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								
						if(query_components['device']=='RollupSC'):
							state = state_rollupsc
							device_id = "12"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									RollupSCOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									RollupSCClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						if(query_components['device']=='KitchenLight'):
							state = state_KitLight
							device_id = "8"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									Kitchen_lightONOFFOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									Kitchen_lightONOFFClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						if(query_components['device']=='SalaLight'):
							state = state_SalaLight
							device_id = "9"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									Sala_lightONOFFOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									Sala_lightONOFFClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
									
						if(query_components['device']=='BedroomLight'):
							state = state_BedroomLight
							device_id = "11"
							if(query_components['cmd']=='set_status'):
								code_ = "405"
								if(query_components['state']=='open'):
									Bedroom_lightONOFFOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									Bedroom_lightONOFFClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
									
						if(query_components['device']=='BathroomLight'):
							state = state_BathroomLight
							device_id = "10"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									Bathroom_lightONOFFOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									Bathroom_lightONOFFClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						if(query_components['device']=='SCLight'):
							state = state_SCLight
							device_id = "15"
							if(query_components['cmd']=='set_status'):	
								if(query_components['state']=='open'):
									code_ = "405"
									SC_lightONOFFOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									SC_lightONOFFClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
						
						if(query_components['device']=='RVLight'):
							state = state_RVLight
							device_id = "14"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									RV_lightONOFFOpen()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									RV_lightONOFFClose()
									state = query_components['state']
									status = "OK"
									code_ = "201"
									
						if(query_components['device']=='CajaModo1'):
							state = state_CajaModo1
							device_id = "14"
							if(query_components['cmd']=='set_status'):	
								code_ = "405"
								if(query_components['state']=='open'):
									abrirModo1()
									state = query_components['state']
									status = "OK"
									code_ = "201"
								if(query_components['state']=='close'):
									cerrarModo1()
									state = query_components['state']
									status = "OK"
									code_ = "201"
							
								
						if(state==1):
						  state = 'open'
						if(state==0):
						  state = 'close'
						message=query_components['device']+query_components['state']
						
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
            device =""
            state = ""
            #NEW----------------------------------------------------------------------------------------
            cmd = "set_status"
            code = ""
            description = ""
            device_id = ""
            

        # If form was submitted, put message back into page
            if request.form_event:
             print "request: ", request.form_event
             try:
              device = cgi.escape(request.form_event.device)
              print "device, ",device
             except :
               print "no device in post"
             try:
              state = cgi.escape(request.form_event.state)
              print "state, ",state
             except :
               print "no state in post"
            # print "message, device , state",message, device, state
             if device is not None:
                if state is not None:
                   if(device=='doorHome' and state=='open'):
                    status = "OK"
                    device_id = "1"
                    code_ = "201"
                    doorHomeOpen() 
                   if(device=='doorHome' and state=='close'):
                    status = "OK"
                    device_id = "1"
                    code_ = "201"
                    doorHomeClose()
                   if(device=='doorSalon' and state=='open'):
                    status = "OK"
                    device_id = "2"
                    code_ = "201"
                    doorSalonOpen()	
                   if(device=='doorSalon' and state=='close'):
                    status = "OK"
                    device_id = "2"
                    code_ = "201"
                    doorSalonClose()
                   if(device=='doorBath' and state=='open'):status = "OK"; device_id = "4"; code_ = "201"; doorbathOpen()	
                   if(device=='doorBath' and state=='close'):status = "OK"; device_id = "4"; code_ = "201"; doorbathClose()	
                   if(device=='doorKitchen' and state=='open'):status = "OK"; device_id = "3"; code_ = "201"; doorKitchenOpen()		
                   if(device=='doorKitchen' and state=='close'):status = "OK"; device_id = "3"; code_ = "201"; doorKitchenClose()		
                   if(device=='doorSC' and state=='open'):status = "OK"; device_id = "5"; code_ = "201"; doorSCOpen()	
                   if(device=='doorSC' and state=='close'):status = "OK"; device_id = "5"; code_ = "201"; doorSCClose()	
                   if(device=='RollupBed' and state=='open'):status = "OK"; device_id = "6"; code_ = "201"; RollupBedOpen()	
                   if(device=='RollupBed' and state=='close'):status = "OK";device_id = "6"; code_ = "201"; RollupBedClose()
                   if(device=='RollupKit' and state=='open'):status = "OK"; device_id = "7"; code_ = "201"; RollupKitOpen()	
                   if(device=='RollupKit' and state=='close'):status = "OK"; device_id = "7"; code_ = "201"; RollupKitClose()
                   if(device=='RollupSal' and state=='open'):status = "OK"; device_id = "8"; code_ = "201"; RollupSalOpen()	
                   if(device=='RollupSal' and state=='close'):status = "OK"; device_id = "8"; code_ = "201"; RollupSalClose()	
                   if(device=='RollupSC' and state=='open'):status = "OK"; device_id = "9"; code_ = "201"; RollupSCOpen()
                   if(device=='RollupSC' and state=='close'):status = "OK"; device_id = "9"; code_ = "201"; RollupSCClose()	
                   if(device=='KitchenLight' and state=='open'):status = "OK"; device_id = "10"; code_ = "201"; Kitchen_lightONOFFOpen()	
                   if(device=='KitchenLight' and state=='close'):status = "OK"; device_id = "10"; code_ = "201"; Kitchen_lightONOFFClose()	
                   if(device=='SalaLight' and state=='open'):status = "OK"; device_id = "11"; code_ = "201"; Sala_lightONOFFOpen()	
                   if(device=='SalaLight' and state=='close'):status = "OK"; device_id = "11"; code_ = "201"; Sala_lightONOFFClose()	
                   if(device=='BedroomLight' and state=='open'):status = "OK"; device_id = "12"; code_ = "201"; Bedroom_lightONOFFOpen()	
                   if(device=='BedroomLight' and state=='close'):status = "OK"; device_id = "12"; code_ = "201"; Bedroom_lightONOFFClose()
                   if(device=='BathroomLight' and state=='open'):status = "OK"; device_id = "13"; code_ = "201"; Bathroom_lightONOFFOpen()	
                   if(device=='BathroomLight' and state=='close'):status = "OK"; device_id = "13"; code_ = "201"; Bathroom_lightONOFFClose()	
                   if(device=='SCLight' and state=='open'):status = "OK"; device_id = "14"; code_ = "201"; SC_lightONOFFOpen()	
                   if(device=='SCLight' and state=='close'):status = "OK"; device_id = "14"; code_ = "201";  SC_lightONOFFClose()
                   if(device=='RVLight' and state=='open'):status = "OK"; device_id = "15"; code_ = "201";  RV_lightONOFFOpen()
                   if(device=='RVLight' and state=='close'):status = "OK"; device_id = "15"; code_ = "201"; RV_lightONOFFClose()
                   if(device=='CajaModo1' and state=='open'):status = "OK"; code_ = "201"; abrirModo1()
                   if(device=='CajaModo1' and state=='close'):status = "OK"; code_ = "201"; cerrarModo1()
                   if(device=='CajaModo2' and state=='open'):status = "OK"; code_ = "201"; abrirModo2()
                   if(device=='CajaModo2' and state=='close'):status = "OK"; code_ = "201"; cerrarModo2()
                   if(device !='doorHome' and device != 'doorSalon' and device != 'doorBath' and device != 'doorKitchen' and device != 'RollupBed' and device != 'RollupKit' and device != 'RollupSal' and device != 'KitchenLight' and device != 'SalaLight' and device != 'BedroomLight' and device != 'BathroomLight' and device != 'SCLight' and device != 'RVLight' and device != 'RollupSC' and device != 'doorSC'):
                    code_ = "404"
                   if (state!='open' and state!='close'):
                    code_ = "405"
                   print "Device, State, status ", device, state, status
        #request.send_html_code('{"device":"bdd", "state":"st","status":"ss"}')
        print "Device, State, status ", device, state, status 
        if(code_ == "201"):
         response='{"version":"mercury","cmd":"'+cmd+'","code":"'+code_+'","description":"Echo response.","device_id":"'+device_id+'","device_name":"'+device+'","value":"'+state+'","status":"'+status+'"}'
        if(code_ == "404" or code_ == "405"):
         response='{"version":"mercury","cmd":"'+cmd+'","code":"'+code_+'","description":"Change device value.","device_id":"'+device_id+'","device_name":"'+device+'","value":"'+state+'","status":"'+status+'"}'
        if(code_ == "405" or code_ == "405"):
         response='{"version":"mercury","cmd":"'+cmd+'","code":"'+code_+'","description":"Change state value.","device_id":"'+device_id+'","device_name":"'+device+'","value":"'+state+'","status":"'+status+'"}'
        request.send_response(200)
        request.send_header("Content-type", "application/json")
        request.send_header("Access-Control-Allow-Origin", "*")
        request.end_headers()
        request.wfile.write(response)
        request.wfile.close()
        status="FAILURE"
        info.setText("device : "+device+" state : "+state)
        
vizhtml.registerHandlerClass('custom_handler',RequestHandler)
vizhtml.registerHandlerClass('another_handler',MyCORSHandler)

