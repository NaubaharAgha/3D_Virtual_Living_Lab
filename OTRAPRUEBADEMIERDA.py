﻿import viz
import vizcam
import vizact
import cgi, cgitb 
import vizinfo
import vizhtml

viz.go()
form = cgi.FieldStorage() 
viz.cam.setHandler(vizcam.KeyboardCamera())
viz.phys.enable()
viz.MainView.setPosition(-4, 1, -3)
viz.MainView.setEuler(30, 0, 0)

ground = viz.add('tut_ground.wrl')
viz.clearcolor([.5, .6, 1])
lab = viz.add('Living_Lab_Blinds_V2.OSGB', scale=[0.002]*3)
lab.setPosition([0, 0.258, 5])

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
    <input type="radio" name="subject" value="maths" /> Maths
    <input type="radio" name="subject" value="physics" /> Physics
    <input type="submit" value="Select Subject" />
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
         
        print request.log_request
        
        DoorHome_GEODE = lab.getChild('Door Principal').getChild ('Box101-OFFSET')
        eule = [0,0,90]
        DoorHome_GEODE.setEuler(eule, viz.REL_LOCAL)
    
        # If request is for a resource (e.g. image), then let vizhtml handle it
        if request.resource_path:
            return

        # If form was submitted, put message back into page
        if request.form_event:
            subject = cgi.escape(request.form_event.subject,True)
        else:
           subject = ''

        # Send html code with dynamic content
        request.send_html_code(code.format(subject=subject))


vizhtml.registerHandlerClass('custom_handler',ExampleRequestHandler,directory='.')

def HandleForm(e):
    info.setText(e.subject)
vizhtml.onFormSubmit(HandleForm)
