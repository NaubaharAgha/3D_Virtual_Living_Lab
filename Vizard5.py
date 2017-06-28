import cgi
import viz
import vizinfo
import vizhtml
from urlparse import urlparse
# test url: http://localhost:8080/vizhtml/custom_handler/device/name/value/value2/valuen?command=set&device=door&value=2
#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)
viz.go()

# Display form submitted message on screen
info = vizinfo.InfoPanel('')

code = """
<html>
<head>
    <title>vizhtml Custom Handler Example</title>
</head>
<body onload="document.the_form.message.focus();">
<!-- <img src='ball.jpg'> -->
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
        print "handle_request task command" , request.command       
        if request.command=="GET": 
            print "handle_request query string:" , request.query_string                      
            print "handle request resource path: ", request.resource_path 
            query = request.query_string
            try:                
                if query is not None: 
                    query_components = dict(qc.split("=") for qc in query.split("&"))
                    print "query string data:" , query_components                                        if (query_components['device']=='doorHome'):                        piazza = viz.addChild('piazza.osgb')                        
            except ValueError:
                print "Oops!  That was an error on the query string.  Try again..."
            path = request.resource_path 
            try:
                if path is not None: 
                    path_components = path.split("/") 
                    print "path string array:" , path_components                    
            except ValueError:
                print "Oops!  That was an error on the path string.  Try again..."
        else:    
            viz.MainWindow.fov(60)
            piazza = viz.addChild('piazza.osgb')
            print "Post!  Draw data"
            
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