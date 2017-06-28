import socket

nombre_equipo = socket.gethostname()
IP = socket.gethostbyname_ex(nombre_equipo)

print "LA IP ES : ", IP
